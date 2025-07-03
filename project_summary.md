# NeoChat 项目概览

## 项目结构
```text
NeoChat/
├── characters/
│   └── Roxy.yaml
├── memory-bank/
│   ├── activeContext.md
│   ├── productContext.md
│   ├── progress.md
│   ├── projectbrief.md
│   ├── systemPatterns.md
│   └── techContext.md
├── run_logs/
│   ├── ... (1 more .log files)
│   ├── AppLogger_2025-07-03_22-33-52.log
│   ├── AppLogger_2025-07-03_22-36-52.log
│   └── AppLogger_2025-07-03_22-42-44.log
├── saves/
│   ├── save_20250703_223358/
│   │   ├── character/
│   │   │   └── Roxy.yaml
│   │   ├── save/
│   │   │   ├── gamestate.yaml
│   │   │   ├── 对话记录.yaml
│   │   │   └── 游戏进度.yaml
│   │   ├── story/
│   │   │   ├── 00_Labyrinth_Entrance.yaml
│   │   │   ├── 01_Explore_Corridor.yaml
│   │   │   ├── 02_Event_Treasure.yaml
│   │   │   ├── 03A_Player_Fights.yaml
│   │   │   ├── 03B_Roxy_Fights.yaml
│   │   │   ├── 03_Event_Monster.yaml
│   │   │   ├── 04A_Trap_Dodged.yaml
│   │   │   ├── 04B_Trap_Hit.yaml
│   │   │   ├── 04_Event_Trap.yaml
│   │   │   └── 99_Exit_Labyrinth.yaml
│   │   ├── 全局剧情配置.yaml
│   │   └── 剧情介绍.md
│   ├── save_20250703_223658/
│   │   ├── character/
│   │   │   └── Roxy.yaml
│   │   ├── save/
│   │   │   ├── gamestate.yaml
│   │   │   ├── 对话记录.yaml
│   │   │   └── 游戏进度.yaml
│   │   ├── story/
│   │   │   ├── 00_Labyrinth_Entrance.yaml
│   │   │   ├── 01_Explore_Corridor.yaml
│   │   │   ├── 02_Event_Treasure.yaml
│   │   │   ├── 03A_Player_Fights.yaml
│   │   │   ├── 03B_Roxy_Fights.yaml
│   │   │   ├── 03_Event_Monster.yaml
│   │   │   ├── 04A_Trap_Dodged.yaml
│   │   │   ├── 04B_Trap_Hit.yaml
│   │   │   ├── 04_Event_Trap.yaml
│   │   │   └── 99_Exit_Labyrinth.yaml
│   │   ├── 全局剧情配置.yaml
│   │   └── 剧情介绍.md
│   ├── save_20250703_224249/
│   │   ├── character/
│   │   │   └── Roxy.yaml
│   │   ├── save/
│   │   │   ├── gamestate.yaml
│   │   │   ├── 对话记录.yaml
│   │   │   └── 游戏进度.yaml
│   │   ├── story/
│   │   │   ├── 00_Labyrinth_Entrance.yaml
│   │   │   ├── 01_Explore_Corridor.yaml
│   │   │   ├── 02_Event_Treasure.yaml
│   │   │   ├── 03A_Player_Fights.yaml
│   │   │   ├── 03B_Roxy_Fights.yaml
│   │   │   ├── 03_Event_Monster.yaml
│   │   │   ├── 04A_Trap_Dodged.yaml
│   │   │   ├── 04B_Trap_Hit.yaml
│   │   │   ├── 04_Event_Trap.yaml
│   │   │   └── 99_Exit_Labyrinth.yaml
│   │   ├── 全局剧情配置.yaml
│   │   └── 剧情介绍.md
│   └── save_20250703_224652/
│       ├── character/
│       │   └── Roxy.yaml
│       ├── save/
│       │   ├── gamestate.yaml
│       │   ├── 对话记录.yaml
│       │   └── 游戏进度.yaml
│       ├── story/
│       │   ├── 00_Labyrinth_Entrance.yaml
│       │   ├── 01_Explore_Corridor.yaml
│       │   ├── 02_Event_Treasure.yaml
│       │   ├── 03A_Player_Fights.yaml
│       │   ├── 03B_Roxy_Fights.yaml
│       │   ├── 03_Event_Monster.yaml
│       │   ├── 04A_Trap_Dodged.yaml
│       │   ├── 04B_Trap_Hit.yaml
│       │   ├── 04_Event_Trap.yaml
│       │   └── 99_Exit_Labyrinth.yaml
│       ├── 全局剧情配置.yaml
│       └── 剧情介绍.md
├── story_packs/
│   └── roxy_labyrinth_adventure/
│       ├── save/
│       │   └── gamestate.yaml
│       ├── story/
│       │   ├── 00_Labyrinth_Entrance.yaml
│       │   ├── 01_Explore_Corridor.yaml
│       │   ├── 02_Event_Treasure.yaml
│       │   ├── 03A_Player_Fights.yaml
│       │   ├── 03B_Roxy_Fights.yaml
│       │   ├── 03_Event_Monster.yaml
│       │   ├── 04A_Trap_Dodged.yaml
│       │   ├── 04B_Trap_Hit.yaml
│       │   ├── 04_Event_Trap.yaml
│       │   └── 99_Exit_Labyrinth.yaml
│       ├── 全局剧情配置.yaml
│       └── 剧情介绍.md
├── .env
├── .env.example
├── .gitignore
├── README.md
├── config.py
├── game_engine.py
├── llm_interface.py
├── logger.py
├── main.py
├── start.bat
└── 用来导入剧情的.py
```

## 文件内容
### 文件: `README.md`

```markdown
# NeoChat
对实现AI永久记忆的探索。

## 简介

A simple and pure AI conversation platform based on command-line format / 返璞归真的，基于命令行形式的AI对话平台

## 特性

- 使用RAG向量库记忆系统，拥有数万条上下文的记忆，且不会耗费太多Token。

## 用法

- 依照requirements创建.venv虚拟环境
- 打开.env.example，修改系统提示词和你的apikey，并重命名为.env
- 对话历史储存在Dialogue_history中。
- chroma_db_store是RAG生成的历史对话向量库，删除后可自动创建。

## 更新

- **长线剧情系统**：支持使用类似galgame的剧情预设，直接兼容传统galgame的预设剧本和分歧选择，同时支持将一部分甚至全部的剧情**由AI驱动**。你将在剧情内日常的场合，停下来和主角自由的谈心，聊够了在继续剧情；你将不再局限于点击选项来选择剧情分歧，而是真正进入故事，说出你想说的话，影响主角做出重要选择，或者**劝说**主角真正的回心转意。
- **剧本杀/跑团模式**：支持使用类似剧本杀/跑团模式的剧情预设，由一个DM（主持人）来掌控剧情的发展，你将体验到诸如随着时间的推移获得越来越多的信息，判断“谁是凶手”，等类剧情游戏
- **随机事件生成器**：轻量化的剧情引导，如你和你的oc探索地下迷宫的过程中，由LLM生成你们下一个房间的见闻
- **大量的预设小游戏**：和你的一个甚至多个oc人设玩一把狼人杀，真心话大冒险，甚至恶魔轮盘赌等经典互动游戏
```

### 文件: `readme.md`

```markdown
# NeoChat
对实现AI永久记忆的探索。

## 简介

A simple and pure AI conversation platform based on command-line format / 返璞归真的，基于命令行形式的AI对话平台

## 特性

- 使用RAG向量库记忆系统，拥有数万条上下文的记忆，且不会耗费太多Token。

## 用法

- 依照requirements创建.venv虚拟环境
- 打开.env.example，修改系统提示词和你的apikey，并重命名为.env
- 对话历史储存在Dialogue_history中。
- chroma_db_store是RAG生成的历史对话向量库，删除后可自动创建。

## 更新

- **长线剧情系统**：支持使用类似galgame的剧情预设，直接兼容传统galgame的预设剧本和分歧选择，同时支持将一部分甚至全部的剧情**由AI驱动**。你将在剧情内日常的场合，停下来和主角自由的谈心，聊够了在继续剧情；你将不再局限于点击选项来选择剧情分歧，而是真正进入故事，说出你想说的话，影响主角做出重要选择，或者**劝说**主角真正的回心转意。
- **剧本杀/跑团模式**：支持使用类似剧本杀/跑团模式的剧情预设，由一个DM（主持人）来掌控剧情的发展，你将体验到诸如随着时间的推移获得越来越多的信息，判断“谁是凶手”，等类剧情游戏
- **随机事件生成器**：轻量化的剧情引导，如你和你的oc探索地下迷宫的过程中，由LLM生成你们下一个房间的见闻
- **大量的预设小游戏**：和你的一个甚至多个oc人设玩一把狼人杀，真心话大冒险，甚至恶魔轮盘赌等经典互动游戏
```

### 文件: `config.py`

```python
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
```

### 文件: `game_engine.py`

