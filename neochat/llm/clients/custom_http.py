# neochat/llm/clients/custom_http.py
import requests
import json
import re
from typing import List, Dict, Generator, Any
from jsonpath_ng import parse

from .base import BaseLLMClient
from neochat.platform.configuration import config as app_config
from neochat.platform.logging import log_debug, log_warning, log_error_color, log_error

class CustomHttpClient(BaseLLMClient):
    """
    一个高度可配置的客户端，用于与任何自定义的、基于HTTP的LLM API进行交互。
    所有配置均在 config.yaml 中定义。
    """
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        # 从配置中加载所有自定义设置
        self.url = config.get("url")
        self.http_method = config.get("method", "POST").upper()
        self.headers_template = config.get("headers_template", {})
        self.payload_template = config.get("payload_template", {})
        self.stream_config = config.get("streaming", {})
        
        if not self.url or not self.payload_template:
            raise ValueError("CustomHttpClient 需要在配置中定义 'url' 和 'payload_template'。")

    def _render_template(self, template: Any, context: Dict[str, Any]) -> Any:
        """递归地渲染模板中的占位符，如 {api_key} 或 {messages_json}。"""
        if isinstance(template, dict):
            return {k: self._render_template(v, context) for k, v in template.items()}
        if isinstance(template, list):
            return [self._render_template(i, context) for i in template]
        if isinstance(template, str):
            for key, value in context.items():
                placeholder = f"{{{key}}}"
                # 对JSON字符串进行特殊处理，避免转义问题
                if placeholder in template and isinstance(value, str) and key.endswith('_json'):
                     # 直接替换，不加引号
                    return template.replace(placeholder, value)
                elif placeholder in template:
                    template = template.replace(placeholder, str(value))
            return template
        return template

    def chat_completion(
        self,
        messages: List[Dict[str, Any]],
        model: str = None,
        stream: bool = True,
        **kwargs
    ) -> Generator[str, None, None]:
        
        # 1. 准备渲染上下文
        context = {
            "api_key": self.config.get("api_key", ""),
            "model": model or self.default_model,
            "messages": messages,
            "messages_json": json.dumps(messages, ensure_ascii=False)
        }
        final_params = vars(self.default_parameters).copy()
        final_params.update(kwargs)
        context.update(final_params)

        # 2. 渲染请求头和请求体
        headers = self._render_template(self.headers_template, context)
        payload = self._render_template(self.payload_template, context)
        
        log_debug(f"准备发起 Custom HTTP 请求。URL: {self.url}, Method: {self.http_method}")
        if app_config.debug.mode:
            log_debug("--- Custom HTTP Request ---")
            log_debug(f"Headers: {json.dumps(headers, indent=2)}")
            log_debug(f"Payload: {json.dumps(payload, indent=2, ensure_ascii=False)}")
            log_debug("--------------------------")

        try:
            response = requests.request(
                method=self.http_method,
                url=self.url,
                headers=headers,
                json=payload,
                stream=stream,
                timeout=app_config.llm.timeout_seconds
            )
            response.raise_for_status()

            if stream and self.stream_config.get('enabled'):
                # 处理流式响应
                line_prefix = self.stream_config.get('line_prefix', 'data: ')
                json_path = self.stream_config.get('json_path_for_content')
                if not json_path:
                    raise ValueError("流式模式下必须配置 'json_path_for_content'。")
                
                jsonpath_expr = parse(json_path)

                for line in response.iter_lines():
                    if not line: continue
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith(line_prefix):
                        json_str = decoded_line[len(line_prefix):]
                        if not json_str.strip(): continue
                        try:
                            data = json.loads(json_str)
                            matches = jsonpath_expr.find(data)
                            if matches:
                                yield str(matches[0].value)
                        except (json.JSONDecodeError, IndexError):
                            log_warning(f"Custom Stream: 解码或解析JSON路径失败: {json_str}")
            else:
                # 处理非流式响应
                json_path = self.config.get('response_json_path_for_content')
                if not json_path:
                    raise ValueError("非流式模式下必须配置 'response_json_path_for_content'。")
                
                jsonpath_expr = parse(json_path)
                data = response.json()
                matches = jsonpath_expr.find(data)
                if matches:
                    yield str(matches[0].value)

        except requests.exceptions.RequestException as e:
            log_error_color(f"\nCustom API 请求失败: {e}", exc_info=True)
        except Exception as e:
            log_error_color(f"\n处理 Custom API 响应时发生未知错误: {e}", exc_info=True)