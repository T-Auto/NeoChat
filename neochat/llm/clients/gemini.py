# neochat/llm/clients/gemini.py
import google.generativeai as genai
from typing import List, Dict, Generator, Any

from .base import BaseLLMClient
from neochat.platform.logging import log_debug, log_warning, log_error_color, log_error

class GeminiClient(BaseLLMClient):
    """
    用于与 Google Gemini API 交互的客户端。
    """
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config.get("api_key")
        if not self.api_key:
            log_error_color("致命错误: Gemini API Key 未配置。")
            raise ValueError("Gemini API Key is missing.")
        
        try:
            genai.configure(api_key=self.api_key)
        except Exception as e:
            log_error_color(f"配置 Google Generative AI SDK 失败: {e}")
            raise

    def _convert_messages_to_gemini_format(self, messages: List[Dict[str, Any]]) -> (str, List[Dict[str, Any]]):
        """
        将 OpenAI 格式的消息列表转换为 Gemini 格式。
        Gemini 需要 system_instruction 和 contents 是分开的，且角色是 'user' 和 'model'。
        它还不允许连续的相同角色消息。
        """
        system_instruction = ""
        gemini_contents = []
        
        # 1. 提取 system prompt
        processed_messages = []
        for msg in messages:
            if msg.get("role") == "system":
                system_instruction += msg.get("content", "") + "\n"
            else:
                processed_messages.append(msg)
        
        # 2. 转换并合并消息
        if not processed_messages:
            return system_instruction.strip(), []

        for msg in processed_messages:
            role = msg.get("role")
            content = msg.get("content", "")
            
            # 角色映射: assistant -> model
            gemini_role = "model" if role == "assistant" else "user"
            
            # 如果当前角色与上一条消息角色相同，则合并内容
            if gemini_contents and gemini_contents[-1]["role"] == gemini_role:
                gemini_contents[-1]["parts"][0]["text"] += f"\n{content}"
            else:
                gemini_contents.append({
                    "role": gemini_role,
                    "parts": [{"text": content}]
                })
                
        return system_instruction.strip(), gemini_contents

    def chat_completion(
        self,
        messages: List[Dict[str, Any]],
        model: str = None,
        stream: bool = True,
        **kwargs
    ) -> Generator[str, None, None]:
        
        target_model = model or self.default_model
        log_debug(f"准备发起 Gemini API 请求。Model: {target_model}")

        system_instruction, gemini_contents = self._convert_messages_to_gemini_format(messages)
        
        # 将 config.yaml 中的通用参数映射到 Gemini 的特定参数
        generation_config = vars(self.default_parameters).copy()
        generation_config.update(kwargs)
        if 'max_tokens' in generation_config:
            generation_config['max_output_tokens'] = generation_config.pop('max_tokens')
        
        try:
            model_instance = genai.GenerativeModel(
                model_name=target_model,
                system_instruction=system_instruction if system_instruction else None
            )
            
            response_generator = model_instance.generate_content(
                gemini_contents,
                stream=stream,
                generation_config=generation_config
            )

            if stream:
                for chunk in response_generator:
                    # 检查是否有内容，并处理可能的安全设置导致的空响应
                    if chunk.parts:
                        yield chunk.text
            else:
                # 非流式响应
                if response_generator.parts:
                    yield response_generator.text
                else:
                    log_warning("Gemini API 返回了空响应，可能由安全设置触发。")
                    yield ""

        except Exception as e:
            log_error_color(f"\n与 Gemini API 通信时发生错误: {e}", exc_info=True)
            # 尝试解析更详细的错误信息
            if hasattr(e, 'message'):
                log_error_color(f"错误详情: {e.message}")
            return