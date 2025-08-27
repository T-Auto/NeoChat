import os
import sys
import yaml
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
from prompt_toolkit import prompt, Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

# 导入日志和动画模块
from neochat.platform.logging import initialize_logger, log_error, log_info_color, TermColors, start_loading_animation, stop_loading_animation

# 导入 LLM 客户端实现
from neochat.llm.clients.base import BaseLLMClient
from neochat.llm.clients.openai_compatible import OpenAICompatibleClient
from neochat.llm.clients.gemini import GeminiClient

# 客户端类型映射
CLIENT_MAPPING = {
    "openai_compatible": OpenAICompatibleClient,
    "gemini": GeminiClient
}

class PromptToolkitColors:
    YELLOW = 'yellow'
    GREEN = 'green'
    MAGENTA = 'magenta'
    BOLD = 'bold'
    REVERSE = 'reverse'

def select_from_list(title: str, options: List[str]) -> Optional[str]:
    """
    使用 prompt_toolkit Application 创建一个稳定的交互式列表供用户选择。
    """
    selected_index = 0
    
    # 定义按键绑定
    bindings = KeyBindings()

    # --- BUG 修复在这里 ---
    # 将 @bindings.handle 改为 @bindings.add
    @bindings.add("up")
    def _(event):
        nonlocal selected_index
        selected_index = (selected_index - 1 + len(options)) % len(options)

    @bindings.add("down")
    def _(event):
        nonlocal selected_index
        selected_index = (selected_index + 1) % len(options)

    @bindings.add("enter")
    def _(event):
        event.app.exit(result=options[selected_index])

    @bindings.add("c-c")
    @bindings.add("q")
    def _(event):
        event.app.exit(result=None)
    # --- 修复结束 ---

    # 定义如何动态生成菜单的显示内容
    def get_menu_text():
        formatted_menu = [
            ('class:title', f"{title}\n"),
            ('', ' (使用 ↑/↓ 选择, Enter 确认, Q 退出)\n\n')
        ]
        for i, option in enumerate(options):
            if i == selected_index:
                formatted_menu.append(('class:selected', f"> {option}\n"))
            else:
                formatted_menu.append(('', f"  {option}\n"))
        return FormattedText(formatted_menu)

    # 定义样式
    style = Style.from_dict({
        'title': 'bold',
        'selected': 'reverse',
    })
    
    # 创建布局和应用
    layout = Layout(Window(content=FormattedTextControl(
        text=get_menu_text,
        key_bindings=bindings,
        focusable=True
    )))

    app = Application(layout=layout, style=style, full_screen=False)
    
    # 运行应用并返回结果
    result = app.run()
    return result

def initialize_llm_client(provider_config: Dict[str, Any]) -> Optional[BaseLLMClient]:
    """根据选择的提供商配置，实例化并返回一个LLM客户端。"""
    client_type = provider_config.get("type")
    ClientClass = CLIENT_MAPPING.get(client_type)
    
    if not ClientClass:
        log_error(f"配置错误: 不支持的客户端类型 '{client_type}'")
        return None

    api_key_env = provider_config.get("api_key_env")
    api_key = os.getenv(api_key_env)

    if not api_key or "YOUR" in api_key:
        log_error(f"错误: 请在项目根目录的 '.env' 文件中设置环境变量 '{api_key_env}'。")
        return None

    # 构建传递给客户端构造函数的配置字典
    client_init_config = provider_config.get("config", {})
    client_init_config['api_key'] = api_key
    client_init_config['default_model'] = provider_config['models'][0] # 默认模型
    client_init_config['default_parameters'] = provider_config.get('default_parameters', {})
    
    try:
        return ClientClass(client_init_config)
    except Exception as e:
        log_error(f"初始化LLM客户端 '{provider_config['name']}' 时失败: {e}", exc_info=True)
        return None