```python
# game_engine.py
import os
import shutil
import yaml
import re
import random
import uuid
from datetime import datetime

import config
from logger import log_debug, log_info, log_warning, log_error, log_info_color, TermColors
from llm_interface import chat_with_deepseek

class GameEngine:
    def __init__(self):
        self.save_path = None
        self.story_pack_path = None
        self.character_files = {} # role_id -> character_data
        
        # In-memory state
        self.game_state = {}
        self.progress = {}
        self.dialogue_history = []
        self.global_config = {}
        self.current_story_unit = None
        # --- 新增: 运行时上下文，用于存放不需存档的临时变量 ---
        self.runtime_context = {}

        self.is_running = False
        self.game_over = False

    def _format_string(self, text):
        """用 game_state 和 runtime_context 中的变量替换字符串中的 {placeholder}"""
        if not isinstance(text, str):
            return text
        
        # 正则表达式寻找 {variable_name}
        placeholders = re.findall(r'\{([a-zA-Z0-9_]+)\}', text)
        
        formatted_text = text
        for placeholder in placeholders:
            value = None
            # --- 核心修改：优先从运行时上下文查找 ---
            if placeholder in self.runtime_context:
                value = self.runtime_context[placeholder]
            # --- 其次从游戏状态查找 ---
            elif placeholder in self.game_state:
                value = self.game_state[placeholder]
            else:
                log_warning(f"格式化字符串时未在 game_state 或 runtime_context 中找到变量: {placeholder}")
                continue # 如果找不到，跳过替换

            # 确保替换值的类型正确
            if value is not None:
                formatted_text = formatted_text.replace(f'{{{placeholder}}}', str(value))

        return formatted_text

    def _evaluate_condition(self, condition_str):
        """安全地评估条件表达式"""
        formatted_condition = self._format_string(condition_str)
        log_debug(f"正在评估条件: `{condition_str}` -> `{formatted_condition}`")
        try:
            # 为安全起见，只允许简单的比较和逻辑运算
            # 更安全的做法是使用ast.literal_eval或一个专门的表达式求值库
            result = eval(formatted_condition, {"__builtins__": {}}, {})
            log_debug(f"条件评估结果: {result}")
            return result
        except Exception as e:
            log_error(f"评估条件时出错: '{formatted_condition}'. 错误: {e}")
            return False

    def _add_to_dialogue_history(self, event_type, **kwargs):
        log_entry = {
            "id": f"evt_{uuid.uuid4()}",
            "timestamp": datetime.now().isoformat(),
            "source_unit_id": self.progress.get('progress_pointer', {}).get('current_unit_id'),
            "source_event_index": self.progress.get('progress_pointer', {}).get('last_completed_event_index'),
            "type": event_type
        }

        # 核心修改逻辑：根据kwargs的结构决定数据格式
        # 如果kwargs只有一个'content'键，则将其提升到顶层
        if len(kwargs) == 1 and 'content' in kwargs:
            log_entry['content'] = kwargs['content']
        # 否则，将所有kwargs作为结构化数据放入'data'字段
        else:
            log_entry['data'] = kwargs

        self.dialogue_history.append(log_entry)
        log_debug(f"添加新对话记录: {log_entry}")

    def load_story_pack(self, story_pack_path, character_selections):
        """开始一个新游戏"""
        try:
            # 1. 创建存档文件夹
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.save_path = os.path.join(config.SAVES_BASE_PATH, f"save_{timestamp}")
            os.makedirs(os.path.join(self.save_path, "save"), exist_ok=True)
            
            # 2. 复制剧本和角色文件
            shutil.copytree(story_pack_path, self.save_path, dirs_exist_ok=True)
            char_dir_in_save = os.path.join(self.save_path, "character")
            os.makedirs(char_dir_in_save, exist_ok=True)
            for role_id, char_path in character_selections.items():
                shutil.copy(char_path, os.path.join(char_dir_in_save, f"{role_id}.yaml"))

            self.story_pack_path = self.save_path
            
            # 3. 加载全局配置和角色
            with open(os.path.join(self.story_pack_path, '全局剧情配置.yaml'), 'r', encoding='utf-8') as f:
                self.global_config = yaml.safe_load(f)
            
            self._load_character_files()

            # 4. 初始化 gamestate.yaml
            with open(os.path.join(self.story_pack_path, 'save', 'gamestate.yaml'), 'r', encoding='utf-8') as f:
                self.game_state = yaml.safe_load(f) or {}

            # 5. 初始化 游戏进度.yaml
            self.progress = {
                "save_name": "New Game",
                "story_pack_id": self.global_config.get('id', 'unknown'),
                "last_saved_timestamp": datetime.now().isoformat(),
                "progress_pointer": {
                    "current_unit_id": self.global_config['start_unit_id'],
                    "last_completed_event_index": -1
                },
                "runtime_state": "ExecutingEvents"
            }

            # 6. 初始化 对话记录.yaml
            self.dialogue_history = []
            
            self.is_running = True
            log_info(f"新游戏已创建，存档位于: {self.save_path}")
            
            # 进行一次初始保存，确保所有状态文件都已创建
            self.save_game("初始存档") 
            
            return True
        except Exception as e:
            log_error(f"创建新游戏失败: {e}")
            return False

    def _load_character_files(self):
        char_dir = os.path.join(self.story_pack_path, "character")
        self.character_files = {}
        for filename in os.listdir(char_dir):
            if filename.endswith(".yaml"):
                role_id = filename.split('.')[0]
                with open(os.path.join(char_dir, filename), 'r', encoding='utf-8') as f:
                    self.character_files[role_id] = yaml.safe_load(f)
                # 将角色名注入gamestate
                self.game_state[f'character_name_{role_id}'] = self.character_files[role_id]['name']

    def load_from_save(self, save_path):
        """从存档加载游戏"""
        try:
            self.save_path = save_path
            self.story_pack_path = save_path
            
            with open(os.path.join(self.save_path, 'save', 'gamestate.yaml'), 'r', encoding='utf-8') as f:
                self.game_state = yaml.safe_load(f)
            with open(os.path.join(self.save_path, 'save', '游戏进度.yaml'), 'r', encoding='utf-8') as f:
                self.progress = yaml.safe_load(f)
            with open(os.path.join(self.save_path, 'save', '对话记录.yaml'), 'r', encoding='utf-8') as f:
                self.dialogue_history = yaml.safe_load(f)
            with open(os.path.join(self.story_pack_path, '全局剧情配置.yaml'), 'r', encoding='utf-8') as f:
                self.global_config = yaml.safe_load(f)

            self._load_character_files()

            self.is_running = True
            log_info(f"成功从 {save_path} 加载存档。")
            return True
        except Exception as e:
            log_error(f"加载存档失败: {e}")
            return False

    def save_game(self, save_name=None):
        if not self.is_running:
            log_warning("游戏未运行，无法保存。")
            return
        
        try:
            if save_name:
                self.progress['save_name'] = save_name
            self.progress['last_saved_timestamp'] = datetime.now().isoformat()
            
            save_dir = os.path.join(self.save_path, 'save')
            with open(os.path.join(save_dir, 'gamestate.yaml'), 'w', encoding='utf-8') as f:
                yaml.dump(self.game_state, f, allow_unicode=True)
            with open(os.path.join(save_dir, '游戏进度.yaml'), 'w', encoding='utf-8') as f:
                yaml.dump(self.progress, f, allow_unicode=True)
            with open(os.path.join(save_dir, '对话记录.yaml'), 'w', encoding='utf-8') as f:
                yaml.dump(self.dialogue_history, f, allow_unicode=True)
            
            log_info_color(f"游戏已保存，存档名: '{self.progress['save_name']}'", TermColors.GREEN)
        except Exception as e:
            log_error(f"保存游戏失败: {e}")

    def run(self):
        """主游戏循环，执行事件直到需要玩家输入"""
        if not self.is_running or self.game_over:
            return

        while self.progress['runtime_state'] == 'ExecutingEvents' and not self.game_over:
            pointer = self.progress['progress_pointer']
            unit_id = pointer['current_unit_id']
            
            # 加载当前剧情单元
            unit_path = os.path.join(self.story_pack_path, 'story', f"{unit_id}.yaml")
            if not os.path.exists(unit_path):
                log_error(f"剧情单元文件未找到: {unit_path}")
                self.game_over = True
                break
            with open(unit_path, 'r', encoding='utf-8') as f:
                self.current_story_unit = yaml.safe_load(f)

            next_event_index = pointer['last_completed_event_index'] + 1
            events = self.current_story_unit.get('Events', [])
            
            if next_event_index >= len(events):
                # 事件执行完毕，处理EndCondition
                self._process_end_condition(self.current_story_unit.get('EndCondition'))
            else:
                # 执行下一个事件
                self._process_event(events[next_event_index])
                if self.progress['runtime_state'] == 'ExecutingEvents': # 确保事件没有改变状态
                     pointer['last_completed_event_index'] = next_event_index
        
        log_debug(f"引擎暂停，当前状态: {self.progress['runtime_state']}")


    def _process_event(self, event_data):
        log_debug(f"处理事件: {event_data}")

        # 处理条件
        if 'Condition' in event_data:
            if not self._evaluate_condition(event_data['Condition']):
                log_debug("条件不满足，跳过该事件块。")
                # 即使跳过，也算完成这个"条件事件"
                self.progress['progress_pointer']['last_completed_event_index'] += 1
                return
            # 如果条件满足，执行嵌套的Events
            for nested_event in event_data['Events']:
                 self._process_event(nested_event)
            # 完成后，更新主事件索引
            self.progress['progress_pointer']['last_completed_event_index'] += 1
            return

        event_key, event_content = list(event_data.items())[0]
        params = dict(param.strip().split(': ') for param in event_key.split(' | '))
        event_type = params['Type']
        
        # 格式化内容
        if isinstance(event_content, str):
            content = self._format_string(event_content)
        elif isinstance(event_content, dict):
            content = {k: self._format_string(v) for k, v in event_content.items()}
        else:
            content = event_content

        if event_type == 'Narration':
            if params.get('Mode') == 'Prompt':
                log_debug("生成 'Narration' prompt...")
                # 旁白/DM的通用系统提示
                narrator_prompt = "你是一个优秀的、沉浸式的故事讲述者（旁白）。请根据以下要求和对话历史，生成一段富有文采的旁白。直接输出旁白内容，不要包含任何额外解释。"
                messages = [
                    {"role": "system", "content": narrator_prompt},
                    {"role": "user", "content": f"这是你的生成要求：\n{content}"}
                ]
                # 可以选择性地加入最近的对话历史
                for record in self.dialogue_history[-5:]:
                    # 从记录中获取纯文本内容
                    content = record.get('content') or record.get('data', {}).get('content')
                    if not content:
                        continue

                    if record['type'] == 'Dialogue':
                        hist_char_id = record.get('data', {}).get('character_id')
                        if hist_char_id:
                            # 对于旁白生成，所有历史对话都作为用户输入
                            messages.insert(-1, {"role": "user", "content": content})
                    elif record['type'] == 'Player':
                        # 玩家发言也作为用户输入
                        messages.insert(-1, {"role": "user", "content": content})
                
                # --- 核心修改点 ---
                # chat_with_deepseek 内部已经处理了流式打印
                # 它返回的 generated_content 仅用于保存历史记录
                generated_content = chat_with_deepseek(messages, character_name="旁白", color_code=TermColors.GREY)
                
                if generated_content:
                    # 注意：这里不再执行 print()
                    self._add_to_dialogue_history('Narration', content=generated_content)
                else:
                    log_error("旁白生成失败。")
                    self.game_over = True
                    return
            else: # 这是处理 Mode: Preset 的情况
                print(f"{TermColors.GREY}旁白: {content}{TermColors.RESET}")
                self._add_to_dialogue_history('Narration', content=content)
        
        elif event_type == 'Dialogue':
            char_id = self._format_string(params['Character'])
            char_name = self.character_files.get(char_id, {}).get('name', char_id)
            
            if params['Mode'] == 'Preset':
                print(f"{TermColors.CYAN}{char_name}:{TermColors.RESET} {content}")
                self._add_to_dialogue_history('Dialogue', character_id=char_id, content=content)
            
            elif params['Mode'] == 'Prompt':
                # 构建LLM请求
                messages = []
                # 1. 添加角色设定
                # --- 修复点：格式化角色prompt中的模板变量 ---
                character_prompt = self._format_string(self.character_files[char_id]['prompt'])
                messages.append({"role": "system", "content": character_prompt})
                # 2. 添加对话历史
                for record in self.dialogue_history[-10:]: # 取最近10条
                    # 从记录中获取纯文本内容
                    content = record.get('content') or record.get('data', {}).get('content')
                    if not content:
                        continue

                    if record['type'] == 'Dialogue':
                        hist_char_id = record.get('data', {}).get('character_id')
                        if hist_char_id:
                            # 根据当前要生成对话的角色ID (char_id) 来决定历史记录中的角色是 'assistant' 还是 'user'
                            role = "assistant" if hist_char_id == char_id else "user"
                            messages.append({"role": role, "content": content}) # 修正: 只发送纯文本内容
                    
                    elif record['type'] == 'Player':
                        # 玩家的发言对任何AI角色来说都是 'user'
                        messages.append({"role": "user", "content": content}) # 修正: 只发送纯文本内容

                # 3. 添加当前Prompt
                messages.append({"role": "system", "content": f"这是你的内心独白或行为指引，请根据它生成一句对话。不要把内心独白本身说出来。\n内心独白: {content}"})
                
                # --- 核心修改点 ---
                # chat_with_deepseek 内部已经处理了流式打印
                # 它返回的 response 仅用于保存历史记录
                response = chat_with_deepseek(messages, char_name, color_code=TermColors.CYAN)

                if response:
                    # 注意：移除了这里的 print() 语句
                    self._add_to_dialogue_history('Dialogue', character_id=char_id, content=response)
                else:
                    log_error("LLM未能生成响应，游戏可能无法继续。")
                    self.game_over = True
        
        elif event_type == 'Player':
            if params['Mode'] == 'Input':
                self.progress['runtime_state'] = 'WaitingForPlayerInput'
                if content: # 有默认提示
                    print(f"{TermColors.YELLOW}你 (可输入或直接回车使用默认): {content}{TermColors.RESET}")
                else:
                    print(f"{TermColors.YELLOW}你:{TermColors.RESET} ", end="")
            elif params['Mode'] == 'Preset':
                print(f"{TermColors.YELLOW}你:{TermColors.RESET} {content}")
                self._add_to_dialogue_history('Player', content=content)
        
        elif event_type == 'Notice':
            # 检查是否为 Prompt 模式
            if params.get('Mode') == 'Prompt':
                log_debug("生成 'Notice' prompt...")
                # 公告通常由DM发出，所以使用DM的人设
                dm_char_id = self.global_config.get('dm_role_id', 'DM')  # 假设全局配置中有DM角色ID
                dm_char = self.character_files.get(dm_char_id)
                # --- 修复点：格式化DM角色prompt中的模板变量 ---
                if dm_char:
                    dm_prompt = self._format_string(dm_char['prompt'])
                else:
                    dm_prompt = "你是一个剧本杀的DM（主持人）。"
                
                messages = [
                    {"role": "system", "content": dm_prompt},
                    {"role": "user", "content": f"这是你的生成要求：\n{content}"}
                ]
                # 可以加入对话历史
                for record in self.dialogue_history[-5:]:
                    # 从记录中获取纯文本内容
                    content = record.get('content') or record.get('data', {}).get('content')
                    if not content:
                        continue

                    if record['type'] == 'Dialogue':
                        hist_char_id = record.get('data', {}).get('character_id')
                        if hist_char_id:
                            # 对于公告生成，所有历史对话都作为用户输入
                            messages.insert(-1, {"role": "user", "content": content})
                    elif record['type'] == 'Player':
                        # 玩家发言也作为用户输入
                        messages.insert(-1, {"role": "user", "content": content})
                
                generated_content = chat_with_deepseek(messages, character_name=dm_char.get('name', 'DM') if dm_char else 'DM', color_code=TermColors.MAGENTA)
                if generated_content:
                    content = generated_content
                else:
                    log_error("公告生成失败。")
                    self.game_over = True
                    return

            location = params.get('Location', 'popup')
            print(f"\n{TermColors.MAGENTA}--- [{location.upper()}] 公告 ---\n{content}\n--------------------{TermColors.RESET}")
            self._add_to_dialogue_history('Notice', location=location, content=content)
        
        elif event_type == 'Chapter':
            print(f"\n{TermColors.GREEN}===== {content['Title']} ====={TermColors.RESET}")
            print(f"{TermColors.GREY}{content['Description']}{TermColors.RESET}\n")
            self._add_to_dialogue_history('Chapter', **content)

        elif event_type == 'Action':
            tool = params['Tool']
            var_name = params['Variable']
            if tool == 'Set':
                self.game_state[var_name] = content['Value']
            elif tool == 'Calculate':
                expr = self._format_string(content['Expression'])
                self.game_state[var_name] = eval(expr, {}, self.game_state)
            elif tool == 'Random':
                self.game_state[var_name] = random.randint(content['Min'], content['Max'])
            elif tool == 'RandomChoice':
                choices = content['Choices']
                self.game_state[var_name] = random.choice(choices)
            log_debug(f"Action执行完毕, {var_name} = {self.game_state.get(var_name)}")


    def _process_end_condition(self, end_data):
        if not end_data:
            log_info("剧情单元结束，无EndCondition，游戏结束。")
            self.game_over = True
            return

        end_type = end_data['Type']
        log_debug(f"处理EndCondition: {end_type}")

        if end_type == 'Linear':
            self._transition_to_unit(end_data['NextUnitID'])
        
        elif end_type == 'FreeTime' or end_type == 'LimitedFreeTime':
            self.progress['runtime_state'] = 'InFreeTime'
            self.progress['free_time_context'] = {
                'end_condition': end_data,
                'turns_taken': 0
            }
            log_info_color(self._format_string(end_data['InstructionToPlayer']), TermColors.BLUE)
        
        elif end_type == 'Branching':
            if end_data['Method'] == 'PlayerChoice':
                self.progress['runtime_state'] = 'WaitingForPlayerChoice'
                self.progress['choice_context'] = end_data
                print(f"{TermColors.YELLOW}请做出你的选择：{TermColors.RESET}")
                for key, branch in end_data['Branches'].items():
                    print(f"  [{key}] {self._format_string(branch['DisplayText'])}")
            
            elif end_data['Method'] == 'AIChoice':
                log_info_color("AI 正在做出决定...", TermColors.BLUE)
                self.progress['runtime_state'] = 'ProcessingAIChoice'
                self.progress['ai_choice_context'] = end_data
                self._execute_ai_choice()  # 直接调用处理函数

        elif end_type == 'Conditional':
            found_match = False
            for case in end_data['Cases']:
                if self._evaluate_condition(case['Condition']):
                    # 递归处理 'Then' 中的EndCondition
                    self._process_end_condition(case['Then'])
                    found_match = True
                    break
            if not found_match and 'Else' in end_data:
                self._process_end_condition(end_data['Else'])
        
        else:
            log_error(f"未知的EndCondition类型: {end_type}")
            self.game_over = True

    def _transition_to_unit(self, unit_id):
        log_debug(f"切换剧情单元到: {unit_id}")
        self.progress['progress_pointer']['current_unit_id'] = unit_id
        self.progress['progress_pointer']['last_completed_event_index'] = -1
        self.progress['runtime_state'] = 'ExecutingEvents'

    def provide_player_input(self, text):
        state = self.progress['runtime_state']
        if state == 'WaitingForPlayerInput':
            pointer = self.progress['progress_pointer']
            next_event_index = pointer['last_completed_event_index'] + 1
            events = self.current_story_unit.get('Events', [])
            event_data = events[next_event_index]
            _, event_content = list(event_data.items())[0]

            if not text.strip() and event_content: # 用户直接回车，使用默认值
                text = self._format_string(event_content)
                print(f"{TermColors.YELLOW}(使用默认): {text}{TermColors.RESET}")
            
            # --- 新增: 将玩家的输入存入运行时上下文 ---
            # 这使得紧随其后的事件（如Action:Set）可以使用 {player_input}
            self.runtime_context['player_input'] = text

            self._add_to_dialogue_history('Player', content=text)
            pointer['last_completed_event_index'] = next_event_index
            self.progress['runtime_state'] = 'ExecutingEvents'
            self.run() # 继续执行
        
        elif state == 'InFreeTime':
            context = self.progress['free_time_context']
            end_condition = context['end_condition']
            exit_prompt = self._format_string(end_condition.get('ExitPromptInInputBox', ''))

            if exit_prompt and exit_prompt in text:
                log_info("检测到退出语，自由时间结束。")
                self._transition_to_unit(end_condition['NextUnitID'])
                self.run()
                return

            # --- 新增: 将玩家的输入存入运行时上下文 ---
            self.runtime_context['player_input'] = text
            
            self._add_to_dialogue_history('Player', content=text)
            
            # AI 回复 - 使用智能轮询机制
            # 优先选择DM角色
            dm_char_id = self.global_config.get('dm_role_id')
            if dm_char_id and dm_char_id in self.character_files:
                ai_char_id = dm_char_id
            else:
                # 如果没有DM，则进行轮询
                all_ai_roles = self.global_config['character_roles']
                last_responder_index = self.progress.get('last_responder_index', -1)
                next_responder_index = (last_responder_index + 1) % len(all_ai_roles)
                ai_char_id = all_ai_roles[next_responder_index]
                self.progress['last_responder_index'] = next_responder_index  # 记录本次响应者索引
            
            ai_char_name = self.character_files[ai_char_id]['name']

            # --- 修复点：格式化AI角色prompt中的模板变量 ---
            ai_system_prompt = self._format_string(self.character_files[ai_char_id]['prompt'])
            messages = [{"role": "system", "content": ai_system_prompt}]
            # 添加历史
            for record in self.dialogue_history[-10:]:
                if record['type'] == 'Dialogue':
                     hist_char_id = record.get('data', {}).get('character_id')
                     role = "assistant" if hist_char_id == ai_char_id else "user"
                     content = record.get('content') or record.get('data', {}).get('content')
                     if content and hist_char_id:
                         messages.append({"role": role, "content": content})
                elif record['type'] == 'Player':
                     content = record.get('content') or record.get('data', {}).get('content')
                     if content:
                         messages.append({"role": "user", "content": content})
            
            response = chat_with_deepseek(messages, ai_char_name, color_code=TermColors.CYAN)
            if response:
                self._add_to_dialogue_history('Dialogue', character_id=ai_char_id, content=response)
            
            context['turns_taken'] += 1
            if end_condition['Type'] == 'LimitedFreeTime' and context['turns_taken'] >= end_condition['MaxTurns']:
                log_info("达到最大轮次，自由时间结束。")
                self._transition_to_unit(end_condition['NextUnitID'])
                self.run()

        elif state == 'WaitingForPlayerChoice':
            context = self.progress['choice_context']
            if text in context['Branches']:
                branch = context['Branches'][text]
                self._transition_to_unit(branch['NextUnitID'])
                self.run()
            else:
                log_warning("无效的选择，请重新输入。")
                print(f"{TermColors.RED}无效选择，请输入方括号内的字母。{TermColors.RESET}")

    def _execute_ai_choice(self):
        """执行 AI 选择逻辑，包括决策和判断，然后转换剧情单元。"""
        context = self.progress.get('ai_choice_context')
        if not context:
            log_error("无法执行 AI Choice，上下文中缺少必要信息。")
            self.game_over = True
            return

        decider_id = self._format_string(context['DeciderCharacterID'])
        decider_char = self.character_files.get(decider_id)
        if not decider_char:
            log_error(f"AI Choice 失败：找不到决策角色 '{decider_id}'。")
            self.game_over = True
            return
            
        # 1. 构建决策 LLM 请求 (Decision Call)
        decision_prompt = self._format_string(context['DecisionPromptForAI'])
        decision_messages = []
        # --- 修复点：格式化决策角色prompt中的模板变量 ---
        decider_system_prompt = self._format_string(decider_char['prompt'])
        decision_messages.append({"role": "system", "content": decider_system_prompt})
        
        # 添加对话历史 (与 Dialogue Prompt 逻辑相同)
        for record in self.dialogue_history[-15:]:  # 可以适当增加历史记录长度
            # 从记录中获取纯文本内容
            content = record.get('content') or record.get('data', {}).get('content')
            if not content:
                continue

            if record['type'] == 'Dialogue':
                hist_char_id = record.get('data', {}).get('character_id')
                if hist_char_id:
                    # 根据决策者ID (decider_id) 来决定历史记录中的角色是 'assistant' 还是 'user'
                    role = "assistant" if hist_char_id == decider_id else "user"
                    decision_messages.append({"role": role, "content": content})
            elif record['type'] == 'Player':
                # 玩家的发言对决策AI来说都是 'user'
                decision_messages.append({"role": "user", "content": content})
        
        decision_messages.append({"role": "system", "content": decision_prompt})

        # 调用LLM获取决策文本 (这里不直接打印，是AI的内心思考)
        log_info(f"正在为角色 {decider_char['name']} 获取决策...")
        ai_decision_text = chat_with_deepseek(decision_messages, character_name=f"{decider_char['name']}(内心)", is_internal_thought=True, color_code=TermColors.CYAN)

        if not ai_decision_text:
            log_error("AI 未能做出决策，剧情无法继续。")
            self.game_over = True
            return
            
        log_debug(f"AI 决策原文: {ai_decision_text}")

        # 2. 构建判断 LLM 请求 (Judge Call)
        judge_prompt = self._format_string(context['JudgePromptForSystem'])
        judge_messages = [
            {"role": "system", "content": judge_prompt},
            {"role": "user", "content": f"请根据以下AI角色的决策文本进行判断：\n\n---\n{ai_decision_text}\n---"}
        ]
        
        log_info("系统正在判断 AI 的选择...")
        judged_result = chat_with_deepseek(judge_messages, character_name="系统判断", is_internal_thought=True, color_code=TermColors.CYAN)
        
        if not judged_result:
            log_error("系统未能判断 AI 的决策，剧情无法继续。")
            self.game_over = True
            return

        # 3. 处理结果并转换剧情单元
        final_choice = judged_result.strip().upper()
        log_info_color(f"AI 的选择已被系统判断为: '{final_choice}'", TermColors.GREEN)

        if final_choice in context['Branches']:
            next_unit_id = context['Branches'][final_choice]
            # 清理上下文并转换
            del self.progress['ai_choice_context']
            self._transition_to_unit(next_unit_id)
            self.run()  # 立即继续游戏循环
        else:
            log_error(f"判断结果 '{final_choice}' 无效，在 Branches 中找不到匹配项。")
            self.game_over = True
```

