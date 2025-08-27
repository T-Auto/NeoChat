import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

from neochat.platform.configuration import config
from neochat.platform.logging import initialize_logger, log_error, log_info_color, TermColors
from neochat.llm.client import generate_chat_response


class PromptToolkitColors:
    YELLOW = 'yellow'
    GREEN = 'green'
    MAGENTA = 'magenta'
    BOLD = 'bold' 

def check_api_key():
    """检查并验证API密钥是否已配置。"""
    try:
        active_provider_name = config.llm.active_provider
        active_provider_config = getattr(config.llm.providers, active_provider_name)
        api_key_value = active_provider_config.api_key

        if not api_key_value or "YOUR" in str(api_key_value):
            log_error("错误: 请在项目根目录的 '.env' 文件中设置你的 API_KEY。")
            return False
        return True
    except AttributeError as e:
        log_error(f"配置错误: 无法获取 LLM API 密钥。请检查 config.yaml。错误: {e}")
        return False
    except Exception as e:
        log_error(f"初始化LLM配置时发生未知错误: {e}")
        return False

def main():
    """程序主入口点。"""
    load_dotenv()
    initialize_logger(app_name="NeoChat-DirectChat", config_debug_mode=config.debug.mode)
    
    if not check_api_key():
        input("按回车键退出...")
        return

    chat_system_prompt = os.getenv("CHAT_SYSTEM_PROMPT", "你是一个AI助手。")
    messages = [{"role": "system", "content": chat_system_prompt}]

    log_info_color("欢迎来到 NeoChat 直接聊天模式！", TermColors.GREEN)
    print_formatted_text(FormattedText([
        (PromptToolkitColors.YELLOW, "说明: "),
        ("", "输入你的消息后按 "),
        (PromptToolkitColors.BOLD, "Alt+Enter"),
        ("", " 发送。"),
    ]))
    print_formatted_text(FormattedText([
        (PromptToolkitColors.YELLOW, "      "),
        ("", "在输入时按 "),
        (PromptToolkitColors.BOLD, "Enter"),
        ("", " 进行换行。"),
    ]))
    print_formatted_text(FormattedText([
        (PromptToolkitColors.YELLOW, "      "),
        ("", "输入 "),
        (PromptToolkitColors.BOLD, "/exit"),
        ("", " 或 "),
        (PromptToolkitColors.BOLD, "quit"),
        ("", " 退出聊天。"),
    ]))
    print("-" * 30)

    try:
        while True:
            user_input = prompt(
                [(PromptToolkitColors.YELLOW, '> 你: ')],
                multiline=True,
                prompt_continuation='  '
            )

            if not user_input.strip():
                continue

            if user_input.lower() in ["/exit", "quit"]:
                log_info_color("再见！", TermColors.MAGENTA)
                break

            messages.append({"role": "user", "content": user_input})

            response_text = generate_chat_response(
                messages,
                character_name="AI",
                color_code=TermColors.CYAN 
            )

            if response_text:
                messages.append({"role": "assistant", "content": response_text})
            else:
                log_error("未能从AI获取回应，请检查网络或API配置。")
                messages.pop()

    except (KeyboardInterrupt, EOFError):
        print("\n")
        log_info_color("聊天被中断。再见！", TermColors.MAGENTA)

if __name__ == "__main__":
    main()