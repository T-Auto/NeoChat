import http.client
import json
import os
import base64
import sys
import mimetypes

# Attempt to import logger and PyMuPDF (fitz)
try:
    import logger
except ImportError:
    print("错误：找不到 logger.py。请确保它与 Gemini.py 在同一目录中。", file=sys.stderr)
    sys.exit(1)

try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False

# --- Configuration ---
API_HOST = "kfcv50.link"  # Host from the URL
API_PATH = "/v1/chat/completions"
# User can change this to "gemini-2.5-pro" or other compatible models
MODEL_NAME = "gemini-2.5-pro-exp-03-25"
SEND_DIRECTORY = "send"
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')
PDF_EXTENSIONS = ('.pdf',)

# Initialize logger
log = logger.initialize_logger(app_name="GeminiCLI", config_debug_mode=True, show_timestamp=True)

if not PYMUPDF_AVAILABLE:
    logger.log_warning("PyMuPDF (fitz) 库未安装。PDF 文件将无法提取文本内容。如需此功能，请运行: pip install PyMuPDF")

def get_api_key():
    """Retrieves the API key from environment variables."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logger.log_error("错误：未设置 GEMINI_API_KEY 环境变量。")
        logger.log_info("请设置 GEMINI_API_KEY 环境变量后重试。例如：export GEMINI_API_KEY='your_api_key'")
        sys.exit(1)
    return api_key

def create_send_directory_if_not_exists():
    """Creates the 'send' directory if it doesn't exist."""
    if not os.path.exists(SEND_DIRECTORY):
        try:
            os.makedirs(SEND_DIRECTORY)
            logger.log_info(f"已创建 '{SEND_DIRECTORY}/' 目录。请将待发送的图片/PDF放入此目录。")
        except OSError as e:
            logger.log_error(f"创建 '{SEND_DIRECTORY}/' 目录失败: {e}")
            sys.exit(1)
    else:
        if not os.path.isdir(SEND_DIRECTORY):
            logger.log_error(f"错误: '{SEND_DIRECTORY}' 已存在但不是一个目录。")
            sys.exit(1)