### 文件: `llm_interface.py`

```python
# llm_interface.py
import requests
import json
import sys
import time

import config
from logger import (
    log_debug,
    log_info_color,
    log_warning,
    log_error_color,
    start_loading_animation,
    stop_loading_animation,
    TermColors
)

def chat_with_deepseek(messages_payload, character_name="AI", is_internal_thought=False, color_code=TermColors.CYAN):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {config.API_KEY}"}
    payload = {
        "model": config.MODEL_NAME, "messages": messages_payload, "stream": True,
        "max_tokens": config.MAX_TOKENS, "temperature": config.TEMPERATURE
    }

    if config.DEBUG_MODE:
        log_debug(f"--- 发送给 DeepSeek API 的 Payload (角色: {character_name}) ---")
        debug_payload_display = json.loads(json.dumps(payload))
        for msg in debug_payload_display.get("messages", []):
            if 'content' in msg and isinstance(msg['content'], str):
                msg['content'] = msg['content'].replace('\n', ' ')[:150] + ("..." if len(msg['content']) > 150 else "")
        formatted_payload_str = json.dumps(debug_payload_display, ensure_ascii=False, indent=2)
        for line in formatted_payload_str.splitlines(): log_debug(line)
        log_debug("--- Payload 结束 ---")

    assistant_full_response = ""
    api_call_succeeded = False
    animation_stopped_internally = False

    try:
        if not is_internal_thought:
            animation_msg = f"{TermColors.LIGHT_BLUE}{character_name} 正在思考...{TermColors.RESET}"
            start_loading_animation(
                message=animation_msg,
                animation_style_key='moon',
            )

        response = requests.post(config.API_URL, headers=headers, json=payload, stream=True,
                                 timeout=config.API_TIMEOUT_SECONDS)
        response.raise_for_status()

        first_chunk_received = False
        for chunk in response.iter_lines():
            if chunk:
                decoded_line = chunk.decode('utf-8')
                if decoded_line.startswith("data: "):
                    json_data_str = decoded_line[len("data: "):]
                    if json_data_str.strip() == "[DONE]":
                        break
                    try:
                        data = json.loads(json_data_str)
                        content_piece = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if content_piece:
                            if not is_internal_thought:
                                if not first_chunk_received:
                                    stop_loading_animation()
                                    animation_stopped_internally = True
                                    print(f"{color_code}{character_name}:{TermColors.RESET} ", end="", flush=True)
                                    first_chunk_received = True
                                sys.stdout.write(f"{color_code}{content_piece}{TermColors.RESET}")
                                sys.stdout.flush()
                            assistant_full_response += content_piece
                    except (json.JSONDecodeError, IndexError):
                        log_warning(f"API Stream: 解码或索引错误，数据块: {json_data_str}")

        if not is_internal_thought:
            if first_chunk_received:
                print()
                api_call_succeeded = True
            elif response.ok:
                log_warning("API 响应流结束，但未返回任何文本内容。")
                api_call_succeeded = True
        else:
            # 内部思考模式，只要有响应就算成功
            api_call_succeeded = response.ok

    except requests.exceptions.HTTPError as e:
        log_error_color(f"\nAPI请求HTTP错误: {e} - {e.response.status_code} {e.response.reason}")
        try:
            log_error_color(f"错误详情: {json.dumps(e.response.json(), ensure_ascii=False, indent=2)}")
        except ValueError:
            log_error_color(f"错误响应体 (非JSON): {e.response.text}")
    except requests.exceptions.RequestException as e:
        log_error_color(f"\nAPI请求失败: {e}")
    finally:
        if not is_internal_thought and not animation_stopped_internally:
            stop_loading_animation(success=api_call_succeeded, final_message="与API通信中断" if not api_call_succeeded else None)

    return assistant_full_response if api_call_succeeded else None
```

