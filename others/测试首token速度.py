import os
import time
import openai
from dotenv import load_dotenv

# --- 1. 配置 ---

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量中获取 API 密钥
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("未找到 DEEPSEEK_API_KEY，请检查你的 .env 文件")

# 初始化 DeepSeek 客户端
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/v1"
)

# 定义要测试的模型
MODEL_NAME = "deepseek-chat"

# --- 2. 核心测试函数 ---

def get_first_token_latency(messages: list) -> (float, str):
    """
    发送请求并测量首个 token 的延迟。
    使用 stream=True 来实现。
    返回 (延迟时间, 完整的AI回复)
    """
    try:
        start_time = time.time()
        
        # 发起流式请求
        response_stream = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            stream=True
        )
        
        first_token_time = None
        full_response_content = ""
        
        # 迭代接收数据块
        for chunk in response_stream:
            # 首次接收到数据块时，计算延迟
            if first_token_time is None:
                first_token_time = time.time()
            
            # 收集完整的回复内容
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                full_response_content += chunk.choices[0].delta.content
        
        if first_token_time:
            latency = first_token_time - start_time
            return latency, full_response_content
        else:
            # 如果没有收到任何 token
            return -1.0, "错误：未收到任何响应"
            
    except Exception as e:
        print(f"发生错误: {e}")
        return -1.0, str(e)

# --- 3. 生成长文本的辅助函数 ---

def generate_long_text(base_text, repeat=5):
    """生成更长的文本以增加token数量"""
    return " ".join([base_text] * repeat)

# --- 4. 三个测试场景 ---

def test_normal_conversation():
    """
    场景一：正常的连续对话，上下文不断增长。
    预期：由于缓存，后续请求的延迟可能降低。
    """
    print("--- 场景一：正常连续对话测试 ---")
    
    # 创建更长的系统提示
    long_system_prompt = generate_long_text(
        "你是一个乐于助人的AI助手，专门为用户提供详细、准确的信息解答。"
        "你的知识涵盖科学技术、文化艺术、历史地理等多个领域。请用中文回答用户的问题，"
        "并尽可能提供全面、深入的解析。如果遇到不确定的问题，请诚实地告知用户。"
        "你的目标是成为用户最信赖的知识伙伴。", 3
    )
    
    # 初始的 system prompt 和对话历史
    messages = [
        {"role": "system", "content": long_system_prompt},
    ]
    
    # 创建更长的用户提示
    user_prompts = [
        generate_long_text("你好，请详细介绍你的功能、能力和技术背景。你基于什么模型构建？你的训练数据包含哪些内容？", 3),
        generate_long_text("你提到的模型有什么特别的技术特点？它在处理中文和多语言任务方面有什么优势？请详细说明。", 3),
        generate_long_text("这个模型在长上下文处理、推理能力和创造性任务方面表现如何？能否举例说明？", 3),
        generate_long_text("总结一下你的主要能力、技术优势和应用场景。对于开发者来说，你有什么特别的价值？", 3)
    ]
    
    for i, prompt in enumerate(user_prompts):
        print(f"\n第 {i+1} 次请求...")
        print(f"  当前对话历史长度: {len(str(messages))} 字符")
        
        # 1. 将用户的新问题添加到对话历史
        messages.append({"role": "user", "content": prompt})
        print(f"  [User]: {prompt[:100]}...")  # 只显示前100字符
        
        # 2. 测量延迟并获取回复
        latency, ai_response = get_first_token_latency(messages)
        
        if latency != -1.0:
            print(f"  [AI]: {ai_response[:100]}...")  # 打印部分回复内容
            print(f"  >> 首Token延迟: {latency:.4f} 秒")
            
            # 3. 将AI的回复也添加到对话历史，为下一次请求做准备
            messages.append({"role": "assistant", "content": ai_response})
            print(f"  更新后对话历史长度: {len(str(messages))} 字符")
        
        time.sleep(2)  # 增加等待时间，避免请求过于频繁

def test_changing_system_prompt():
    """
    场景二：每次请求都更新 System Prompt。
    预期：由于 System Prompt 改变，缓存可能失效，延迟较高且稳定。
    """
    print("--- 场景二：每次更新 System Prompt 测试 ---")
    
    # 创建更长的系统提示
    system_prompts = [
        generate_long_text("你是一位知识渊博的历史学家，专注于中国古代史和世界文明发展史。"
                         "请用专业且易于理解的方式回答历史相关问题，提供准确的历史背景、时间线和重要人物信息。", 3),
        generate_long_text("你是一位充满激情的诗人，擅长中国古典诗词和现代诗歌创作。"
                         "请用富有韵律和美感的语言回答，尽可能以诗歌形式表达，展现语言的魅力。", 3),
        generate_long_text("你是一位严谨的计算机科学家，专注于人工智能、机器学习和算法设计。"
                         "请用专业术语和准确的技术描述回答问题，提供代码示例和技术实现细节。", 3),
        generate_long_text("你是一位富有想象力的科幻小说作家，擅长构建未来世界和科幻设定。"
                         "请用创意十足的方式回答问题，编织引人入胜的科幻叙事和世界观构建。", 3)
    ]
    
    # 创建更长的用户提示
    user_prompt = generate_long_text(
        "请从你的专业角度详细解释'光'是什么？包括它的物理特性、在不同文化中的象征意义、"
        "以及它在你的专业领域中的特殊重要性。请提供全面的解析。", 3
    )
    
    for i, sys_prompt in enumerate(system_prompts):
        print(f"\n第 {i+1} 次请求...")
        
        # 每次都构建全新的 messages 列表
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ]
        print(f"  请求消息长度: {len(str(messages))} 字符")
        print(f"  [System]: {sys_prompt[:100]}...")
        print(f"  [User]: {user_prompt[:100]}...")
        
        latency, ai_response = get_first_token_latency(messages)
        
        if latency != -1.0:
            print(f"  [AI]: {ai_response[:100]}...")
            print(f"  >> 首Token延迟: {latency:.4f} 秒")
            
        time.sleep(2)