def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file if PyMuPDF is available."""
    if not PYMUPDF_AVAILABLE:
        logger.log_warning(f"PyMuPDF 不可用，无法从 '{os.path.basename(pdf_path)}' 提取文本。将仅发送文件名。")
        return f"[无法提取 '{os.path.basename(pdf_path)}' 的文本内容，PyMuPDF未安装]"
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        logger.log_debug(f"成功从 '{os.path.basename(pdf_path)}' 提取文本。")
        return text
    except Exception as e:
        logger.log_error(f"从 '{os.path.basename(pdf_path)}' 提取文本失败: {e}")
        return f"[提取 '{os.path.basename(pdf_path)}' 文本时出错: {e}]"

def encode_image_to_base64(image_path):
    """Encodes an image file to a base64 string and determines its MIME type."""
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            # Fallback for common types if mimetypes fails (e.g., on some minimal systems)
            ext = os.path.splitext(image_path)[1].lower()
            if ext == ".jpg" or ext == ".jpeg":
                mime_type = "image/jpeg"
            elif ext == ".png":
                mime_type = "image/png"
            else:
                mime_type = "application/octet-stream" # Generic fallback
        logger.log_debug(f"成功编码图片 '{os.path.basename(image_path)}' (MIME: {mime_type})。")
        return encoded_string, mime_type
    except Exception as e:
        logger.log_error(f"编码图片 '{os.path.basename(image_path)}' 失败: {e}")
        return None, None

def scan_send_directory_and_prepare_parts():
    """Scans the 'send' directory for images and PDFs and prepares content parts."""
    content_parts = []
    if not os.path.isdir(SEND_DIRECTORY):
        logger.log_warning(f"'{SEND_DIRECTORY}/' 目录不存在或不是一个目录，跳过文件扫描。")
        return content_parts

    processed_files = []
    logger.log_info(f"扫描 '{SEND_DIRECTORY}/' 目录中的文件...")
    for filename in os.listdir(SEND_DIRECTORY):
        file_path = os.path.join(SEND_DIRECTORY, filename)
        if not os.path.isfile(file_path):
            continue

        _, ext = os.path.splitext(filename.lower())

        if ext in IMAGE_EXTENSIONS:
            base64_image, mime_type = encode_image_to_base64(file_path)
            if base64_image and mime_type:
                content_parts.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{base64_image}"
                    }
                })
                processed_files.append(filename)
        elif ext in PDF_EXTENSIONS:
            pdf_text = extract_text_from_pdf(file_path)
            content_parts.append({
                "type": "text",
                "text": f"[来自PDF '{filename}' 的内容]:\\n{pdf_text}"
            })
            processed_files.append(filename)

    if processed_files:
        logger.log_info_color(f"已准备附加以下文件: {', '.join(processed_files)}", logger.TermColors.CYAN)
    else:
        logger.log_info(f"在 '{SEND_DIRECTORY}/' 目录中未找到可附加的图片或PDF文件。")
        
    return content_parts

def call_gemini_api(api_key, user_text_prompt):
    """Calls the Gemini API with the user prompt and any file contents."""
    logger.start_loading_animation(message="与Gemini通讯中", animation_style_key='spinner')

    # Always start with the user's text prompt
    message_content_parts = [{"type": "text", "text": user_text_prompt}]
    
    # Scan and add parts from 'send/' directory
    file_content_parts = scan_send_directory_and_prepare_parts()
    if file_content_parts:
        message_content_parts.extend(file_content_parts)

    payload_dict = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                # If only text, content is string. If multimodal, content is list of parts.
                # The example API format suggests "content" might need to be a string.
                # However, to support multimodal properly as per Gemini/OpenAI standards,
                # a list of parts is more appropriate if the endpoint supports it.
                # We will try with a list of parts if multiple parts exist.
                # If only one text part, it will be a string.
                "content": message_content_parts if len(message_content_parts) > 1 else message_content_parts[0]["text"]
            }
        ],
        "stream": True  # Enable streaming
    }
    
    # If the content ended up being a list, and the user's example strictly means string content,
    # this might need adjustment based on API behavior.
    # For now, this structure is common for multimodal.
    if isinstance(payload_dict["messages"][0]["content"], list):
        logger.log_debug("构建的多模态消息内容，包含多个部分。")
    else:
        logger.log_debug("构建的单文本消息内容。")

    payload_json = json.dumps(payload_dict)
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    conn = None
    try:
        conn = http.client.HTTPSConnection(API_HOST)
        logger.log_debug(f"发送请求到: https://{API_HOST}{API_PATH}")
        logger.log_debug(f"请求体: {payload_json}") # Be careful logging full payload if sensitive
        conn.request("POST", API_PATH, payload_json, headers)
        res = conn.getresponse()
        status = res.status
        reason = res.reason
        data = res.read()
        logger.log_debug(f"API响应状态: {status} {reason}")

        if status == 200:
            logger.stop_loading_animation(success=True, final_message=None) # Stop animation before streaming
            logger.log_info_color("来自Gemini的回复 (流式):", logger.TermColors.BLUE)
            
            full_response_content = ""
            try:
                while True:
                    line = res.readline()
                    if not line:
                        break  # End of stream

                    line_str = line.decode("utf-8").strip()
                    logger.log_debug(f"Stream raw line: {line_str}")

                    if line_str.startswith("data:"):
                        json_data_str = line_str[len("data:"):].strip()
                        if json_data_str == "[DONE]":
                            logger.log_debug("Stream finished with [DONE]")
                            break
                        
                        try:
                            response_chunk_json = json.loads(json_data_str)
                            chunk_content = ""
                            if "choices" in response_chunk_json and \
                               len(response_chunk_json["choices"]) > 0 and \
                               "delta" in response_chunk_json["choices"][0] and \
                               "content" in response_chunk_json["choices"][0]["delta"]:
                                chunk_content = response_chunk_json["choices"][0]["delta"]["content"]
                            
                            if chunk_content:
                                print(chunk_content, end="")
                                sys.stdout.flush()
                                full_response_content += chunk_content
                            # Handle other potential fields in delta if necessary (e.g., role)
                        except json.JSONDecodeError as je:
                            logger.log_warning(f"无法解析流中的JSON块: {json_data_str}, 错误: {je}")
                        except Exception as e_chunk:
                            logger.log_warning(f"处理流数据块时发生错误: {e_chunk}")
                
                print() # Ensure a final newline after streaming
                if full_response_content:
                    logger.log_debug(f"完整流式响应内容: {full_response_content}")
                else:
                    logger.log_debug("流式响应未包含可识别的内容。")

            except Exception as e_stream:
                logger.log_error(f"读取流式响应时出错: {e_stream}", exc_info=True)
                # Ensure newline if error occurs mid-stream printing
                print()

        else: # Non-200 status
            logger.stop_loading_animation(success=False, final_message=f"API请求失败: {status} {reason}")
            error_data = res.read().decode('utf-8', errors='replace')
            logger.log_error_color(f"服务器响应: {error_data}", logger.TermColors.RED)
            # Attempt to parse error if JSON
            try:
                error_json = json.loads(error_data)
                if "error" in error_json:
                    err_msg = error_json["error"].get("message", "未知API错误")
                    code = error_json["error"].get("code", "N/A")
                    logger.log_error(f"API返回详细错误: {err_msg} (代码: {code})")
            except json.JSONDecodeError:
                pass # Already logged the raw error_data

    except http.client.HTTPException as e:
        logger.stop_loading_animation(success=False, final_message="HTTP通讯错误")
        logger.log_error(f"HTTP客户端错误: {e}")
    except ConnectionRefusedError:
        logger.stop_loading_animation(success=False, final_message="连接被拒绝")
        logger.log_error(f"连接到 {API_HOST} 被拒绝。请检查网络连接和API主机名。")
    except Exception as e:
        logger.stop_loading_animation(success=False, final_message="发生意外错误")
        logger.log_error(f"调用API时发生意外错误: {e}", exc_info=True)
    finally:
        if conn:
            conn.close()

def main():
    """Main function to run the Gemini CLI."""
    logger.log_info_color(f"欢迎使用 Gemini 对话程序 (模型: {MODEL_NAME})", logger.TermColors.MAGENTA)
    logger.log_info(f"API 端点: https://{API_HOST}{API_PATH}")
    logger.log_info(f"输入 'exit', 'quit' 或按 Ctrl+C 退出程序。")
    logger.log_info(f"输入内容后，连续按两次 Enter 键 (即输入一个空行) 来结束多行输入并发送。")
    logger.log_info(f"每次发送消息前，程序会自动扫描 '{SEND_DIRECTORY}/' 目录中的图片和PDF文件。")
    
    api_key = get_api_key()
    create_send_directory_if_not_exists()

    try:
        while True:
            print("-" * 50)
            logger.log_info_color("请输入您的消息 (连续按两次 Enter 结束输入):", logger.TermColors.CYAN)
            
            lines = []
            while True:
                try:
                    line = input(f"{logger.TermColors.GREEN}> {logger.TermColors.RESET}" if not lines else f"{logger.TermColors.GREEN}. {logger.TermColors.RESET}")
                    if not line and lines and not lines[-1]:
                        if lines and not lines[-1]:
                            lines.pop()
                        break
                    lines.append(line)
                    if len(lines) == 1 and line.lower() in ['exit', 'quit']:
                        break
                except EOFError:
                    logger.log_debug("捕获到 EOFError，视为输入结束。")
                    if lines and not lines[-1]:
                        lines.pop()
                    break

            user_input = "\n".join(lines).strip()

            if user_input.lower() in ['exit', 'quit']:
                logger.log_info("程序退出。")
                break
            
            if not user_input:
                logger.log_warning("输入不能为空，请重新输入。")
                continue

            call_gemini_api(api_key, user_input)

    except KeyboardInterrupt:
        logger.log_info_color("\\n再见！", logger.TermColors.YELLOW)
    except Exception as e:
        logger.log_error(f"主循环发生未捕获错误: {e}", exc_info=True)
    finally:
        # Ensure animation is stopped if exited abruptly, though logger's animation is daemon.
        if logger._animation_thread and logger._animation_thread.is_alive():
             logger.stop_loading_animation(final_message="程序终止")
        sys.exit(0)

if __name__ == "__main__":
    main()