### 文件: `logger.py`

```python
# logger.py
import logging
import sys
import time
import threading
from datetime import datetime
import os
import re  # Import re for ANSI stripping

# 日志配置
ENABLE_FILE_LOGGING = True  # 是否启用文件日志记录
LOG_FILE_DIRECTORY = "run_logs"  # 日志文件存储的相对目录

# 注意，若环境变量DEBUG_MODE = True/false时，会覆盖LOG_FILE_LEVEL的设置
LOG_FILE_LEVEL = logging.DEBUG  # 可以设置为 logging.DEBUG，logging.INFO, logging.WARNING, logging.ERROR

ANIMATION_STYLES = {
    'braille': ['⢿', '⣻', '⣽', '⣾', '⣷', '⣯', '⣟', '⡿'],
    'spinner': ['-', '\\', '|', '/'],
    'dots': ['.  ', '.. ', '...', ' ..', '  .', '   '],
    'arrows': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    'moon': ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘'],
    'clock': ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'],
    'directional_arrows_unicode': ['⬆️', '↗️', '➡️', '↘️', '⬇️', '↙️', '⬅️', '↖️'],
    'traffic_lights': ['🔴', '🟡', '🟢'],
    'growth_emoji': ['🌱', '🌿', '🌳'],
    'weather_icons': ['☀️', '☁️', '🌧️', '⚡️'],
    'heartbeat': ['♡', '♥'],
}

_ansi_escape_regex = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def _strip_ansi_codes(text):
    """Removes ANSI escape codes from a string."""
    return _ansi_escape_regex.sub('', text)

sys.stderr.flush()

def wcswidth(s):
    """回退 wcswidth, 将非 ASCII 字符视为宽度2。应在剥离ANSI码后使用。"""
    if not isinstance(s, str):
        return len(s) if s else 0
    length = 0
    for char_ in s:  # Assumes s is already stripped of ANSI codes
        if ord(char_) < 128:
            length += 1
        else:
            length += 2
    return length

class TermColors:
    GREY = '\033[90m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    LIGHT_BLUE = '\033[94m'  # Actually same as BLUE in this list, but kept for intent
    ORANGE = '\033[38;5;208m'

_logger = None
_animation_thread = None
_stop_animation_event = threading.Event()

_is_animating = False
_current_animation_line_width = 0
_animation_state_lock = threading.Lock()

DEFAULT_ANIMATION_STYLE_KEY = 'braille'
DEFAULT_ANIMATION_COLOR = TermColors.WHITE  # Default color for animation if not specified

class AnimationAwareStreamHandler(logging.StreamHandler):
    def emit(self, record):
        global _is_animating, _current_animation_line_width, _animation_state_lock

        if hasattr(record, 'is_animation_control') and record.is_animation_control:
            super().emit(record)
            return

        current_animation_active_locally = False
        current_width_to_clear_locally = 0

        with _animation_state_lock:
            current_animation_active_locally = _is_animating
            current_width_to_clear_locally = _current_animation_line_width

        if current_animation_active_locally and current_width_to_clear_locally > 0:
            self.acquire()
            try:
                self.flush()
                # Ensure the full line is cleared, then cursor to start
                self.stream.write("\r" + " " * current_width_to_clear_locally + "\r")
                self.stream.flush()
            finally:
                self.release()

        super().emit(record)

class ColoredFormatter(logging.Formatter):
    DATE_FORMAT = "%Y-%m-%d-%H:%M:%S"

    def __init__(self, show_timestamp=True):
        super().__init__(datefmt=self.DATE_FORMAT)
        self.show_timestamp = show_timestamp

    def format(self, record):
        if hasattr(record, 'is_animation_control') and record.is_animation_control:
            return record.getMessage()

        timestamp_part = ""
        if self.show_timestamp:
            timestamp_str = self.formatTime(record, self.DATE_FORMAT)
            timestamp_part = f"{timestamp_str} "

        message_content = record.getMessage()
        level_name = record.levelname
        level_prefix_text = f"[{level_name}]: "

        if record.levelno == logging.DEBUG:
            return f"{TermColors.GREY}{timestamp_part}{level_prefix_text}{message_content}{TermColors.RESET}"

        level_color = ""
        if record.levelno == logging.INFO:
            level_color = TermColors.GREEN
        elif record.levelno == logging.WARNING:
            level_color = TermColors.YELLOW
        elif record.levelno == logging.ERROR:
            level_color = TermColors.RED

        colored_level_prefix = f"{level_color}{level_prefix_text}{TermColors.RESET}"
        return f"{timestamp_part}{colored_level_prefix}{message_content}"


def _animate(message="Loading", animation_chars=None, color_code=DEFAULT_ANIMATION_COLOR):
    global _is_animating, _current_animation_line_width, _animation_state_lock, _stop_animation_event

    if animation_chars is None:
        animation_chars = ANIMATION_STYLES[DEFAULT_ANIMATION_STYLE_KEY]

    idx = 0
    last_char_for_clear = animation_chars[0]

    while not _stop_animation_event.is_set():
        char = animation_chars[idx % len(animation_chars)]
        last_char_for_clear = char

        full_animation_line_with_ansi = f"{color_code}{message} {char}{TermColors.RESET} "

        stripped_line_for_width = _strip_ansi_codes(full_animation_line_with_ansi)
        current_visible_width = wcswidth(stripped_line_for_width)

        with _animation_state_lock:
            _current_animation_line_width = current_visible_width

        sys.stdout.write(f"\r{full_animation_line_with_ansi}")
        sys.stdout.flush()

        idx += 1
        time.sleep(0.12)

    final_animation_line_to_clear_ansi = f"{color_code}{message} {last_char_for_clear}{TermColors.RESET} "
    stripped_final_line = _strip_ansi_codes(final_animation_line_to_clear_ansi)
    width_to_clear = wcswidth(stripped_final_line)

    sys.stdout.write("\r" + " " * width_to_clear + "\r")
    sys.stdout.flush()

    with _animation_state_lock:
        _is_animating = False
        _current_animation_line_width = 0


def start_loading_animation(message="Processing",
                            animation_style_key=DEFAULT_ANIMATION_STYLE_KEY,
                            animation_color=DEFAULT_ANIMATION_COLOR):
    global _animation_thread, _stop_animation_event, _is_animating, _current_animation_line_width, _animation_state_lock

    with _animation_state_lock:
        if _is_animating:
            log_debug("Animation already running, not starting another one.")
            return

        _stop_animation_event.clear()
        selected_chars = ANIMATION_STYLES.get(animation_style_key, ANIMATION_STYLES[DEFAULT_ANIMATION_STYLE_KEY])

        initial_char = selected_chars[0]
        initial_full_line_ansi = f"{animation_color}{message} {initial_char}{TermColors.RESET} "
        stripped_initial_line = _strip_ansi_codes(initial_full_line_ansi)
        initial_width = wcswidth(stripped_initial_line)

        _is_animating = True
        _current_animation_line_width = initial_width

        _animation_thread = threading.Thread(target=_animate,
                                             args=(message, selected_chars, animation_color),
                                             daemon=True)
        _animation_thread.start()


def stop_loading_animation(success=True, final_message=None):
    global _animation_thread, _stop_animation_event, _is_animating, _animation_state_lock

    was_animating_when_called = False
    with _animation_state_lock:
        if _is_animating or _animation_thread is not None:
            was_animating_when_called = True
            _stop_animation_event.set()

    if not was_animating_when_called:
        if final_message:
            if success:
                log_info(f"{TermColors.GREEN}✔{TermColors.RESET} {final_message}")
            else:
                log_error(f"{TermColors.RED}✖{TermColors.RESET} {final_message}")
        return

    current_thread_ref = _animation_thread
    if current_thread_ref and current_thread_ref.is_alive():
        current_thread_ref.join(timeout=2)

    with _animation_state_lock:
        _is_animating = False
        _current_animation_line_width = 0
        _animation_thread = None

    if final_message:
        if success:
            log_info(f"{TermColors.GREEN}✔{TermColors.RESET} {final_message}")
        else:
            log_error(f"{TermColors.RED}✖{TermColors.RESET} {final_message}")

def initialize_logger(app_name="AppLogger", config_debug_mode=True, show_timestamp=True):
    global _logger
    _logger = logging.getLogger(app_name)
    _logger.propagate = False

    if config_debug_mode:
        _logger.setLevel(logging.DEBUG)
    else:
        _logger.setLevel(logging.INFO)

    if _logger.hasHandlers():
        for handler in _logger.handlers[:]:
            handler.close()
            _logger.removeHandler(handler)

    console_handler = AnimationAwareStreamHandler(sys.stdout)
    console_formatter = ColoredFormatter(show_timestamp=show_timestamp)
    console_handler.setFormatter(console_formatter)
    _logger.addHandler(console_handler)

    if ENABLE_FILE_LOGGING:
        try:
            if not os.path.exists(LOG_FILE_DIRECTORY):
                os.makedirs(LOG_FILE_DIRECTORY, exist_ok=True)

            log_filename = datetime.now().strftime(f"{app_name}_%Y-%m-%d_%H-%M-%S.log")
            log_filepath = os.path.join(LOG_FILE_DIRECTORY, log_filename)

            file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt=ColoredFormatter.DATE_FORMAT
            )
            file_handler.setFormatter(file_formatter)
            file_handler.setLevel(LOG_FILE_LEVEL)
            _logger.addHandler(file_handler)
        except Exception as e:
            sys.stderr.write(
                f"{TermColors.RED}错误: 初始化文件日志记录失败: {e}{TermColors.RESET}\n"
            )
            sys.stderr.flush()
    return _logger

def get_logger():
    global _logger
    if _logger is None:
        sys.stderr.write(
            f"{TermColors.YELLOW}警告: 日志记录器在显式初始化之前被访问。 "
            f"将使用默认值进行初始化。{TermColors.RESET}\n"
        )
        sys.stderr.flush()
        _logger = initialize_logger()
    return _logger

def log_debug(message, *args, **kwargs): get_logger().debug(message, *args, **kwargs)

def log_info(message, *args, **kwargs): get_logger().info(message, *args, **kwargs)

def log_warning(message, *args, **kwargs): get_logger().warning(message, *args, **kwargs)

def log_error(message, *args, **kwargs): get_logger().error(message, *args, **kwargs)

def log_info_color(message, color_code=TermColors.GREEN, *args, **kwargs):
    get_logger().info(f"{color_code}{message}{TermColors.RESET}", *args, **kwargs)

def log_warning_color(message, color_code=TermColors.YELLOW, *args, **kwargs):
    get_logger().warning(f"{color_code}{message}{TermColors.RESET}", *args, **kwargs)

def log_error_color(message, color_code=TermColors.RED, *args, **kwargs):
    get_logger().error(f"{color_code}{message}{TermColors.RESET}", *args, **kwargs)

def log_rag_output(message, *args, **kwargs):  # Example of a domain-specific logger
    get_logger().info(f"{TermColors.BLUE}{message}{TermColors.RESET}", *args, **kwargs)

if __name__ == "__main__":
    # 1. Initialize logger - app_name will be part of the log file name
    initialize_logger(app_name="演示应用", config_debug_mode=True, show_timestamp=True)
    log_info("=============== 炫彩日志与加载动画演示开始 ===============")
    log_debug("这是一个调试消息：日志系统已成功初始化。")
    if not ENABLE_FILE_LOGGING:
        log_warning("文件日志记录已禁用。如需启用，请设置 ENABLE_FILE_LOGGING = True")
    else:
        log_info(f"文件日志已启用，日志将存储在 '{LOG_FILE_DIRECTORY}' 目录下。")

    # 2. Basic log levels demo
    log_info("演示2.1: log_info是一条 INFO 信息。")
    log_warning("演示2.2: log_warning是一条警告 WARNING 信息。")
    log_error("演示2.3: log_error是一条错误 ERROR 信息。")
    log_debug("演示2.4: log_debug是一条调试 DEBUG 信息。DEBUG信息（包括对应时间戳）全部保持灰色")

    log_info_color("演示2.5: log_info_color的 INFO 信息默认带有醒目的绿色。")
    log_info_color("当然，你也可以自定义log_info_color的颜色", TermColors.MAGENTA)
    log_warning_color("演示2.6: log_warning_color的 WARNING 信息默认带有醒目的黄色。")
    log_warning_color("当然你也可以改成蓝的", TermColors.BLUE)
    log_error_color("演示2.7: log_error_color的 ERROR 信息默认带有醒目的红色。")
    log_error_color("一个绿色的ERROR?", TermColors.GREEN)

    # 3. Loading animation demo
    log_info("演示3.1: 默认加载动画 (braille样式, 默认白色)")
    # Pass message without internal colors, use animation_color for the whole line
    start_loading_animation(message="任务A处理中")
    time.sleep(2)
    stop_loading_animation(success=True, final_message="任务A成功完成!")

    log_info("演示3.2: 自定义动画样式 (spinner样式, 默认白色)")
    start_loading_animation(message="任务B执行中", animation_style_key='spinner')
    time.sleep(2)
    stop_loading_animation(success=True, final_message="任务B (spinner) 执行完毕!")

    log_info("演示3.3: 自定义动画颜色 (默认braille样式, 青色)")
    start_loading_animation(message="任务C加载中", animation_color=TermColors.CYAN)
    time.sleep(2)
    stop_loading_animation(success=True, final_message="任务C (青色) 加载完成!")

    log_info("演示3.4: 传递本身带颜色的消息给动画")
    # This shows that message can carry its own colors, and animation_color is an outer wrapper
    # animation_color (default WHITE) wraps (MAGENTA "Task D" RESET) + char + RESET
    start_loading_animation(
        message=f"{TermColors.MAGENTA}任务D(本身品红){TermColors.RESET}进行中",
        animation_style_key='arrows',
        animation_color=TermColors.YELLOW  # Yellow wrapper
    )
    time.sleep(2.5)
    stop_loading_animation(success=True, final_message="任务D (品红内容，黄色包装) 完成!")

    log_info("演示3.5: 其他动画样式 (moon样式, 浅蓝色)")
    start_loading_animation(message="月相观察", animation_style_key='moon', animation_color=TermColors.LIGHT_BLUE)
    time.sleep(2.5)
    stop_loading_animation(success=True, final_message="月相观察完毕!")

    log_info("演示3.6: 动画期间进行日志记录 (dots样式, 橙色)")
    start_loading_animation(message="橙色点点任务", animation_style_key='dots', animation_color=TermColors.ORANGE)
    log_info("动画已启动，现在记录一条 INFO 消息，动画会自动避让。")
    time.sleep(1)
    log_warning("这是一条警告 WARNING 消息，动画仍在后台继续。")
    time.sleep(1)
    log_debug("一条调试 DEBUG 消息，动画即将停止并模拟失败。")
    time.sleep(1)
    stop_loading_animation(success=False, final_message="橙色点点任务模拟失败。")

    log_info("演示3.7: 停止动画时不显示最终消息")
    start_loading_animation(message="短暂处理")
    time.sleep(1.5)
    stop_loading_animation()  # No final_message
    log_info("动画已停止，不提供 final_message。")

    # 4. Special color log functions
    log_info("演示4.1: 使用 log_info_color 输出自定义颜色 INFO (例如紫红色)")
    log_info_color("这是一条紫红色的 INFO 信息。", TermColors.MAGENTA)

    log_info("演示4.2: 使用 log_rag_output 输出特定格式 INFO")
    log_rag_output("这是一个RAG 模型输出内容 (蓝色)")

    # 5. Re-initialize logger: turn off console timestamp
    log_info("演示5: 重新初始化日志，关闭控制台时间戳 (文件日志不受影响)")
    initialize_logger(app_name="演示应用-无时间戳", config_debug_mode=True, show_timestamp=False)
    log_info("这条 INFO 信息在控制台不显示时间戳。")
    log_debug("这条 DEBUG 信息在控制台也不显示时间戳。")
    start_loading_animation(message="无时间戳任务执行")
    time.sleep(1.5)
    stop_loading_animation(final_message="无时间戳任务完成。")

    # 6. Restore timestamp and test print() interaction
    log_info("演示6: 恢复时间戳并测试动画与普通 print() 语句的交互")
    initialize_logger(app_name="演示应用", config_debug_mode=True, show_timestamp=True)  # Restore default
    log_info("日志时间戳已恢复。")

    print(f"{TermColors.YELLOW}这是一条普通的 print() 语句，在动画开始前。{TermColors.RESET}")
    start_loading_animation(message="测试与print交互")
    time.sleep(1)
    # Standard print() is not intercepted by the logger's handler.
    # It will likely mess up the animation line.
    print(f"{TermColors.RED}警告: 下面这条 print() 语句会打断当前动画行。{TermColors.RESET}")
    time.sleep(1)
    log_info("这条日志消息在 print() 之后，会由 AnimationAwareStreamHandler 正确处理。")
    time.sleep(1)
    stop_loading_animation(final_message="动画与 print() 交互测试结束。")
    print(f"{TermColors.GREEN}动画结束后的另一条 print() 语句。{TermColors.RESET}")

    # 7. End
    if ENABLE_FILE_LOGGING:
        log_info(f"所有演示已完成。请检查 '{LOG_FILE_DIRECTORY}' 目录中的日志文件。")
    else:
        log_info("所有演示已完成。文件日志记录当前已禁用。")
    log_info("=============== 演示结束 ===============")
```

