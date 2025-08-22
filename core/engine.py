# core/engine.py
from .models import GameSession
from .state_manager import StateManager
from .event_handler import EventHandler
from .ui import ConsoleUI
from .save_manager import SaveManager
from .llm_interface import chat_with_deepseek
from .logger import log_info, log_error, log_debug, log_info_color, TermColors

class GameEngine:
    """
    游戏主引擎，负责驱动游戏循环和协调各个组件。
    """
    def __init__(self, session: GameSession):
        self.session = session
        self.is_running = True
        self.game_over = False

        # 初始化核心组件
        self.ui = ConsoleUI()
        self.state = StateManager(self.session)
        self.event_handler = EventHandler(self.state, self.ui)
        self.save_manager = SaveManager()

    def run(self):
        """主游戏循环。"""
        log_info_color("游戏开始！在任何你需要输入的时候，都可以使用 /save 命令。", TermColors.GREEN)
        
        while self.is_running and not self.game_over:
            current_state = self.state.progress.runtime_state
            
            if current_state == 'ExecutingEvents':
                self._execute_events()
            elif current_state == 'WaitingForPlayerInput':
                self._wait_for_player_input()
            elif current_state == 'WaitingForPlayerChoice':
                self._wait_for_player_choice()
            elif current_state == 'InFreeTime':
                self._handle_free_time()
            else:
                log_error(f"未知的游戏状态: {current_state}, 游戏结束。")
                self.game_over = True

        log_info_color("游戏结束。", TermColors.MAGENTA)

    def _execute_events(self):
        """循环执行当前剧情单元中的事件，直到需要暂停或单元结束。"""
        while self.state.progress.runtime_state == 'ExecutingEvents':
            next_event = self.state.get_next_event()
            
            if next_event:
                should_continue = self.event_handler.handle_event(next_event)
                self.state.advance_event_pointer()
                if not should_continue:
                    break
            else:
                self._process_end_condition()
                break

    def _process_end_condition(self):
        """处理当前剧情单元的结束条件。"""
        unit = self.state.get_current_story_unit()
        if not unit or not unit.end_condition:
            log_info("剧情单元结束，无EndCondition，游戏结束。")
            self.game_over = True
            return

        end_data = self.state.format_string(unit.end_condition)
        end_type = end_data.get('Type')
        log_debug(f"处理EndCondition: {end_type}")

        if end_type == 'Linear':
            self.state.transition_to_unit(end_data.get('NextUnitID'))
        
        elif end_type in ['FreeTime', 'LimitedFreeTime']:
            self.state.progress.runtime_state = 'InFreeTime'
            self.state.progress.context['free_time_config'] = end_data
            self.state.progress.context['turns_taken'] = 0
            self.ui.display_system_message(end_data.get('InstructionToPlayer', '进入自由活动时间。'), color=TermColors.BLUE)

        elif end_type == 'Branching':
            method = end_data.get('Method')
            if method == 'PlayerChoice':
                self.state.progress.runtime_state = 'WaitingForPlayerChoice'
                self.state.progress.context['choices_config'] = end_data.get('Branches', {})
            elif method == 'AIChoice':
                self._execute_ai_choice(end_data)
            else:
                log_error(f"未知的 Branching Method: {method}")
                self.game_over = True

        elif end_type == 'Conditional':
            found_match = False
            for case in end_data.get('Cases', []):
                if self.state.evaluate_condition(case['Condition']):
                    # 递归处理 'Then' 中的EndCondition
                    self._process_end_condition_recursively(case['Then'])
                    found_match = True
                    break
            if not found_match and 'Else' in end_data:
                self._process_end_condition_recursively(end_data['Else'])
        
        else:
            log_error(f"未知的EndCondition类型: {end_type}")
            self.game_over = True

    def _process_end_condition_recursively(self, end_data):
        """用于Conditional内部的递归调用，避免重复日志。"""
        # 这是一个简化的包装器，实际逻辑仍在 _process_end_condition 中
        # 为了避免无限递归，这里可以添加深度检查
        unit = self.state.get_current_story_unit()
        unit.end_condition = end_data # 临时替换
        self._process_end_condition()


    def _wait_for_player_input(self):
        """处理玩家输入状态。"""
        prompt = self.state.progress.context.get('prompt')
        user_input = self.ui.prompt_for_input(self.state.format_string(prompt))
        
        if self._handle_system_commands(user_input):
            return

        final_input = user_input
        if not user_input.strip() and prompt:
            final_input = self.state.format_string(prompt)
            self.ui.display_system_message(f"(使用默认): {final_input}", color=TermColors.YELLOW)

        self.state.runtime_context['player_input'] = final_input
        self.state.add_dialogue_history('Player', content=final_input)
        self.state.progress.runtime_state = 'ExecutingEvents'

    def _wait_for_player_choice(self):
        """处理玩家选择状态。"""
        choices_data = self.state.progress.context.get('choices_config', {})
        display_choices = {key: self.state.format_string(branch['DisplayText']) for key, branch in choices_data.items()}
        self.ui.display_choices(display_choices)
        
        while True:
            user_choice = self.ui.prompt_for_input().upper()
            if self._handle_system_commands(user_choice):
                # 如果是系统命令，重新显示选项并等待
                self.ui.display_choices(display_choices)
                continue

            if user_choice in choices_data:
                next_unit_id = choices_data[user_choice]['NextUnitID']
                self.state.transition_to_unit(next_unit_id)
                break
            else:
                self.ui.display_system_message("无效的选择，请重新输入。", color=TermColors.RED)

    def _handle_free_time(self):
        """处理自由活动时间的玩家输入和AI回应。"""
        config = self.state.progress.context['free_time_config']
        user_input = self.ui.prompt_for_input()

        if self._handle_system_commands(user_input):
            return

        # 检查退出指令
        exit_prompt = config.get('ExitPromptInInputBox', '')
        if exit_prompt and exit_prompt in user_input:
            log_info("检测到退出语，自由时间结束。")
            self.state.transition_to_unit(config['NextUnitID'])
            return

        self.state.add_dialogue_history('Player', content=user_input)
        
        # AI 回应逻辑 (简化版，可扩展为轮询)
        # 默认让DM或第一个角色回应
        responder_id = config.get('InteractWith', [self.state.session.story_pack_config.dm_role_id or list(self.state.session.characters.keys())[0]])[0]
        responder = self.state.session.characters.get(responder_id)

        if responder:
            messages = [{"role": "system", "content": self.state.format_string(responder.prompt)}]
            # 添加历史上下文
            for record in self.state.dialogue_history[-10:]:
                # ... (构建历史消息的逻辑)
                pass
            messages.append({"role": "user", "content": user_input})
            
            response = chat_with_deepseek(messages, responder.name, color_code=TermColors.CYAN)
            if response:
                self.state.add_dialogue_history('Dialogue', character_id=responder_id, content=response)

        # 检查回合数限制
        self.state.progress.context['turns_taken'] += 1
        if config['Type'] == 'LimitedFreeTime' and self.state.progress.context['turns_taken'] >= config['MaxTurns']:
            log_info("达到最大轮次，自由时间结束。")
            self.state.transition_to_unit(config['NextUnitID'])

    def _execute_ai_choice(self, config: dict):
        """执行 AI 决策逻辑。"""
        log_info_color("AI 正在做出决定...", TermColors.BLUE)
        decider_id = config['DeciderCharacterID']
        decider = self.state.session.characters.get(decider_id)
        if not decider:
            log_error(f"AI Choice 失败：找不到决策角色 '{decider_id}'。")
            self.game_over = True
            return

        # 1. 决策 Call
        decision_prompt = self.state.format_string(config['DecisionPromptForAI'])
        messages = [{"role": "system", "content": self.state.format_string(decider.prompt)}]
        # ... (构建历史消息)
        messages.append({"role": "system", "content": decision_prompt})
        ai_decision_text = chat_with_deepseek(messages, character_name=f"{decider.name}(内心)", is_internal_thought=True)
        if not ai_decision_text:
            log_error("AI 未能做出决策。")
            self.game_over = True
            return
        log_debug(f"AI 决策原文: {ai_decision_text}")

        # 2. 判断 Call
        judge_prompt = self.state.format_string(config['JudgePromptForSystem'])
        judge_messages = [
            {"role": "system", "content": judge_prompt},
            {"role": "user", "content": f"请根据以下AI角色的决策文本进行判断：\n\n---\n{ai_decision_text}\n---"}
        ]
        judged_result = chat_with_deepseek(judge_messages, character_name="系统判断", is_internal_thought=True)
        if not judged_result:
            log_error("系统未能判断 AI 的决策。")
            self.game_over = True
            return

        # 3. 转换剧情
        final_choice = judged_result.strip().upper()
        log_info_color(f"AI 的选择已被系统判断为: '{final_choice}'", TermColors.GREEN)
        
        branches = config.get('Branches', {})
        if final_choice in branches:
            self.state.transition_to_unit(branches[final_choice])
        else:
            log_error(f"判断结果 '{final_choice}' 无效，在 Branches 中找不到匹配项。")
            self.game_over = True

    def _handle_system_commands(self, user_input: str) -> bool:
        """处理系统命令，如 /save。返回 True 表示已处理，无需后续操作。"""
        if user_input.lower().startswith('/save'):
            save_name = user_input[5:].strip() or f"手动存档_{datetime.now().strftime('%H%M%S')}"
            self.save_manager.save_game_session(self.session, save_name)
            return True
        return False