def test_rag_simulation():
    """
    场景三：模拟 RAG，System Prompt 不变，但在用户输入前插入变化的上下文。
    预期：由于插入了新内容，缓存可能部分失效或完全失效，延迟可能较高。
    """
    print("--- 场景三：模拟 RAG 插入变动知识测试 ---")
    
    # 创建更长的固定 system prompt
    long_system_prompt = generate_long_text(
        "你是一个专业的问答机器人，请根据我提供的背景知识来回答问题。"
        "你需要仔细分析提供的背景信息，并基于这些信息给出准确、全面的回答。"
        "如果背景信息不足以回答问题，请诚实地告知用户，不要编造信息。", 3
    )
    
    # 固定的 system prompt 和初始对话历史
    messages = [
        {"role": "system", "content": long_system_prompt},
    ]
    
    # 创建更长的 RAG 上下文
    rag_contexts = [
        generate_long_text("背景知识：DeepSeek-V2 是由深度求索公司开发的第二代MoE模型。"
                         "该模型采用混合专家架构，总参数量达到236B，但每次推理仅激活21B参数，"
                         "显著降低了推理成本和能耗。模型支持多种编程语言和自然语言任务。", 3),
        generate_long_text("背景知识：DeepSeek-V2 支持长达128k的上下文窗口，能够处理长文档和复杂对话。"
                         "在API定价上，它具有很强的竞争力，缓存命中情况下价格低至0.1元/百万tokens。"
                         "模型在多项中英文基准测试中表现优异。", 3),
        generate_long_text("背景知识：该模型在代码生成、数学推理和逻辑推理任务上表现突出。"
                         "它采用了先进的训练方法和高质量的数据集，涵盖科技、学术、文学等多个领域。"
                         "模型还具备强大的指令遵循能力和安全性保障。", 3),
        generate_long_text("背景知识：DeepSeek-V2 提供了灵活的API接口和丰富的开发工具。"
                         "开发者可以轻松集成到各种应用中，包括聊天机器人、内容生成、知识问答等场景。"
                         "官方提供了详细的文档和示例代码支持开发者使用。", 3)
    ]
    
    # 创建更长的用户问题
    user_question = generate_long_text(
        "根据以上提供的背景信息，请详细总结一下这个模型的主要特点、技术优势和应用场景。"
        "对于开发者来说，使用这个模型有什么特别的价值和注意事项？请提供全面的分析。", 3
    )
    
    for i, context in enumerate(rag_contexts):
        print(f"\n第 {i+1} 次请求...")
        
        # 1. 复制当前对话历史，避免污染原始 history
        current_request_messages = messages.copy()
        
        # 2. 模拟 RAG 插入：在最后的用户问题前插入变化的上下文
        rag_message = {"role": "user", "content": context}
        user_message = {"role": "user", "content": user_question}
        
        current_request_messages.append(rag_message)
        current_request_messages.append(user_message)
        
        print(f"  请求消息长度: {len(str(current_request_messages))} 字符")
        print(f"  [RAG Context]: {context[:100]}...")
        print(f"  [User]: {user_question[:100]}...")
        
        # 3. 测量延迟并获取回复
        latency, ai_response = get_first_token_latency(current_request_messages)
        
        if latency != -1.0:
            print(f"  [AI]: {ai_response[:100]}...")
            print(f"  >> 首Token延迟: {latency:.4f} 秒")
            
            # 4. 将本次交互（包括RAG上下文、问题、AI回答）完整地加入到主对话历史中
            messages.append(rag_message)
            messages.append(user_message)
            messages.append({"role": "assistant", "content": ai_response})
            print(f"  更新后对话历史长度: {len(str(messages))} 字符")
            
        time.sleep(2)

# --- 5. 运行所有测试 ---

if __name__ == "__main__":
    print(f"开始测试 DeepSeek API ({MODEL_NAME}) 首Token延迟...\n")
    
    test_normal_conversation()
    print("\n" + "="*60 + "\n")
    test_changing_system_prompt()
    print("\n" + "="*60 + "\n")
    test_rag_simulation()
    print("\n测试完成。")