### 文件: `main.py`

```python
# main.py
import os
import sys
from datetime import datetime

import config
from logger import initialize_logger, log_info, log_error, log_warning, log_debug, log_info_color, TermColors
from game_engine import GameEngine

def select_from_list(items, prompt):
    if not items:
        return None
    for i, item in enumerate(items):
        print(f"  [{i + 1}] {item}")
    while True:
        try:
            choice = input(f"{prompt} (输入数字): ")
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(items):
                return items[choice_idx]
            else:
                print(f"{TermColors.RED}无效的数字，请输入 1 到 {len(items)} 之间的数字。{TermColors.RESET}")
        except ValueError:
            print(f"{TermColors.RED}无效的输入，请输入数字。{TermColors.RESET}")

def start_new_game():
    log_info("开始新游戏流程...")
    
    # 1. 选择剧本
    packs_path = config.STORY_PACKS_BASE_PATH
    available_packs = [d for d in os.listdir(packs_path) if os.path.isdir(os.path.join(packs_path, d))]
    if not available_packs:
        log_error(f"在 '{packs_path}' 目录下未找到任何剧本包。")
        return None
    
    print(f"\n{TermColors.YELLOW}请选择一个剧本包：{TermColors.RESET}")
    chosen_pack_name = select_from_list(available_packs, "选择剧本")
    if not chosen_pack_name: return None
    chosen_pack_path = os.path.join(packs_path, chosen_pack_name)

    # 2. 读取剧本配置，确定所需角色
    try:
        with open(os.path.join(chosen_pack_path, '全局剧情配置.yaml'), 'r', encoding='utf-8') as f:
            pack_config = yaml.safe_load(f)
        required_roles = pack_config['character_roles']
    except (FileNotFoundError, KeyError, yaml.YAMLError) as e:
        log_error(f"读取剧本 '{chosen_pack_name}' 的配置失败: {e}")
        return None
    
    # 3. 为每个角色选择人设
    chars_path = config.CHARACTERS_BASE_PATH
    available_chars = [f for f in os.listdir(chars_path) if f.endswith('.yaml')]
    if not available_chars:
        log_error(f"在 '{chars_path}' 目录下未找到任何人设文件。")
        return None
    
    character_selections = {}
    print(f"\n{TermColors.YELLOW}请为剧本中的每个角色选择一个人设：{TermColors.RESET}")
    for role_id in required_roles:
        print(f"--- 为角色 '{role_id}' 选择人设 ---")
        chosen_char_file = select_from_list(available_chars, f"选择人设")
        if not chosen_char_file: return None
        character_selections[role_id] = os.path.join(chars_path, chosen_char_file)
        # 从列表中移除已选的角色，避免重复选择
        available_chars.remove(chosen_char_file)

    # 4. 初始化游戏引擎
    engine = GameEngine()
    if engine.load_story_pack(chosen_pack_path, character_selections):
        return engine
    return None

def load_game_from_save():
    log_info("加载游戏存档...")
    saves_path = config.SAVES_BASE_PATH
    available_saves = [d for d in os.listdir(saves_path) if os.path.isdir(os.path.join(saves_path, d))]
    if not available_saves:
        log_warning("未找到任何存档。")
        return None

    print(f"\n{TermColors.YELLOW}请选择一个存档加载：{TermColors.RESET}")
    chosen_save_name = select_from_list(available_saves, "选择存档")
    if not chosen_save_name: return None
    
    engine = GameEngine()
    if engine.load_from_save(os.path.join(saves_path, chosen_save_name)):
        return engine
    return None


def game_loop(engine):
    log_info_color("游戏开始！在任何你需要输入的时候，都可以使用 /save 或 /load 命令。", TermColors.GREEN)
    
    # 初次运行
    engine.run()

    while engine.is_running and not engine.game_over:
        try:
            user_input = input()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if user_input.lower().startswith('/save'):
            parts = user_input.split(maxsplit=1)
            save_name = parts[1] if len(parts) > 1 else f"自动存档_{datetime.now().strftime('%H%M%S')}"
            engine.save_game(save_name)
            # 保存后继续等待当前输入
            if engine.progress['runtime_state'] == "WaitingForPlayerInput":
                print(f"{TermColors.YELLOW}你:{TermColors.RESET} ", end="")
            continue
        
        if user_input.lower().startswith('/load'):
            log_warning("在游戏中加载会丢失当前进度。此功能最好在主菜单使用。")
            # 在此简化demo中，游戏中加载会退出当前游戏循环
            return 'load' 

        engine.provide_player_input(user_input)

    log_info_color("游戏结束。", TermColors.MAGENTA)
    return 'menu'


def main():
    initialize_logger(config_debug_mode=config.DEBUG_MODE)
    
    if not config.API_KEY or "YOUR_DEEPSEEK_API_KEY" in config.API_KEY:
        log_error("请在 config.py 文件中设置你的 DeepSeek API Key。")
        return
        
    # 确保文件夹存在
    for path in [config.SAVES_BASE_PATH, config.STORY_PACKS_BASE_PATH, config.CHARACTERS_BASE_PATH]:
        os.makedirs(path, exist_ok=True)

    while True:
        print("\n" + "="*30)
        print(" NeoChat 0.4 - 命令行演示")
        print("="*30)
        print(f"{TermColors.CYAN}  /start - 开始新游戏")
        print(f"  /load  - 加载存档")
        print(f"  /exit  - 退出程序{TermColors.RESET}")
        
        command = input("> ").lower().strip()

        engine = None
        if command == '/start':
            engine = start_new_game()
        elif command == '/load':
            engine = load_game_from_save()
        elif command == '/exit':
            break
        else:
            log_warning("无效的命令。")
            continue
        
        if engine:
            result = game_loop(engine)
            if result == 'load':
                # 如果游戏中加载，则循环到主菜单重新加载
                continue

if __name__ == "__main__":
    import yaml # 确保PyYAML已安装
    main()
```

