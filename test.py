import os
import sys
import yaml
import time
import re
import requests
import json
from datetime import datetime

try:
    import config
    from logger import (
        initialize_logger,
        log_info,
        log_debug,
        log_error,
        log_info_color,
        log_warning_color,
        TermColors,
        start_loading_animation,
        stop_loading_animation
    )
except ImportError as e:
    print(f"错误：无法从 NeoChat 项目导入必要的模块。请确保 test.py 与 config.py 和 logger.py 在同一目录下。")
    print(f"详细错误: {e}")
    sys.exit(1)

def call_llm_api(messages_payload):
    """
    一个独立的、简化的函数，用于调用LLM API。
    直接从main.py改编而来，移除了RAG和流式输出的复杂性，以适应剧情引擎的需求。
    返回完整的AI响应文本。
    """
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {config.API_KEY}"}
    payload = {
        "model": config.MODEL_NAME,
        "messages": messages_payload,
        "stream": False,
        "max_tokens": config.MAX_TOKENS,
        "temperature": config.TEMPERATURE
    }

    if config.DEBUG_MODE:
        log_debug("--- 发送给 LLM API 的 Payload ---")
        debug_payload_str = json.dumps(payload, ensure_ascii=False, indent=2)
        log_debug(debug_payload_str)
        log_debug("--- Payload 结束 ---")

    try:
        start_loading_animation(
            message=f"{TermColors.LIGHT_BLUE}{config.AI_NAME}正在思考{TermColors.RESET}",
            animation_style_key='moon'
        )
        response = requests.post(
            config.API_URL,
            headers=headers,
            json=payload,
            timeout=config.API_TIMEOUT_SECONDS
        )
        response.raise_for_status()
        stop_loading_animation(success=True)

        data = response.json()
        assistant_response = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        
        if assistant_response:
            log_debug(f"API完整响应已接收 (长度: {len(assistant_response)}).")
            return assistant_response.strip()
        else:
            log_warning_color("API调用成功，但响应内容为空。")
            return None

    except requests.exceptions.HTTPError as e:
        stop_loading_animation(success=False, final_message="API HTTP错误")
        log_error(f"API请求HTTP错误: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.RequestException as e:
        stop_loading_animation(success=False, final_message="API 请求失败")
        log_error(f"API请求失败: {e}")
    except Exception as e:
        stop_loading_animation(success=False, final_message="发生未知错误")
        log_error(f"处理API响应时发生未知错误: {e}")
    
    return None

class GameEngine:
    STORY_DIR = "story"

    def __init__(self):
        initialize_logger(config_debug_mode=config.DEBUG_MODE, app_name="AIGalgame_Engine")
        self.story_units = {}
        self.player_name = "玩家"
        self.ai_name = "AI"
        self.ai_persona = ""
        self.conversation_history = []
        self.current_unit_id = None
        
    def load_game_data(self):
        """加载所有剧情和角色配置文件"""
        log_info("开始加载游戏数据...")
        try:
            char_config_path = os.path.join(self.STORY_DIR, "character_config.txt")
            with open(char_config_path, 'r', encoding='utf-8') as f:
                char_config = yaml.safe_load(f)
                self.player_name = char_config.get("Player_Name", "风雪")
                self.ai_name = char_config.get("AI_Name", "浅川夏帆")
                self.ai_persona = char_config.get("AI_Persona", "")
                self.ai_persona = self._replace_placeholders(self.ai_persona)
                config.AI_NAME = self.ai_name
                log_info(f"角色配置加载成功: 玩家({self.player_name}), AI({self.ai_name})")

            for filename in os.listdir(self.STORY_DIR):
                if filename.endswith(".txt") and filename != "character_config.txt":
                    filepath = os.path.join(self.STORY_DIR, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        unit_data = yaml.safe_load(f)
                        unit_id = unit_data.get("UnitID")
                        if unit_id:
                            self.story_units[unit_id] = unit_data
                            log_debug(f"已加载剧情单元: {unit_id} ({unit_data.get('UnitName')})")
            
            if not self.story_units:
                log_error("未加载任何剧情单元！请检查 'story' 文件夹。")
                return False

            log_info_color("游戏数据加载完毕！", TermColors.GREEN)
            return True

        except FileNotFoundError as e:
            log_error(f"加载文件失败: {e}。请确保 story 文件夹和文件存在。")
            return False
        except yaml.YAMLError as e:
            log_error(f"解析剧情文件时出错: {e}。请检查文件格式是否为有效的YAML。")
            return False
        except Exception as e:
            log_error(f"加载游戏数据时发生未知错误: {e}")
            return False

    def _replace_placeholders(self, text):
        """替换文本中的占位符"""
        if not isinstance(text, str):
            return text
        now = datetime.now()
        text = text.replace("[玩家名]", self.player_name)
        text = text.replace("[AI名]", self.ai_name)
        text = text.replace("<时间>", now.strftime("%H:%M"))
        return text

    def _call_llm(self, prompt_text, for_judgement=False):
        """
        核心LLM调用函数，负责构建完整的上下文并调用API。
        根据模型特性，将剧情指令包装在user角色中发送。
        """
        messages = []
        
        if not for_judgement:
            messages.append({"role": "system", "content": self.ai_persona})
            messages.extend(self.conversation_history)
        
        if for_judgement:
            final_prompt = {"role": "system", "content": self._replace_placeholders(prompt_text)}
        else:
            final_prompt_content = f"System: {self._replace_placeholders(prompt_text)}"
            final_prompt = {"role": "user", "content": final_prompt_content}
        
        messages.append(final_prompt)
        
        response_text = call_llm_api(messages)
        
        return response_text

    def run(self):
        """启动并运行游戏主循环"""
        if not self.load_game_data():
            return
        
        self.current_unit_id = "Classroom_01" 
        
        while self.current_unit_id:
            unit_data = self.story_units.get(self.current_unit_id)
            if not unit_data:
                log_error(f"找不到ID为 '{self.current_unit_id}' 的剧情单元。游戏结束。")
                break
            
            self.process_unit(unit_data)
        
        log_info_color("\n=============== 游戏结束 ===============\n", TermColors.YELLOW)

    def process_unit(self, unit_data):
        """处理单个剧情单元的所有事件和结束条件"""
        unit_name = self._replace_placeholders(unit_data.get('UnitName', '未知场景'))
        cg = unit_data.get('SceneCG', '无')
        bgm = unit_data.get('BGM', '无')
        
        print("\n" + "="*50)
        log_info_color(f"进入场景: {unit_name}", TermColors.CYAN)
        log_debug(f"场景资源: CG({cg}), BGM({bgm})")
        print("="*50 + "\n")
        time.sleep(1)

        for event in unit_data.get("Events", []):
            event_type = event.get("Type")
            if event_type == "Narration":
                self._handle_narration(event)
            elif event_type == "Dialogue":
                self._handle_dialogue(event)
            elif event_type == "WaitForPlayerInput":
                self._handle_player_input(event)
            time.sleep(0.5)

        end_condition = unit_data.get("EndCondition", {})
        end_type = end_condition.get("Type")

        next_unit = None
        if end_type == "Linear":
            next_unit = self._handle_linear_end(end_condition)
        elif end_type == "Branching":
            next_unit = self._handle_branching_end(end_condition)
        elif end_type == "FreeTime":
            next_unit = self._handle_freetime_end(end_condition)
        
        self.current_unit_id = next_unit

    def _handle_narration(self, event):
        content = self._replace_placeholders(event.get("Content", ""))
        mode = event.get("Mode", "Preset")
        
        if mode == "Prompt":
            response = self._call_llm(content)
            if response:
                content = response
        
        log_info_color(f"旁白: {content}", TermColors.GREY)

    def _handle_dialogue(self, event):
        character = self._replace_placeholders(event.get("Character", "??"))
        content = self._replace_placeholders(event.get("Content", ""))
        mode = event.get("Mode", "Preset")
        
        if mode == "Prompt":
            response = self._call_llm(content)
            if response:
                content = response
            else:
                content = "(思考良久，但什么也没说...)"

        print(f"{TermColors.CYAN}{character}:{TermColors.RESET} {content}")
        if character == self.ai_name:
            self.conversation_history.append({"role": "assistant", "content": content})
            log_debug(f"已将AI回复加入历史记录。当前历史长度: {len(self.conversation_history)}")

    def _handle_player_input(self, event):
        instruction = self._replace_placeholders(event.get("InstructionToPlayer", ""))
        if instruction:
            log_info_color(f"系统提示: {instruction}", TermColors.YELLOW)
        
        user_input = ""
        while not user_input:
            user_input = input(f"{TermColors.YELLOW}{self.player_name}:{TermColors.RESET} ").strip()
        
        self.conversation_history.append({"role": "user", "content": user_input})
        log_debug(f"已将玩家输入加入历史记录。当前历史长度: {len(self.conversation_history)}")

    def _handle_linear_end(self, end_condition):
        return end_condition.get("NextUnitID")

    def _handle_branching_end(self, end_condition):
        method = end_condition.get("Method")
        if method == "PlayerChoice":
            return self._handle_player_choice(end_condition)
        elif method == "AIChoice":
            return self._handle_ai_choice(end_condition)
        return None

    def _handle_player_choice(self, end_condition):
        branches = end_condition.get("Branches", {})
        log_info_color("剧情走到了分歧点，请做出你的选择：", TermColors.MAGENTA)
        
        options = {}
        for key, value in branches.items():
            options[key] = value['DisplayText']
            print(f"  {TermColors.GREEN}[{key}]{TermColors.RESET} {self._replace_placeholders(options[key])}")
        
        choice = ""
        while choice not in options:
            choice = input("请输入你的选择 (A, B, ...): ").upper()
            if choice not in options:
                log_error("无效的选项，请重新输入。")

        choice_text = f"（你选择了：'{options[choice]}'）"
        self.conversation_history.append({"role": "user", "content": choice_text})
        log_debug(f"玩家选择已记录: {choice_text}")

        return branches[choice]['NextUnitID']
        
    def _handle_ai_choice(self, end_condition):
        log_info_color(f"{self.ai_name} 似乎正在做出重要的决定...", TermColors.MAGENTA)
        
        decision_prompt = end_condition.get("DecisionPromptForAI")
        ai_decision_text = self._call_llm(decision_prompt)
        
        if not ai_decision_text:
            log_error("AI决策失败，无法继续剧情。")
            return None

        print(f"{TermColors.CYAN}{self.ai_name}:{TermColors.RESET} {ai_decision_text}")
        self.conversation_history.append({"role": "assistant", "content": ai_decision_text})

        log_debug("正在调用系统LLM来判断AI的选择...")
        judge_prompt = end_condition.get("JudgePromptForSystem")
        judge_prompt = judge_prompt.replace("{AI_LAST_RESPONSE}", ai_decision_text)
        
        judgement = self._call_llm(judge_prompt, for_judgement=True)
        
        if judgement:
            judgement = judgement.strip().upper()
            log_debug(f"系统判断结果: '{judgement}'")
            branches = end_condition.get("Branches", {})
            if judgement in branches:
                return branches[judgement]
            else:
                log_error(f"系统判断返回了无效选项 '{judgement}'，将随机选择一个分支。")
                return list(branches.values())[0]
        else:
            log_error("系统判断AI选择失败，将随机选择一个分支。")
            return list(end_condition.get("Branches", {}).values())[0]

    def _handle_freetime_end(self, end_condition):
        instruction = self._replace_placeholders(end_condition.get("InstructionToPlayer", ""))
        exit_phrase = "时间不早了"
        
        log_info_color(instruction, TermColors.YELLOW)
        
        while True:
            user_input = input(f"{TermColors.YELLOW}{self.player_name}:{TermColors.RESET} ").strip()
            
            if exit_phrase in user_input:
                log_info("自由时间结束。")
                self.conversation_history.append({"role": "user", "content": user_input})
                break

            self.conversation_history.append({"role": "user", "content": user_input})
            
            ai_response = self._call_llm(prompt_text=f"这是你的内心活动：请自然地回应[玩家名]的话。")
            
            if ai_response:
                print(f"{TermColors.CYAN}{self.ai_name}:{TermColors.RESET} {ai_response}")
                self.conversation_history.append({"role": "assistant", "content": ai_response})
            else:
                print(f"{TermColors.CYAN}{self.ai_name}:{TermColors.RESET} (我...我不知道该说什么了...)")
        
        return end_condition.get("NextUnitID")


if __name__ == "__main__":
    if not config.API_KEY or "your_" in config.API_KEY:
        log_error("错误：请在 .env 文件中正确设置您的 API_KEY。")
    else:
        engine = GameEngine()
        engine.run()