def stream_llm_response(client: BaseLLMClient, model: str, messages: List[Dict[str, Any]], params: Dict[str, Any]):
    """处理LLM的流式响应并打印到控制台。"""
    full_response = ""
    animation_stopped = False
    
    try:
        animation_msg = f"{TermColors.LIGHT_BLUE}AI 正在思考...{TermColors.RESET}"
        start_loading_animation(message=animation_msg, animation_style_key='moon')

        response_generator = client.chat_completion(
            messages=messages,
            model=model,
            stream=True,
            **params
        )

        first_chunk = True
        for chunk in response_generator:
            if first_chunk:
                stop_loading_animation()
                animation_stopped = True
                print(f"{TermColors.CYAN}AI:{TermColors.RESET} ", end="", flush=True)
                first_chunk = False
            
            sys.stdout.write(f"{TermColors.CYAN}{chunk}{TermColors.RESET}")
            sys.stdout.flush()
            full_response += chunk
        
        if not first_chunk:
            print() # 换行

    except Exception as e:
        log_error(f"与LLM通信时发生错误: {e}", exc_info=True)
        return None
    finally:
        if not animation_stopped:
            stop_loading_animation(success=bool(full_response), final_message="与API通信中断" if not full_response else None)
    
    return full_response

def main():
    """程序主入口点。"""
    load_dotenv()
    initialize_logger(app_name="NeoChat-DirectChat")

    # 1. 加载 chat_config.yaml
    try:
        with open("chat_config.yaml", 'r', encoding='utf-8') as f:
            chat_config = yaml.safe_load(f)
        providers = chat_config.get("providers", [])
        if not providers:
            raise ValueError("chat_config.yaml 中未找到任何 'providers'。")
    except (FileNotFoundError, yaml.YAMLError, ValueError) as e:
        log_error(f"加载或解析 chat_config.yaml 失败: {e}")
        input("按回车键退出...")
        return

    # 2. 交互式选择提供商和模型
    provider_names = [p['name'] for p in providers]
    selected_provider_name = select_from_list("请选择一个模型服务提供商:", provider_names)
    if not selected_provider_name:
        log_info_color("操作已取消。", TermColors.YELLOW)
        return
        
    selected_provider_config = next(p for p in providers if p['name'] == selected_provider_name)
    
    model_names = selected_provider_config['models']
    selected_model = select_from_list(f"请为 '{selected_provider_name}' 选择一个模型:", model_names)
    if not selected_model:
        log_info_color("操作已取消。", TermColors.YELLOW)
        return

    # 3. 初始化选择的LLM客户端
    llm_client = initialize_llm_client(selected_provider_config)
    if not llm_client:
        input("按回车键退出...")
        return
        
    log_info_color(f"模型已选定: {selected_provider_name} - {selected_model}", TermColors.GREEN)

    # 4. 进入聊天循环
    chat_system_prompt = os.getenv("CHAT_SYSTEM_PROMPT", "你是一个AI助手。")
    messages = [{"role": "system", "content": chat_system_prompt}]

    print_formatted_text(FormattedText([
        (PromptToolkitColors.YELLOW, "说明: "),
        ("", "输入你的消息后按 "),
        (PromptToolkitColors.BOLD, "Alt+Enter"),
        ("", " 或 "),
        (PromptToolkitColors.BOLD, "Esc -> Enter"),
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
                FormattedText([
                    (PromptToolkitColors.YELLOW, '> 你: ')
                ]),
                multiline=True,
                prompt_continuation='  '
            )

            if not user_input.strip():
                continue

            if user_input.lower() in ["/exit", "quit"]:
                log_info_color("再见！", TermColors.MAGENTA)
                break

            messages.append({"role": "user", "content": user_input})
            
            response_text = stream_llm_response(
                client=llm_client,
                model=selected_model,
                messages=messages,
                params=selected_provider_config.get('default_parameters', {})
            )

            if response_text:
                messages.append({"role": "assistant", "content": response_text})
            else:
                log_error("未能从AI获取回应，请检查网络或API配置。")
                messages.pop() # 移除失败的用户输入

    except (KeyboardInterrupt, EOFError):
        print("\n")
        log_info_color("聊天被中断。再见！", TermColors.MAGENTA)

if __name__ == "__main__":
    main()