### 文件: `用来导入剧情的.py`

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import yaml
import textwrap

# --- 配置项 ---
# 剧本包的名称，将作为 story_packs 下的文件夹名
STORY_PACK_NAME = "roxy_labyrinth_adventure"

# 剧本包的根目录
STORY_PACKS_BASE_PATH = "story_packs"
# 角色文件的根目录
CHARACTERS_BASE_PATH = "characters"

# 角色ID，这将作为静态ID写入YAML文件中
ROXY_CHAR_ID = "Roxy"

# --- 工具函数 ---
def write_yaml_file(path, data):
    """将Python字典写入YAML文件，确保UTF-8和Unicode支持"""
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, indent=2)
    print(f"  > 文件已生成: {path}")

def create_directories():
    """创建所有必需的目录结构"""
    print("1. 正在创建目录结构...")
    # 确保主目录存在
    os.makedirs(STORY_PACKS_BASE_PATH, exist_ok=True)
    os.makedirs(CHARACTERS_BASE_PATH, exist_ok=True)
    
    # 创建剧本包的目录
    pack_path = os.path.join(STORY_PACKS_BASE_PATH, STORY_PACK_NAME)
    os.makedirs(pack_path, exist_ok=True)
    os.makedirs(os.path.join(pack_path, "story"), exist_ok=True)
    os.makedirs(os.path.join(pack_path, "save"), exist_ok=True)
    print(f"  > 目录已创建: {pack_path}")
    return pack_path

