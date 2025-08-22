# core/event_handler.py
from typing import Any, Dict

from .state_manager import StateManager
from .ui import ConsoleUI
from .llm_interface import chat_with_deepseek
from .logger import log_debug, log_error, log_info, log_info_color, TermColors

class EventHandler:
    """
    处理单个剧情事件，执行其逻辑。
    这是一个无状态的类，所有状态都由 StateManager 管理。
    """
    def __init__(self, state_manager: StateManager, ui: ConsoleUI):
        self.state = state_manager
        self.ui = ui
        
        # 事件分派表，将事件类型映射到处理函数
        self.handlers = {
            'Narration': self._handle_narration,
            'Dialogue': self._handle_dialogue,
            'Player': self._handle_player,
            'Action': self._handle_action,
            'Chapter': self._handle_chapter,
            'Notice': self._handle_notice,
            'PlayerNotice': self._handle_player_notice,
            'SystemAction': self._handle_system_action,
        }

    def handle_event(self, event_data: Dict[str, Any]) -> bool:
        """
        事件处理的入口点。
        返回 True 表示游戏可以继续自动执行，False 表示需要等待（如玩家输入）。
        """
        log_debug(f"处理事件: {event_data}")

        # 处理条件
        if 'Condition' in event_data:
            if not self.state.evaluate_condition(event_data['Condition']):
                log_debug("条件不满足，跳过事件块。")
                return True # 跳过也算成功，继续执行
            # 如果条件满足，递归处理嵌套的Events
            for nested_event in event_data.get('Events', []):
                if not self.handle_event(nested_event):
                    return False # 如果嵌套事件需要暂停，则整个事件块暂停
            return True

        # 解析事件类型和内容
        # 确保 event_data 不为空
        if not event_data:
            log_error("接收到空的事件数据。")
            return True

        event_key, event_content = list(event_data.items())[0]
        params = dict(param.strip().split(': ') for param in event_key.split(' | '))
        event_type = params.get('Type')

        # 格式化内容
        if isinstance(event_content, str):
            content = self.state.format_string(event_content)
        elif isinstance(event_content, dict):
            content = {k: self.state.format_string(v) for k, v in event_content.items()}
        else:
            content = event_content

        # 分派到具体的处理函数
        handler = self.handlers.get(event_type)
        if handler:
            return handler(params, content)
        else:
            log_error(f"未知的事件类型: {event_type}")
            return True # 遇到未知事件，跳过并继续

    # --- 已有事件处理器 (保持不变) ---
    def _handle_narration(self, params: Dict, content: str) -> bool:
        if params.get('Mode') == 'Prompt':
            narrator_prompt = "你是一个优秀的、沉浸式的故事讲述者（旁白）。请根据以下要求和对话历史，生成一段富有文采的旁白。直接输出旁白内容，不要包含任何额外解释。"
            messages = [
                {"role": "system", "content": narrator_prompt},
                {"role": "user", "content": f"这是你的生成要求：\n{content}"}
            ]
            generated_content = chat_with_deepseek(messages, character_name="旁白", color_code=TermColors.GREY)
            if generated_content:
                self.state.add_dialogue_history('Narration', content=generated_content)
            else:
                log_error("旁白生成失败。")
        else: # Preset
            self.ui.display_narration(content)
            self.state.add_dialogue_history('Narration', content=content)
        return True

    def _handle_dialogue(self, params: Dict, content: str) -> bool:
        char_id = self.state.format_string(params['Character'])
        character = self.state.session.characters.get(char_id)
        if not character:
            log_error(f"对话事件错误: 找不到角色ID '{char_id}'")
            return True

        if params.get('Mode') == 'Preset':
            self.ui.display_dialogue(character.name, content)
            self.state.add_dialogue_history('Dialogue', character_id=char_id, content=content)
        
        elif params.get('Mode') == 'Prompt':
            messages = [{"role": "system", "content": self.state.format_string(character.prompt)}]
            # 此处可以添加逻辑来构建更丰富的历史上下文
            messages.append({"role": "user", "content": f"这是你的内心独白或行为指引，请根据它生成一句对话。不要把内心独白本身说出来。\n内心独白: {content}"})
            
            response = chat_with_deepseek(messages, character.name, color_code=TermColors.CYAN)
            if response:
                self.state.add_dialogue_history('Dialogue', character_id=char_id, content=response)
            else:
                log_error("LLM未能生成响应。")
        return True

    def _handle_player(self, params: Dict, content: str) -> bool:
        if params.get('Mode') == 'Input':
            self.state.progress.runtime_state = 'WaitingForPlayerInput'
            self.state.progress.context['prompt'] = content
            return False
        
        elif params.get('Mode') == 'Preset':
            self.ui.display_player_dialogue(self.state.session.player.name, content)
            self.state.add_dialogue_history('Player', content=content)
            return True
        return True

    def _handle_action(self, params: Dict, content: Dict) -> bool:
        tool = params.get('Tool')
        var_name = params.get('Variable')
        
        if tool == 'Set':
            self.state.set_variable(var_name, content.get('Value'))
        elif tool == 'Calculate':
            self.state.calculate_variable(var_name, content.get('Expression'))
        elif tool == 'Random':
            self.state.set_random_variable(var_name, content.get('Min'), content.get('Max'))
        elif tool == 'RandomChoice':
            self.state.set_random_choice_variable(var_name, content.get('Choices'))
        else:
            log_error(f"未知的 Action Tool: {tool}")
        return True

    def _handle_chapter(self, params: Dict, content: Dict) -> bool:
        self.ui.display_chapter(content.get('Title'), content.get('Description'))
        self.state.add_dialogue_history('Chapter', **content)
        return True

    # --- 新增事件处理器 ---

    def _handle_notice(self, params: Dict, content: str) -> bool:
        """处理游戏内公告，对玩家和LLM都可见。"""
        final_content = content
        if params.get('Mode') == 'Prompt':
            log_info("正在生成公告内容...")
            dm_char_id = self.state.session.story_pack_config.dm_role_id
            dm_char = self.state.session.characters.get(dm_char_id)
            
            dm_prompt = "你是一个剧本杀的DM（主持人）。"
            dm_name = "DM"
            if dm_char:
                dm_prompt = self.state.format_string(dm_char.prompt)
                dm_name = dm_char.name

            messages = [
                {"role": "system", "content": dm_prompt},
                {"role": "user", "content": f"请根据以下要求生成一条公告:\n{content}"}
            ]
            generated_content = chat_with_deepseek(messages, character_name=dm_name, color_code=TermColors.MAGENTA)
            if generated_content:
                final_content = generated_content
            else:
                log_error("公告生成失败。")
                return True # 即使失败也继续游戏

        location = params.get('Location', 'popup')
        self.ui.display_system_message(f"--- [{location.upper()}] 公告 ---\n{final_content}\n--------------------", color=TermColors.MAGENTA)
        self.state.add_dialogue_history('Notice', location=location, content=final_content)
        return True

    def _handle_player_notice(self, params: Dict, content: str) -> bool:
        """处理仅玩家可见的系统提示，不计入对话历史。"""
        self.ui.display_system_message(f"[系统提示]: {content}", color=TermColors.BLUE)
        # 注意：这里故意不调用 add_dialogue_history
        return True

    def _handle_system_action(self, params: Dict, content: str) -> bool:
        """处理后台系统动作，通常是调用LLM生成内容并存入变量。"""
        tool = params.get('Tool')
        var_name = params.get('Variable')
        if not tool or not var_name:
            log_error(f"SystemAction 事件缺少 Tool 或 Variable 参数: {params}")
            return True

        if tool == 'Generate':
            log_info_color("AI 正在幕后构思剧情...", TermColors.MAGENTA)
            system_prompt = "你是一个富有创造力的游戏剧本助手。请根据以下要求完成任务，并直接输出结果，不要包含任何额外解释。"
            
            # 此处可以添加更复杂的逻辑来包含历史记录，就像旧代码中一样
            # 为了简洁，我们暂时只发送当前prompt
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": content}
            ]

            generated_content = chat_with_deepseek(messages, character_name="幕后导演", is_internal_thought=True)
            if generated_content:
                self.state.set_variable(var_name, generated_content.strip())
                log_debug(f"SystemAction 执行完毕, 变量 '{var_name}' 已设置。")
            else:
                log_error(f"SystemAction 未能从LLM生成内容，变量 '{var_name}' 未设置。")
        else:
            log_error(f"未知的 SystemAction Tool: {tool}")
        
        # 注意：后台动作不计入对话历史
        return True