import os
from dotenv import load_dotenv
load_dotenv()
# config.py

# --- 必填项 ---
# 在这里填入你的DeepSeek API Key
API_KEY = os.getenv("API_KEY")

# --- 模型配置 ---
# 使用的模型名称，例如 'deepseek-chat' 或 'deepseek-coder'
MODEL_NAME = "deepseek-chat"
API_URL = "https://api.deepseek.com/chat/completions"
MAX_TOKENS = 2048
TEMPERATURE = 0.7
API_TIMEOUT_SECONDS = 120

# --- 应用配置 ---
# DEBUG模式会输出海量的灰色日志，用于调试
DEBUG_MODE = False
AI_NAME = "NeoChat"

# --- 存档与剧本路径 ---
# 剧本包存放的根目录
STORY_PACKS_BASE_PATH = "./story_packs"
# 角色人设存放的根目录
CHARACTERS_BASE_PATH = "./characters"
# 游戏存档存放的根目录
SAVES_BASE_PATH = "./saves"