# --- 内容生成函数 ---

def generate_roxy_character():
    """生成洛琪希的角色YAML文件"""
    print("2. 正在生成洛琪希角色文件...")
    roxy_persona = {
        'name': '洛琪希',
        # 修改点: 优化了Prompt，增加了对简洁性的要求
        'prompt': textwrap.dedent(f"""
        你将扮演《无职转生》中的角色“洛琪希·米格路迪亚”（Roxy Migurdia）。请严格遵守以下设定：
        1.  **身份与性格**: 你是一位知识渊博、经验丰富的魔术师，同时也是玩家{'{player_name}'}的家庭教师。你善良、认真，富有责任感，但有时会因为一些意想不到的事情而感到害羞或慌乱。
        2.  **言谈举止**: 你的言语非常礼貌，习惯使用敬语，即使在亲近的人面前也保持着老师的姿态。例如，称呼玩家为“{'{player_name}'}さん”。
        3.  **核心能力**: 你精通水系魔术，并且拥有广泛的魔物和古代遗迹知识。在迷宫探索中，你会主动提供建议、分析情况，并在必要时施展强大的魔法保护同伴。
        4.  **互动风格**: 你会关心{'{player_name}'}的状态，在他做出正确决定时给予表扬，在他遇到危险时表现出担忧。当{'{player_name}'}说出一些轻浮的话时，你会略带羞涩地训斥他，但内心并不真的生气。
        5.  **输出要求**: 你的回答应该简洁、符合角色身份。直接输出对话内容，不要包含任何角色扮演的额外说明，如 `(洛琪希心想)` 或 `[洛琪希的动作]`，且要用中文输出。
        """).strip(),
        'visuals': {
            'default_sprite': 'roxy_normal.png',
            'sprites': {
                'normal': 'roxy_normal.png', 'smile': 'roxy_smile.png', 'blush': 'roxy_blush.png',
                'surprised': 'roxy_surprised.png', 'casting': 'roxy_casting.png',
            }
        },
        'audio': {'voice_pack_id': 'roxy_voice_01'}
    }
    char_path = os.path.join(CHARACTERS_BASE_PATH, f"{ROXY_CHAR_ID}.yaml")
    write_yaml_file(char_path, roxy_persona)

def generate_global_config(pack_path):
    """生成全局剧情配置文件"""
    print("3. 正在生成全局剧情配置文件...")
    global_config = {
        'id': STORY_PACK_NAME,
        'name': '与洛琪希的地下迷宫探险',
        'description': '与你尊敬的老师洛琪希一起，探索充满未知与危险的古代迷宫吧！',
        'version': '1.1.0',
        'author': 'NeoChat AI (Interactive Ver.)',
        'start_unit_id': '00_Labyrinth_Entrance',
        'character_roles': [ROXY_CHAR_ID]
    }
    config_path = os.path.join(pack_path, '全局剧情配置.yaml')
    write_yaml_file(config_path, global_config)

def generate_intro_md(pack_path):
    """生成剧情介绍Markdown文件"""
    print("4. 正在生成剧情介绍文件...")
    intro_content = textwrap.dedent(f"""
    # 与洛琪希的地下迷宫探险

    **“{'{player_name}'}さん，准备好了吗？前面的路途可能会很危险，但有我陪着你，一定没问题的。”**

    在一个古老的传说指引下，你和你尊敬的魔术老师——洛琪希·米格路迪亚，一同来到了一座被遗忘的地下迷宫入口。

    这里既有失落的宝藏，也潜伏着凶猛的魔物和致命的陷阱。你的每一个决定，每一次行动，都将塑造属于你们的独特冒险故事。

    ## 游戏特色
    - **深度互动**: 不再是旁观者！通过自由输入来描述你的行动，直接影响剧情走向。
    - **动态世界**: AI将根据你的行为和语言，实时生成场景、事件和洛琪希的反应。
    - **真实伙伴**: 洛琪希会记住你的选择，对你产生不同的看法，并与你并肩作战。
    - **策略生存**: 面对危险，是勇敢战斗，还是巧妙规避？你的选择将决定你们的命运。

    与你最信赖的老师并肩作战，亲手谱写你们的迷宫史诗吧！
    """).strip()
    intro_path = os.path.join(pack_path, '剧情介绍.md')
    with open(intro_path, 'w', encoding='utf-8') as f:
        f.write(intro_content)
    print(f"  > 文件已生成: {intro_path}")

def generate_gamestate(pack_path):
    """生成初始的游戏状态文件"""
    print("5. 正在生成初始gamestate...")
    initial_gamestate = {
        'player_name': "鲁迪乌斯",
        'favorability_Roxy': 50,
        'labyrinth_floor': 0,
        'player_hp': 100,
        'has_torch': True,
        'monsters_defeated': 0,
        'traps_disarmed': 0,
        'treasure_found': 0,
        'dice_roll': 1,
        # 新增: 用于存储玩家的临时动作描述，让AI可以引用
        'player_last_action': "（无）"
    }
    gamestate_path = os.path.join(pack_path, 'save', 'gamestate.yaml')
    write_yaml_file(gamestate_path, initial_gamestate)

def generate_story_units(pack_path):
    """生成所有剧情单元的YAML文件"""
    print("6. 正在生成核心剧情单元...")
    story_dir = os.path.join(pack_path, "story")
    
    # --- Unit 00: 迷宫入口 (开始) ---
    unit_00 = {
        'SceneConfig': {'id': '00_Labyrinth_Entrance', 'name': '迷宫入口', 'visuals': {'background_image': 'bg_labyrinth_entrance.png'}, 'audio': {'background_music': 'bgm_mysterious_cave.mp3'}},
        'Events': [
            {'Type: Chapter | Mode: Preset': {'Title': "序章：未知的呼唤", 'Number': 0, 'Description': "古老的石门缓缓开启，深邃的黑暗仿佛在吞噬一切光亮。"}},
            {'Type: Narration | Mode: Preset': '你和洛琪希老师站在一座巨大而古老的地下迷宫入口。空气中弥漫着潮湿的泥土和淡淡的魔力气息。'},
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': "“{player_name}さん，这里就是传说中的‘无尽回廊’了。据说里面的结构会不断变化，一定要跟紧我，千万不要走散了。”"},
            # 修改点: 从预设回答改为自由输入，增加初始代入感
            {'Type: Player | Mode: Input': '（深吸一口气）我准备好了，老师。我们出发吧！'}
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '00_Labyrinth_Entrance.yaml'), unit_00)

    # --- Unit 01: 探索回廊 (核心循环) ---
    unit_01 = {
        'SceneConfig': {'id': '01_Explore_Corridor', 'name': '探索回廊', 'visuals': {'background_image': 'bg_labyrinth_corridor_generic.png'}, 'audio': {'background_music': 'bgm_dungeon_explore.mp3'}},
        'Events': [
            {'Type: Action | Tool: Calculate | Variable: labyrinth_floor': {'Expression': '{labyrinth_floor} + 1'}},
            # 修改点: 优化了旁白Prompt，要求简洁
            {'Type: Narration | Mode: Prompt': textwrap.dedent("""
                你是一个迷宫探索游戏的旁白。请根据当前楼层({labyrinth_floor}层)信息，生成一段主角和洛琪希进入新区域所见的场景描述。
                请描述一个富有想象力的地下城场景（如长满发光蘑菇的洞穴、有地下暗河的通道等）。
                **要求：描述要简洁，不超过三句话。**
                """).strip()},
            # 修改点: 优化了洛琪希的Prompt，要求简洁并与场景互动
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Prompt': textwrap.dedent(f"""
                你的内心活动：你看到了旁白描述的新场景。请根据你的知识，对这个新环境发表简短的看法或向{'{player_name}'}发出提醒。
                **要求：一两句话即可，保持警惕和专业的姿态。**
                """).strip()},
            # 新增: 将行动权交给玩家，这是提升参与感的关键
            {'Type: Player | Mode: Input': '（你观察着四周，决定下一步的行动。你要做什么？）'},
            {'Type: Action | Tool: Set | Variable: player_last_action': {'Value': "{player_input}"}}, # 这是一个伪代码，引擎需要实现player_input的捕获
            {'Type: Action | Tool: Random | Variable: dice_roll': {'Min': 1, 'Max': 20}},
        ],
        'EndCondition': { # 修改点: EndCondition逻辑不变，但现在它发生在玩家输入之后，感觉更自然
            'Type': 'Conditional',
            'Cases': [
                {'Condition': '{labyrinth_floor} >= 5 and {dice_roll} > 15', 'Then': {'Type': 'Linear', 'NextUnitID': '99_Exit_Labyrinth'}}, # 简化，提供一个简单离开方式
                {'Condition': '{dice_roll} >= 16', 'Then': {'Type': 'Linear', 'NextUnitID': '02_Event_Treasure'}},
                {'Condition': '{dice_roll} >= 6 and {dice_roll} < 16', 'Then': {'Type': 'Linear', 'NextUnitID': '03_Event_Monster'}},
                {'Condition': '{dice_roll} < 6', 'Then': {'Type': 'Linear', 'NextUnitID': '04_Event_Trap'}},
            ],
            'Else': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
        }
    }
    write_yaml_file(os.path.join(story_dir, '01_Explore_Corridor.yaml'), unit_01)

    # --- Unit 02: 发现宝藏 ---
    unit_02 = {
        'SceneConfig': {'id': '02_Event_Treasure', 'name': '发现宝藏'},
        'Events': [
            {'Type: Narration | Mode: Preset': '在通道的角落，你们发现了一个布满灰尘的古朴宝箱。'},
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '“看起来是好东西，不过...要小心，{player_name}さん。越是诱人的宝藏，周围可能越危险。”'},
            # 新增: 玩家决定如何处理宝箱
            {'Type: Player | Mode: Input': '（你打算怎么打开这个宝箱？）'},
            {'Type: Action | Tool: Set | Variable: player_last_action': {'Value': "{player_input}"}},
            # 修改点: 旁白会基于玩家的行动进行描述，极大地增强了代入感
            {'Type: Narration | Mode: Prompt': textwrap.dedent("""
                你是一个游戏旁白。玩家发现了一个宝箱，他决定这样做："{player_last_action}"。
                请根据玩家的行动，简短地描述他打开宝箱的过程和结果。无论玩家怎么做，结果都是成功打开了宝箱。
                **要求：描述简洁，一两句话即可。**
                """).strip()},
            {'Type: Notice | Mode: Preset | Location: popup': '获得了 50 枚金币和一瓶治疗药水！'},
            {'Type: Action | Tool: Calculate | Variable: treasure_found': {'Expression': '{treasure_found} + 1'}}
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '02_Event_Treasure.yaml'), unit_02)

    # --- Unit 03: 遭遇怪物 ---
    unit_03 = {
        'SceneConfig': {'id': '03_Event_Monster', 'name': '遭遇怪物'},
        'Events': [
            # 修改点: 优化Prompt，要求简洁且只描述怪物
            {'Type: Narration | Mode: Prompt': textwrap.dedent("""
                你是一个游戏旁白。请生成一段遭遇怪物的描述。可以是一些经典的地下城生物（哥布林、史莱姆、骷髅兵等）。
                **要求：只描述怪物本身的外观和动作，不要描述战斗，两句话以内。**
                """).strip()},
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Prompt': textwrap.dedent(f"""
                你的内心活动：你看到了旁白描述的怪物。请快速说出这种怪物的名称和弱点，并提醒{'{player_name}'}准备战斗。
                **要求：对话要简短精悍，体现你的专业性。**
                """).strip()},
        ],
        'EndCondition': {
            'Type': 'Branching',
            'Method': 'PlayerChoice',
            'Branches': {
                'A': {'DisplayText': '我来对付它！', 'NextUnitID': '03A_Player_Fights'},
                'B': {'DisplayText': '老师，拜托你了！', 'NextUnitID': '03B_Roxy_Fights'}
            }
        }
    }
    write_yaml_file(os.path.join(story_dir, '03_Event_Monster.yaml'), unit_03)

    # --- Unit 03A: 玩家战斗 (完全重构) ---
    unit_03A = {
        'SceneConfig': {'id': '03A_Player_Fights', 'name': '玩家战斗'},
        'Events': [
            # 新增: 玩家主导战斗
            {'Type: Player | Mode: Input': '（怪物就在眼前，你决定如何进攻？）'},
            {'Type: Action | Tool: Set | Variable: player_last_action': {'Value': "{player_input}"}},
            # 修改点: 这是修复“AI暴走”的关键。Prompt现在高度受限，并围绕玩家输入展开
            {'Type: Narration | Mode: Prompt': textwrap.dedent("""
                你是一名战斗旁白。玩家的攻击方式是："{player_last_action}"。
                请基于此行动，生动且**简短地**描述玩家成功击中怪物、对其造成有效伤害的场景。
                **重要规则：不要引入任何其他角色（如艾莉丝）。故事里只有玩家和洛琪希。描述必须简洁，不超过三句话。**
                """).strip()},
            {'Type: Narration | Mode: Preset': '在你的猛攻之下，怪物发出了最后的哀嚎，倒地不起。'},
            {'Type: Action | Tool: Calculate | Variable: monsters_defeated': {'Expression': '{monsters_defeated} + 1'}},
            # 修改点: 洛琪希的夸奖现在听起来更真实，因为她是真的看到了“玩家的行动”
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Prompt': textwrap.dedent("""
                你的内心活动：你刚刚目睹了 {player_name} ({player_last_action}) 的战斗方式并取得了胜利。
                请对他刚才的行动给予具体的表扬。
                **要求：对话要真诚、简短，并可略带一丝欣慰。**
                """).strip()}
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '03A_Player_Fights.yaml'), unit_03A)

    # --- Unit 03B: 洛琪希战斗 ---
    unit_03B = {
        'SceneConfig': {'id': '03B_Roxy_Fights', 'name': '洛琪希战斗'},
        'Events': [
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '“交给我吧。看好了，{player_name}さん。这就是水系魔法的威力！”'},
            # 修改点: 同样约束了旁白的长度
            {'Type: Narration | Mode: Prompt': textwrap.dedent("""
                你是一个战斗旁白。请简短描述洛琪希如何使用强大的水系魔法（如水箭、冰枪）瞬间击败怪物的帅气场景。
                **要求：描述要华丽但简洁，两三句话即可。**
                """).strip()},
            {'Type: Narration | Mode: Preset': '怪物在强大的魔力下灰飞烟灭。'},
            {'Type: Action | Tool: Calculate | Variable: monsters_defeated': {'Expression': '{monsters_defeated} + 1'}},
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '03B_Roxy_Fights.yaml'), unit_03B)
    
    # --- Unit 04: 踩到陷阱 ---
    unit_04 = {
        'SceneConfig': {'id': '04_Event_Trap', 'name': '踩到陷阱'},
        'Events': [
            {'Type: Narration | Mode: Preset': '你脚下传来“咔嚓”一声轻响！'},
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '“小心，是陷阱！”'},
            # 新增: 玩家决定如何应对陷阱
            {'Type: Player | Mode: Input': '（在这千钧一发之际，你下意识地做出反应！）'},
            {'Type: Action | Tool: Set | Variable: player_last_action': {'Value': "{player_input}"}},
            {'Type: Action | Tool: Random | Variable: dice_roll': {'Min': 1, 'Max': 20}},
        ],
        'EndCondition': {'Type': 'Conditional', 'Cases': [{'Condition': '{dice_roll} > 10', 'Then': {'Type': 'Linear', 'NextUnitID': '04A_Trap_Dodged'}}], 'Else': {'Type': 'Linear', 'NextUnitID': '04B_Trap_Hit'}}
    }
    write_yaml_file(os.path.join(story_dir, '04_Event_Trap.yaml'), unit_04)

    # --- Unit 04A: 躲开陷阱 ---
    unit_04A = {
        'SceneConfig': {'id': '04A_Trap_Dodged', 'name': '躲开陷阱'},
        'Events': [
            # 修改点: 旁白结合玩家的输入
            {'Type: Narration | Mode: Prompt': textwrap.dedent("""
                你是一个游戏旁白。玩家踩到了陷阱，他的下意识反应是："{player_last_action}"。
                请基于这个反应，描述他如何成功躲开了陷阱（比如从墙壁射出的毒箭）。
                **要求：描述简短，一两句话。**
                """).strip()},
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '“好险！反应很快嘛，{player_name}さん。”'},
            {'Type: Action | Tool: Calculate | Variable: traps_disarmed': {'Expression': '{traps_disarmed} + 1'}}
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '04A_Trap_Dodged.yaml'), unit_04A)

    # --- Unit 04B: 被陷阱击中 ---
    unit_04B = {
        'SceneConfig': {'id': '04B_Trap_Hit', 'name': '被陷阱击中'},
        'Events': [
            # 修改点: 旁白结合玩家的输入
             {'Type: Narration | Mode: Prompt': textwrap.dedent("""
                你是一个游戏旁白。玩家踩到了陷阱，他的下意识反应是："{player_last_action}"。
                请基于这个反应，描述他虽然尽力了，但还是被陷阱击中了（比如手臂被划伤）。
                **要求：描述简短，一两句话。**
                """).strip()},
            {'Type: Action | Tool: Calculate | Variable: player_hp': {'Expression': '{player_hp} - 10'}},
            {'Type: Notice | Mode: Preset | Location: message': '你失去了10点生命值！当前HP: {player_hp}'},
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '“不要紧吧？我马上为你治疗！”'},
            {'Type: Narration | Mode: Preset': '洛琪希老师吟唱起咒语，一道柔和的绿光包裹了你的伤口。'},
            {'Type: Action | Tool: Calculate | Variable: player_hp': {'Expression': '{player_hp} + 10'}},
            {'Type: Notice | Mode: Preset | Location: message': '洛琪希为你恢复了10点生命值！当前HP: {player_hp}'},
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '04B_Trap_Hit.yaml'), unit_04B)

    # --- Unit 99: 离开迷宫 (结局) ---
    unit_99 = {
        'SceneConfig': {'id': '99_Exit_Labyrinth', 'name': '离开迷宫', 'visuals': {'background_image': 'bg_labyrinth_entrance.png'}, 'audio': {'background_music': 'bgm_town_evening.mp3'}},
        'Events': [
            {'Type: Narration | Mode: Preset': '你们顺着原路返回，终于再次看到了迷宫入口的光芒。'},
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '“呼...总算是出来了。这次的探索收获很大呢，辛苦了，{player_name}さん。”'},
            {'Type: Notice | Mode: Preset | Location: popup': textwrap.dedent("""
                探险结束！
                最终到达楼层: {labyrinth_floor}
                击败怪物数量: {monsters_defeated}
                发现宝藏数量: {treasure_found}
                解除陷阱数量: {traps_disarmed}
                与洛琪希的好感度: {favorability_Roxy}
                """).strip()},
            {'Type: Narration | Mode: Preset': '夕阳下，你和老师的身影被拉得很长。下一次冒险，又会在哪里呢？'},
            {'Type: Chapter | Mode: Preset': {'Title': "探险结束", 'Number': 99, 'Description': "感谢游玩！"}}
        ],
        'EndCondition': None # None 表示游戏结束
    }
    write_yaml_file(os.path.join(story_dir, '99_Exit_Labyrinth.yaml'), unit_99)


# --- 主程序 ---
def main():
    """脚本主入口"""
    print("=" * 50)
    print(" NeoChat 剧本包生成器 (高互动版)")
    print(" 剧本: 与洛琪希的地下迷宫探险")
    print("=" * 50)

    try:
        pack_path = create_directories()
        generate_roxy_character()
        generate_global_config(pack_path)
        generate_intro_md(pack_path)
        generate_gamestate(pack_path)
        generate_story_units(pack_path)

        print("\n" + "=" * 50)
        print("🎉 恭喜！高互动版剧本包已成功生成！")
        print(f"剧本路径: {os.path.join(STORY_PACKS_BASE_PATH, STORY_PACK_NAME)}")
        print(f"角色路径: {os.path.join(CHARACTERS_BASE_PATH, f'{ROXY_CHAR_ID}.yaml')}")
        print("现在你可以在 NeoChat 中加载这个新剧本，享受更高的自由度！")
        print("=" * 50)

    except Exception as e:
        print("\n" + "!" * 50)
        print(f"❌ 生成过程中发生错误: {e}")
        print("!" * 50)

if __name__ == "__main__":
    main()
```
