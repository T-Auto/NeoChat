# NeoChat 项目概览

## 项目结构
```text
NeoChat/
├── Dialogue_history/
│   ├── 2025年05月/
│   │   ├── 17日/
│   │   │   ├── session_20250517_002253.json
│   │   │   ├── session_20250517_003940.json
│   │   │   └── session_20250517_125703.json
│   │   └── 27日/
│   └── 2025年06月/
│       ├── 22日/
│       │   └── session_20250622_123509.json
│       └── 28日/
│           └── session_20250628_180313.json
├── chroma_db_store/
│   ├── c33596e3-7231-4818-8614-d2eb5df21ec9/
│   │   ├── ... (1 more .bin files)
│   │   ├── data_level0.bin
│   │   ├── header.bin
│   │   └── length.bin
│   └── chroma.sqlite3
├── memory-bank/
│   ├── Dialogue_history/
│   │   ├── 2025年02月/
│   │   │   ├── 02日/
│   │   │   │   └── session_20250202_101042.json
│   │   │   ├── 03日/
│   │   │   │   └── session_20250205_161534.json
│   │   │   └── 05日/
│   │   │       └── session_20250205_161534.json
│   │   └── 2025年05月/
│   │       └── 16日/
│   │           └── session_20250516_232754.json
│   ├── activeContext.md
│   ├── productContext.md
│   ├── projectbrief.md
│   ├── systemPatterns.md
│   └── techContext.md
├── run_logs/
│   ├── ... (58 more .log files)
│   ├── AIGalgameDemo_2025-06-28_19-13-34.log
│   ├── AIGalgameDemo_2025-06-28_19-14-45.log
│   └── AIGalgameDemo_2025-06-28_19-17-02.log
├── story/
│   ├── Classroom_01.txt
│   ├── GoHome_03B.txt
│   ├── Library_03A.txt
│   ├── Park_04.txt
│   ├── SchoolGate_02.txt
│   └── character_config.txt
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── config.py
├── logger.py
├── main.py
├── requirements.txt
├── start.bat
├── test.py
└── 设置管理器.exe
```

## 文件内容
### 文件: `README.md`

```markdown
# LingChat AI-Galgame 剧情创作指南

本指南将教你如何使用我们独特的剧情脚本系统，创作出由AI赋予灵魂、充满互动与惊喜的Galgame故事。

你不需要编写任何代码，只需要学会使用我们简单直观的剧情脚本（`.txt`文件），就能构建出完整的游戏世界。

## 第一章：核心理念——编剧的魔杖

传统的Galgame剧情是固定的，玩家的每一次选择都通向一个预设好的分支。而我们的系统引入了**AI驱动**的核心理念，这意味着：

1.  **角色拥有“灵魂”**：AI角色（如“浅川夏帆”）不再是念台词的木偶。她会根据你的**角色设定（Persona）**和**实时对话**，生成真正属于她自己的反应和台词。
2.  **对话充满“不确定性”**：你不需要写死每一句对话。你可以给AI一个“内心活动”或“情境提示”，让她自己组织语言。这使得每一次游玩体验都可能有些微不同，更具真实感。
3.  **剧情分支更加“智能”**：除了玩家的选择，AI角色自己也可以根据与玩家的互动，**自主做出决定**，从而推动剧情走向不同的分支。

你的工作，就是利用手中的“魔杖”——剧情脚本，来引导和塑造这一切。

## 第二章：全局设定——世界的基石

在开始创作具体剧情前，我们需要先定义好世界的基石。这一切都在 `story/character_config.txt` 文件中完成。

### 1. 角色命名 (`AI_Name` & `Player_Name`)

-   `AI_Name`: 你的AI女主角的名字。这个名字会自动替换所有剧情脚本中的 `[AI名]` 占位符。
-   `Player_Name`: 玩家的名字。同理，它会替换 `[玩家名]`。

### 2. AI的核心灵魂 (`AI_Persona`)

这是整个游戏**最重要**的部分。`AI_Persona` 定义了AI角色的性格、背景、价值观和行为模式。它是一切AI生成内容的“最高指令”。

**编写优秀的 `AI_Persona` 的技巧：**

*   **使用第一人称视角**：用“你是XXX”的口吻来写，这能让AI更好地代入角色。
*   **描绘内外反差**：如示例中的“外表文静内向，但内心细腻”，这种反差能让角色更立体。
*   **定义核心关系**：明确她与玩家的关系和她对这段关系的态度（例如：“你非常看重和[玩家名]的关系”）。
*   **设定行为动机**：她为什么会这么做？（例如：“很在意他对你的看法”）。
*   **加入“黄金法则”**：最后一句 **“记住，你不是AI助手，你就是浅川夏帆，请完全代入这个角色进行回应。”** 至关重要，它能有效防止AI“出戏”，避免出现“作为一个AI模型……”之类的回答。

`AI_Persona` 写得越好，AI在游戏中的表现就越稳定、越符合人设。

## 第三章：剧情单元——故事的积木

你的整个故事是由一个个“剧情单元（Unit）”串联起来的。每个单元代表一个独立的场景。让我们来解构一个剧情单元的组成部分。

### 1. 基础信息

-   `UnitID`: 剧情单元的**唯一身份证**。必须是独一无二的，用于剧情跳转。推荐命名方式：`场景_序号`，如 `Classroom_01`。
-   `UnitName`: 场景的名称，会显示给玩家看。

### 2. 场景参数

-   `SceneCG`: 该场景的背景图片。
-   `BGM`: 该场景的背景音乐。
-   `Time`: 故事发生的时间，会自动替换脚本中的 `<时间>` 占位符。

### 3. 剧情事件序列 (`Events`)

这是单元的核心，一个按照顺序执行的事件列表。引擎会从上到下一个个处理。

#### 事件类型 1：旁白 (`Narration`)

用于描述环境、角色动作或内心独白。

-   `Mode: Preset` (预设模式):
    -   **用途**：讲述固定不变的剧情、环境描写。
    -   **写法**：`Content` 后面直接写下你想显示的旁白文字。
    ```yaml
    - Type: Narration
      Mode: Preset
      Content: "夕阳的余晖透过窗户，洒在空无一人的教室里。"
    ```
-   `Mode: Prompt` (提示模式):
    -   **用途**：需要AI根据上下文动态生成的、富有文采的过渡或氛围描写。
    -   **写法**：`Content` 后面写下给AI的**指令**，告诉它要生成一段什么样的旁白。
    ```yaml
    - Type: Narration
      Mode: Prompt
      Content: "你是一个负责剧情衔接的旁白。请描述[玩家名]看着[AI名]转身离去的背影，在<时间>的夜色下，心中涌起的一丝莫名的失落与怅然。"
    ```

#### 事件类型 2：对话 (`Dialogue`)

角色的台词。

-   `Character`: 发言的角色，直接写名字（会被`AI_Name`和`Player_Name`自动替换）。
-   `Mode: Preset` (预设模式):
    -   **用途**：用于推动剧情的关键性台词，或AI角色的开场白。
    -   **写法**：`Content` 后面直接写下固定台词。
    ```yaml
    - Type: Dialogue
      Character: 浅川夏帆
      Mode: Preset
      Content: "呼...终于弄完了。今天值日还真是有点累呢。"
    ```
-   `Mode: Prompt` (提示模式):
    -   **用途**：**这正是AI驱动的核心！** 让AI根据玩家的上一句话和当前情境，生成符合人设的台词。
    -   **写法**：`Content` 后面写下给AI的**“内心活动”指令**。这非常重要，你不是在写台词，而是在描绘角色此刻的心理状态和说话意图。
    ```yaml
    - Type: Dialogue
      Character: 浅川夏帆
      Mode: Prompt
      Content: "这是你的内心活动：听了[玩家名]的回应，你感觉心情放松了一些。但一想到下周就要考试了，又感到一阵焦虑。你看着他，略带担忧地提起考试的话题。"
    ```
    **【关键技巧】**：写`Prompt`模式的对话时，多使用“你感觉……”、“你想要……”、“你试探性地……”、“你鼓起勇气……”等描述心理动机的词语。

#### 事件类型 3：等待玩家输入 (`WaitForPlayerInput`)

这是一个**暂停标志**。当引擎执行到这里，会停下来，等待玩家在终端输入回应。

-   **用途**：**创造对话的节奏感**。通常放在AI的一句台词之后，让玩家可以回应，然后再触发AI的下一句（通常是`Prompt`模式的）台词。这是实现真实互动的关键！
-   `InstructionToPlayer` (可选): 可以给玩家一些提示，告诉他当前的输入可能会有什么影响。

```yaml
# AI说完话
- Type: Dialogue
  Character: 浅川夏帆
  Mode: Preset
  Content: "那...就到这里了。你回家也早点开始复习哦。"

# 停下来，等玩家回应
- Type: WaitForPlayerInput

# AI根据玩家的回应，生成下一句话
- Type: Dialogue
  Character: 浅川夏帆
  Mode: Prompt
  Content: "这是你的内心活动：听了[玩家名]的话，你点点头，但心里还是觉得有点空落落的。你对他挥了挥手，再次叮嘱他路上小心。"
```

## 第四章：剧情的流转——结束与分支

每个单元的结尾都需要一个 `EndCondition`，它决定了接下来会发生什么。

### 1. 线性结局 (`Linear`)

-   **用途**：一本道的剧情，当前单元结束后，直接进入下一个指定单元。
-   **写法**：
```yaml
EndCondition:
  Type: Linear
  NextUnitID: SchoolGate_02 # 直接指定下一个单元的ID
```

### 2. 自由时间 (`FreeTime`)

-   **用途**：提供一个“聊天沙盒”，让玩家可以在特定场景下与AI自由对话，直到触发结束语。
-   **写法**：
```yaml
EndCondition:
  Type: FreeTime
  # 给玩家的提示
  InstructionToPlayer: "你已进入自由聊天时间。点击右上方按钮或输入“时间不早了”可结束对话。"
  # 触发结束的关键词
  ExitPromptInInputBox: "时间不早了，我们开始学习吧！"
  # 结束后跳转的单元ID
  NextUnitID: Park_04
```

### 3. 分支结局 (`Branching`)

-   **用途**：故事的核心玩法！让剧情根据**玩家的选择**或**AI的决定**走向不同的道路。
-   `Method: PlayerChoice` (玩家选择):
    -   **用途**：经典的选项分支。
    -   **写法**：在`Branches`下定义多个选项（A, B, C...），每个选项包含 `DisplayText`（显示给玩家看的选项文本）和 `NextUnitID`（选择后跳转的单元ID）。
    ```yaml
    EndCondition:
      Type: Branching
      Method: PlayerChoice
      Branches:
        A: 
          DisplayText: "上前打个招呼"
          NextUnitID: Park_Encounter_05A
        B: 
          DisplayText: "还是不要打扰她了，悄悄离开"
          NextUnitID: GoHome_Quietly_05B
    ```

-   `Method: AIChoice` (AI决定):
    -   **用途**：**最具革命性的功能！** 让AI角色根据之前的对话，自己做出决定，从而影响剧情走向。
    -   **写法**：这需要两步Prompt。
        1.  `DecisionPromptForAI`: **给AI的决策指令**。这个指令会生成一段AI的台词，这段台词会**显示给玩家**，表明AI做出了什么决定。
        2.  `JudgePromptForSystem`: **给系统的判断指令**。这是一个隐藏的指令，它会分析AI生成的决策台词，并输出一个简单的'A'或'B'来告诉引擎应该走哪个分支。你必须包含 `{AI_LAST_RESPONSE}` 占位符。
    -   **示例剖析**：
    ```yaml
    EndCondition:
      Type: Branching
      Method: AIChoice
      # 1. AI根据这个Prompt，说出自己的决定 (玩家可见)
      DecisionPromptForAI: "这是你的内心活动：现在是时候做出决定了。综合刚才和[玩家名]的对话，以及他对你邀请的回应，明确告诉他，你最终决定'一起去自习室'还是'先各自回家'复习。"
      
      # 2. 系统后台根据AI说的话，进行判断 (玩家不可见)
      JudgePromptForSystem: |
        你是AI-galgame的剧情助手。请根据[浅川夏帆]的最后一句话，判断她是打算 A:去自习室学习 还是 B:在家学习。
        你只能输出'A'或'B'，无需任何其他解释。
        [浅川夏帆]的回答是：{AI_LAST_RESPONSE}
        
      # 3. 根据判断结果(A或B)，跳转到不同剧情
      Branches:
        A: Library_03A
        B: GoHome_03B
    ```

## 第五章：优秀编剧的最佳实践

1.  **节奏为王**：巧妙地混合 `Preset` 和 `Prompt` 模式。用 `Preset` 稳定主线，用 `Prompt` 增添血肉和真实感。
2.  **善用`WaitForPlayerInput`**：不要让AI自言自语说太长。在关键节点插入等待，让玩家参与进来，这是“互动”的核心。
3.  **精准的Prompt**：给AI的指令（无论是对话还是旁白）要清晰、具体。提供“内心活动”和“情感状态”远比直接命令它“说一句话”效果好。
4.  **为AI决策铺垫**：在使用 `AIChoice` 前，确保前面的对话已经为AI提供了足够的信息来做判断。例如，在邀请玩家一起学习前，先问问玩家的计划。
5.  **画出你的故事树**：在开始写之前，可以简单画一个流程图，标明每个`UnitID`以及它们之间的跳转关系，这会让你思路更清晰。
6.  **亲自测试！**：由于AI的存在，你写的脚本可能会产生意想不到的效果。一定要亲自运行和测试你的剧情，看看AI的反应是否符合预期，并根据测试结果微调你的`Prompt`。
```

### 文件: `readme.md`

```markdown
# LingChat AI-Galgame 剧情创作指南

本指南将教你如何使用我们独特的剧情脚本系统，创作出由AI赋予灵魂、充满互动与惊喜的Galgame故事。

你不需要编写任何代码，只需要学会使用我们简单直观的剧情脚本（`.txt`文件），就能构建出完整的游戏世界。

## 第一章：核心理念——编剧的魔杖

传统的Galgame剧情是固定的，玩家的每一次选择都通向一个预设好的分支。而我们的系统引入了**AI驱动**的核心理念，这意味着：

1.  **角色拥有“灵魂”**：AI角色（如“浅川夏帆”）不再是念台词的木偶。她会根据你的**角色设定（Persona）**和**实时对话**，生成真正属于她自己的反应和台词。
2.  **对话充满“不确定性”**：你不需要写死每一句对话。你可以给AI一个“内心活动”或“情境提示”，让她自己组织语言。这使得每一次游玩体验都可能有些微不同，更具真实感。
3.  **剧情分支更加“智能”**：除了玩家的选择，AI角色自己也可以根据与玩家的互动，**自主做出决定**，从而推动剧情走向不同的分支。

你的工作，就是利用手中的“魔杖”——剧情脚本，来引导和塑造这一切。

## 第二章：全局设定——世界的基石

在开始创作具体剧情前，我们需要先定义好世界的基石。这一切都在 `story/character_config.txt` 文件中完成。

### 1. 角色命名 (`AI_Name` & `Player_Name`)

-   `AI_Name`: 你的AI女主角的名字。这个名字会自动替换所有剧情脚本中的 `[AI名]` 占位符。
-   `Player_Name`: 玩家的名字。同理，它会替换 `[玩家名]`。

### 2. AI的核心灵魂 (`AI_Persona`)

这是整个游戏**最重要**的部分。`AI_Persona` 定义了AI角色的性格、背景、价值观和行为模式。它是一切AI生成内容的“最高指令”。

**编写优秀的 `AI_Persona` 的技巧：**

*   **使用第一人称视角**：用“你是XXX”的口吻来写，这能让AI更好地代入角色。
*   **描绘内外反差**：如示例中的“外表文静内向，但内心细腻”，这种反差能让角色更立体。
*   **定义核心关系**：明确她与玩家的关系和她对这段关系的态度（例如：“你非常看重和[玩家名]的关系”）。
*   **设定行为动机**：她为什么会这么做？（例如：“很在意他对你的看法”）。
*   **加入“黄金法则”**：最后一句 **“记住，你不是AI助手，你就是浅川夏帆，请完全代入这个角色进行回应。”** 至关重要，它能有效防止AI“出戏”，避免出现“作为一个AI模型……”之类的回答。

`AI_Persona` 写得越好，AI在游戏中的表现就越稳定、越符合人设。

## 第三章：剧情单元——故事的积木

你的整个故事是由一个个“剧情单元（Unit）”串联起来的。每个单元代表一个独立的场景。让我们来解构一个剧情单元的组成部分。

### 1. 基础信息

-   `UnitID`: 剧情单元的**唯一身份证**。必须是独一无二的，用于剧情跳转。推荐命名方式：`场景_序号`，如 `Classroom_01`。
-   `UnitName`: 场景的名称，会显示给玩家看。

### 2. 场景参数

-   `SceneCG`: 该场景的背景图片。
-   `BGM`: 该场景的背景音乐。
-   `Time`: 故事发生的时间，会自动替换脚本中的 `<时间>` 占位符。

### 3. 剧情事件序列 (`Events`)

这是单元的核心，一个按照顺序执行的事件列表。引擎会从上到下一个个处理。

#### 事件类型 1：旁白 (`Narration`)

用于描述环境、角色动作或内心独白。

-   `Mode: Preset` (预设模式):
    -   **用途**：讲述固定不变的剧情、环境描写。
    -   **写法**：`Content` 后面直接写下你想显示的旁白文字。
    ```yaml
    - Type: Narration
      Mode: Preset
      Content: "夕阳的余晖透过窗户，洒在空无一人的教室里。"
    ```
-   `Mode: Prompt` (提示模式):
    -   **用途**：需要AI根据上下文动态生成的、富有文采的过渡或氛围描写。
    -   **写法**：`Content` 后面写下给AI的**指令**，告诉它要生成一段什么样的旁白。
    ```yaml
    - Type: Narration
      Mode: Prompt
      Content: "你是一个负责剧情衔接的旁白。请描述[玩家名]看着[AI名]转身离去的背影，在<时间>的夜色下，心中涌起的一丝莫名的失落与怅然。"
    ```

#### 事件类型 2：对话 (`Dialogue`)

角色的台词。

-   `Character`: 发言的角色，直接写名字（会被`AI_Name`和`Player_Name`自动替换）。
-   `Mode: Preset` (预设模式):
    -   **用途**：用于推动剧情的关键性台词，或AI角色的开场白。
    -   **写法**：`Content` 后面直接写下固定台词。
    ```yaml
    - Type: Dialogue
      Character: 浅川夏帆
      Mode: Preset
      Content: "呼...终于弄完了。今天值日还真是有点累呢。"
    ```
-   `Mode: Prompt` (提示模式):
    -   **用途**：**这正是AI驱动的核心！** 让AI根据玩家的上一句话和当前情境，生成符合人设的台词。
    -   **写法**：`Content` 后面写下给AI的**“内心活动”指令**。这非常重要，你不是在写台词，而是在描绘角色此刻的心理状态和说话意图。
    ```yaml
    - Type: Dialogue
      Character: 浅川夏帆
      Mode: Prompt
      Content: "这是你的内心活动：听了[玩家名]的回应，你感觉心情放松了一些。但一想到下周就要考试了，又感到一阵焦虑。你看着他，略带担忧地提起考试的话题。"
    ```
    **【关键技巧】**：写`Prompt`模式的对话时，多使用“你感觉……”、“你想要……”、“你试探性地……”、“你鼓起勇气……”等描述心理动机的词语。

#### 事件类型 3：等待玩家输入 (`WaitForPlayerInput`)

这是一个**暂停标志**。当引擎执行到这里，会停下来，等待玩家在终端输入回应。

-   **用途**：**创造对话的节奏感**。通常放在AI的一句台词之后，让玩家可以回应，然后再触发AI的下一句（通常是`Prompt`模式的）台词。这是实现真实互动的关键！
-   `InstructionToPlayer` (可选): 可以给玩家一些提示，告诉他当前的输入可能会有什么影响。

```yaml
# AI说完话
- Type: Dialogue
  Character: 浅川夏帆
  Mode: Preset
  Content: "那...就到这里了。你回家也早点开始复习哦。"

# 停下来，等玩家回应
- Type: WaitForPlayerInput

# AI根据玩家的回应，生成下一句话
- Type: Dialogue
  Character: 浅川夏帆
  Mode: Prompt
  Content: "这是你的内心活动：听了[玩家名]的话，你点点头，但心里还是觉得有点空落落的。你对他挥了挥手，再次叮嘱他路上小心。"
```

## 第四章：剧情的流转——结束与分支

每个单元的结尾都需要一个 `EndCondition`，它决定了接下来会发生什么。

### 1. 线性结局 (`Linear`)

-   **用途**：一本道的剧情，当前单元结束后，直接进入下一个指定单元。
-   **写法**：
```yaml
EndCondition:
  Type: Linear
  NextUnitID: SchoolGate_02 # 直接指定下一个单元的ID
```

### 2. 自由时间 (`FreeTime`)

-   **用途**：提供一个“聊天沙盒”，让玩家可以在特定场景下与AI自由对话，直到触发结束语。
-   **写法**：
```yaml
EndCondition:
  Type: FreeTime
  # 给玩家的提示
  InstructionToPlayer: "你已进入自由聊天时间。点击右上方按钮或输入“时间不早了”可结束对话。"
  # 触发结束的关键词
  ExitPromptInInputBox: "时间不早了，我们开始学习吧！"
  # 结束后跳转的单元ID
  NextUnitID: Park_04
```

### 3. 分支结局 (`Branching`)

-   **用途**：故事的核心玩法！让剧情根据**玩家的选择**或**AI的决定**走向不同的道路。
-   `Method: PlayerChoice` (玩家选择):
    -   **用途**：经典的选项分支。
    -   **写法**：在`Branches`下定义多个选项（A, B, C...），每个选项包含 `DisplayText`（显示给玩家看的选项文本）和 `NextUnitID`（选择后跳转的单元ID）。
    ```yaml
    EndCondition:
      Type: Branching
      Method: PlayerChoice
      Branches:
        A: 
          DisplayText: "上前打个招呼"
          NextUnitID: Park_Encounter_05A
        B: 
          DisplayText: "还是不要打扰她了，悄悄离开"
          NextUnitID: GoHome_Quietly_05B
    ```

-   `Method: AIChoice` (AI决定):
    -   **用途**：**最具革命性的功能！** 让AI角色根据之前的对话，自己做出决定，从而影响剧情走向。
    -   **写法**：这需要两步Prompt。
        1.  `DecisionPromptForAI`: **给AI的决策指令**。这个指令会生成一段AI的台词，这段台词会**显示给玩家**，表明AI做出了什么决定。
        2.  `JudgePromptForSystem`: **给系统的判断指令**。这是一个隐藏的指令，它会分析AI生成的决策台词，并输出一个简单的'A'或'B'来告诉引擎应该走哪个分支。你必须包含 `{AI_LAST_RESPONSE}` 占位符。
    -   **示例剖析**：
    ```yaml
    EndCondition:
      Type: Branching
      Method: AIChoice
      # 1. AI根据这个Prompt，说出自己的决定 (玩家可见)
      DecisionPromptForAI: "这是你的内心活动：现在是时候做出决定了。综合刚才和[玩家名]的对话，以及他对你邀请的回应，明确告诉他，你最终决定'一起去自习室'还是'先各自回家'复习。"
      
      # 2. 系统后台根据AI说的话，进行判断 (玩家不可见)
      JudgePromptForSystem: |
        你是AI-galgame的剧情助手。请根据[浅川夏帆]的最后一句话，判断她是打算 A:去自习室学习 还是 B:在家学习。
        你只能输出'A'或'B'，无需任何其他解释。
        [浅川夏帆]的回答是：{AI_LAST_RESPONSE}
        
      # 3. 根据判断结果(A或B)，跳转到不同剧情
      Branches:
        A: Library_03A
        B: GoHome_03B
    ```

## 第五章：优秀编剧的最佳实践

1.  **节奏为王**：巧妙地混合 `Preset` 和 `Prompt` 模式。用 `Preset` 稳定主线，用 `Prompt` 增添血肉和真实感。
2.  **善用`WaitForPlayerInput`**：不要让AI自言自语说太长。在关键节点插入等待，让玩家参与进来，这是“互动”的核心。
3.  **精准的Prompt**：给AI的指令（无论是对话还是旁白）要清晰、具体。提供“内心活动”和“情感状态”远比直接命令它“说一句话”效果好。
4.  **为AI决策铺垫**：在使用 `AIChoice` 前，确保前面的对话已经为AI提供了足够的信息来做判断。例如，在邀请玩家一起学习前，先问问玩家的计划。
5.  **画出你的故事树**：在开始写之前，可以简单画一个流程图，标明每个`UnitID`以及它们之间的跳转关系，这会让你思路更清晰。
6.  **亲自测试！**：由于AI的存在，你写的脚本可能会产生意想不到的效果。一定要亲自运行和测试你的剧情，看看AI的反应是否符合预期，并根据测试结果微调你的`Prompt`。
```

### 文件: `config.py`

```python
import os
from dotenv import load_dotenv
load_dotenv()

# AI配置
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.deepseek.com/chat/completions"
MODEL_NAME = "deepseek-chat"
AI_NAME = os.getenv("AI_NAME")
MAX_TOKENS = 4096                         # DeepSeek API允许的最大输出Token数，根据模型调整
TEMPERATURE = 0.7                         # 生成文本的温度值，0.1-1.0，越高越随机。默认为0.7
API_TIMEOUT_SECONDS = 180                 # API请求的超时时间 (秒) (建议)

# 系统提示词(System Prompt)
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")
# print(SYSTEM_PROMPT)

# 会话与历史记录
HISTORY_BASE_PATH = "Dialogue_history"    # 聊天记录保存路径
CHROMA_DB_PATH = "./chroma_db_store"      # RAG缓存路径，ChromaDB持久化存储路径。可安全删除，删除后会根据Json聊天记录重新生成，但更耗时。

# 调试与日志
DEBUG_MODE = False                         #开启/关闭开发者模式。设置为True/False将开关Debug日志。

# RAG (Retrieval Augmented Generation) 设置
USE_RAG = True                            # 是否启用RAG功能
MAX_CONTEXT_MESSAGES_SLIDING_WINDOW = 20  # 限制本轮次对话最近发送的上下文消息数量，以防token爆炸
RAG_RETRIEVAL_COUNT = 3                   # 配置RAG搜索多少条聊天记录
RAG_CONTEXT_M_BEFORE = 2                  # 把检索到的聊天记录之前的m条消息发送给llm
RAG_CONTEXT_N_AFTER = 2                   # 把检索到的聊天记录之后的n条消息发送给llm
RAG_CANDIDATE_MULTIPLIER = 3              # 代码稳定性设置。为获取RAG_RETRIEVAL_COUNT个块，实际从ChromaDB查询的候选倍数，不建议改动

RAG_PROMPT_PREFIX = (                     # RAG 内容的前缀提示
    "--- 以下是根据你的历史记忆检索到的相关对话片段，请参考它们来回答当前问题。这些是历史信息，不是当前对话的一部分： ---"
)
RAG_PROMPT_SUFFIX = (
    "--- 以上是历史记忆检索到的内容。请注意，这些内容用于提供背景信息，你不需要直接回应它们，而是基于它们和下面的当前对话来生成回复。 ---"
)

# SentenceTransformer 嵌入模型进度条设置。如果你希望在DEBUG_MODE=False时也显示SentenceTransformer的进度条，可以设置为True
SHOW_EMBEDDING_PROGRESS = DEBUG_MODE
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
import sys
import config
from logger import (
    initialize_logger,
    start_loading_animation,
    stop_loading_animation,
    TermColors,
    log_debug,
    log_info,
    log_warning,
    log_error,
    log_info_color,
    log_warning_color,
    log_error_color
)
# 早期日志初始化，用于在python库导入期间显示动画
_early_init_app_name = getattr(config, 'AI_NAME', "App") + "_PreLoad"
initialize_logger(
    config_debug_mode=getattr(config, 'DEBUG_MODE', False),
    app_name=_early_init_app_name,
    show_timestamp=False  # 早期加载信息可以简洁些
)
log_debug("您目前处于开发者模式中，终端将会显示大量的灰色DEBUG日志，若要获得更好的使用体验，关闭开发者模式")
log_debug("正在加载Python依赖库，此过程可能较慢。")
start_loading_animation(
    message=f"{TermColors.CYAN}{config.AI_NAME}正在试图起床{TermColors.RESET}",
    animation_style_key='dots'
)

# 开始导入可能耗时的模块
import requests
import json
import os
from datetime import datetime, timezone
import uuid
import torch
import re

_sentence_transformer_imported_ok = True
_chromadb_imported_ok = True

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    _sentence_transformer_imported_ok = False
    if hasattr(config, 'USE_RAG') and config.USE_RAG:
        sys.stderr.write(
            f"{TermColors.RED}错误: 'sentence-transformers' 模块未找到，但 RAG 功能已启用。\n"
            f"请安装: pip install sentence-transformers{TermColors.RESET}\n")
        sys.stderr.flush()


    class SentenceTransformer:
        def __init__(self, *args, **kwargs): pass

        def encode(self, *args, **kwargs): raise NotImplementedError("SentenceTransformer is not available.")

try:
    import chromadb
except ImportError:
    _chromadb_imported_ok = False
    if hasattr(config, 'USE_RAG') and config.USE_RAG:
        sys.stderr.write(
            f"{TermColors.RED}错误: 'chromadb' 模块未找到，但 RAG 功能已启用。\n"
            f"请安装: pip install chromadb{TermColors.RESET}\n")
        sys.stderr.flush()

    class chromadb:
        class PersistentClient:
            def __init__(self, *args, **kwargs): pass

            def get_or_create_collection(self, *args, **kwargs): raise NotImplementedError(
                "chromadb is not available.")

        def get_collection(self, *args, **kwargs): raise NotImplementedError(
            "chromadb is not available.")

_early_load_successful = True
_early_load_message = "核心模块加载完成。"

if hasattr(config, 'USE_RAG') and config.USE_RAG:
    if not _sentence_transformer_imported_ok or not _chromadb_imported_ok:
        _early_load_successful = False
        missing_modules = []
        if not _sentence_transformer_imported_ok: missing_modules.append("'sentence-transformers'")
        if not _chromadb_imported_ok: missing_modules.append("'chromadb'")
        _early_load_message = f"核心RAG模块 ({', '.join(missing_modules)}) 加载失败。RAG功能可能受限。"

stop_loading_animation(success=_early_load_successful)

# --- 历史记录管理 ---
def get_history_filepath():
    now = datetime.now()
    year_month_path = os.path.join(config.HISTORY_BASE_PATH, now.strftime("%Y年%m月"))
    day_path = os.path.join(year_month_path, now.strftime("%d日"))
    os.makedirs(day_path, exist_ok=True)
    session_start_time_str = now.strftime("%Y%m%d_%H%M%S")
    return os.path.join(day_path, f"session_{session_start_time_str}.json")

def save_session_history(session_messages, filepath):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(session_messages, f, ensure_ascii=False, indent=4)
        log_debug(f"会话历史已保存到: {filepath}")
    except IOError as e:
        log_error_color(f"保存历史记录失败: {e}")
        log_debug(f"IOError saving history: {e}", exc_info=True)

def parse_session_time_from_filename(filename):
    match = re.search(r"session_(\d{8}_\d{6})\.json", filename)
    if match:
        try:
            dt_obj = datetime.strptime(match.group(1), "%Y%m%d_%H%M%S")
            return dt_obj.strftime("%Y年%m月%d日 %H:%M")
        except ValueError:
            log_debug(f"无法从文件名 {filename} 解析有效日期时间。")
            return "未知时间"
    return "未知时间"

def load_all_historical_data():
    all_messages_flat = []
    historical_sessions_map = {}

    if not os.path.exists(config.HISTORY_BASE_PATH):
        log_warning(f"历史记录基础路径 {config.HISTORY_BASE_PATH} 不存在。未加载任何历史。")
        return all_messages_flat, historical_sessions_map

    log_debug(f"开始从 {config.HISTORY_BASE_PATH} 加载历史对话数据...")
    loaded_files_count = 0
    total_messages_loaded = 0
    for root, _, files in os.walk(config.HISTORY_BASE_PATH):
        sorted_files = sorted([f for f in files if f.endswith(".json")])
        for filename in sorted_files:
            filepath = os.path.join(root, filename)
            session_time_str = parse_session_time_from_filename(filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    session_data = json.load(f)
                    if isinstance(session_data, list) and session_data:
                        historical_sessions_map[filename] = []
                        for idx, msg in enumerate(session_data):
                            msg_copy_flat = msg.copy()
                            msg_copy_flat['_source_file'] = filename
                            msg_copy_flat['_original_idx'] = idx
                            msg_copy_flat['_session_timestamp_str'] = session_time_str
                            all_messages_flat.append(msg_copy_flat)

                            msg_copy_map = msg.copy()
                            msg_copy_map['_source_file'] = filename
                            msg_copy_map['_original_idx'] = idx
                            msg_copy_map['_session_timestamp_str'] = session_time_str
                            historical_sessions_map[filename].append(msg_copy_map)
                        loaded_files_count += 1
                        total_messages_loaded += len(session_data)
            except (json.JSONDecodeError, IOError) as e:
                log_warning_color(f"加载历史文件 {filepath} 失败: {e}")
                log_debug(f"Failed to load history file {filepath}: {e}", exc_info=True)

    if loaded_files_count > 0:
        log_debug(f"成功从 {loaded_files_count} 个文件中加载了 {total_messages_loaded} 条历史消息。")
    else:
        log_warning_color("未找到或加载任何有效的历史会话文件。请检查Dialogue_history/文件是否正确存放，若您是初次使用本项目，请忽略此警报")
    log_debug(f"共映射 {len(historical_sessions_map)} 个会话。")
    return all_messages_flat, historical_sessions_map

# --- RAG 相关 ---
embedding_model = None
chroma_client = None
chroma_collection = None
CHROMA_COLLECTION_NAME = "chat_history_collection_v4"
EMBEDDING_MODEL_NAME = 'all-MiniLM-L6-v2'

def initialize_rag_components():
    global embedding_model, chroma_client, chroma_collection, _sentence_transformer_imported_ok, _chromadb_imported_ok
    if not config.USE_RAG:
        log_info("RAG功能已禁用 (根据配置)。")
        return False

    if not _sentence_transformer_imported_ok:
        log_error_color("RAG组件初始化失败: SentenceTransformer 模块未能成功导入。")
        return False
    if not _chromadb_imported_ok:
        log_error_color("RAG组件初始化失败: ChromaDB 模块未能成功导入。")
        return False

    log_debug("开始初始化RAG组件...")
    try:
        log_debug(f"RAG: 初始化Sentence Transformer模型: {EMBEDDING_MODEL_NAME}")
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME, device=device)
        log_debug(f"RAG: Sentence Transformer模型 ({EMBEDDING_MODEL_NAME}) 加载成功 。当前使用 {device})进行RAG向量库匹配的推理。")

        chroma_db_path = getattr(config, 'CHROMA_DB_PATH', './chroma_db_store_v2')
        log_debug(f"RAG: 初始化ChromaDB客户端 (记忆库将存储在 '{chroma_db_path}').")
        chroma_client = chromadb.PersistentClient(path=chroma_db_path)
        log_debug(f"RAG: ChromaDB客户端初始化成功 (数据路径: {chroma_db_path})。")

        log_debug(f"RAG: 获取或创建ChromaDB集合: {CHROMA_COLLECTION_NAME}")
        chroma_collection = chroma_client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )
        log_debug(
            f"RAG: ChromaDB集合 '{CHROMA_COLLECTION_NAME}' 已就绪。当前包含 {chroma_collection.count()} 条目。")
        return True
    except Exception as e:
        log_error_color(f"RAG组件初始化过程中发生错误: {e}")
        log_debug(f"RAG Initialization Error during component setup: {e}", exc_info=True)
        embedding_model = None
        chroma_client = None
        chroma_collection = None
        return False


def add_messages_to_rag_index(messages_with_metadata):
    global embedding_model, chroma_collection
    if not config.USE_RAG or not embedding_model or not chroma_collection:
        log_debug("RAG: 组件未初始化或RAG已禁用，跳过索引。")
        return

    if not messages_with_metadata:
        log_info("RAG: 无消息可供索引。")
        return

    log_debug(f"RAG: 准备为 {len(messages_with_metadata)} 条消息建立索引...")
    documents, metadatas, ids = [], [], []

    for msg in messages_with_metadata:
        content, role = msg.get('content'), msg.get('role')
        source_file, original_idx = msg.get('_source_file'), msg.get('_original_idx')

        if not all([content, isinstance(content, str), role, source_file is not None, original_idx is not None]):
            log_debug(f"RAG: 跳过无效消息进行索引 (字段缺失): {str(msg)[:100]}...")
            continue

        message_id_str = f"{source_file}_{original_idx}_{role}_{content[:100]}"
        message_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, message_id_str))
        documents.append(content)
        metadatas.append({"role": role, "source_file": source_file, "original_idx": original_idx})
        ids.append(message_id)

    if not documents:
        log_warning_color("RAG: 筛选后无有效文档可供索引。")
        return

    log_debug(f"RAG: 正在为 {len(documents)} 个文档生成嵌入向量...")
    embeddings = embedding_model.encode(documents).tolist()
    log_debug(f"RAG: 嵌入向量生成完毕。Shape: ({len(embeddings)}, {len(embeddings[0]) if embeddings else 0})")

    try:
        batch_size = 500
        for i in range(0, len(ids), batch_size):
            batch_ids, batch_embeddings = ids[i:i + batch_size], embeddings[i:i + batch_size]
            batch_documents, batch_metadatas = documents[i:i + batch_size], metadatas[i:i + batch_size]
            chroma_collection.upsert(ids=batch_ids, embeddings=batch_embeddings, documents=batch_documents,
                                     metadatas=batch_metadatas)
            log_debug(f"RAG: Upserted batch {i // batch_size + 1} ({len(batch_ids)} documents).")
        log_debug(f"RAG: 成功向ChromaDB中添加/更新了 {len(ids)} 个文档。")
        log_debug(f"RAG: 索引库 '{CHROMA_COLLECTION_NAME}' 当前总条目: {chroma_collection.count()}")
    except Exception as e:
        log_error_color(f"RAG: 向ChromaDB中Upsert文档时出错: {e}")
        log_debug(f"ChromaDB Upsert Error: {e}", exc_info=True)


def get_rag_messages_chroma(query_text, historical_sessions_map):
    global embedding_model, chroma_collection
    if not config.USE_RAG or not embedding_model or not chroma_collection:
        log_warning_color("RAG: 组件未初始化或RAG已禁用，跳过检索。")
        return []
    if not query_text:
        log_warning_color("RAG: 查询文本为空，跳过RAG检索。")
        return []
    if chroma_collection.count() == 0:
        log_warning_color("RAG: ChromaDB集合为空，跳过RAG检索。")
        return []

    num_candidates_to_fetch = config.RAG_RETRIEVAL_COUNT * config.RAG_CANDIDATE_MULTIPLIER
    num_candidates_to_fetch = min(num_candidates_to_fetch, chroma_collection.count())

    log_info_color(f"RAG: 正在为查询 \"{query_text[:50]}...\" 检索最多 {num_candidates_to_fetch} 个候选片段...",
                   TermColors.BLUE)
    query_embedding = embedding_model.encode([query_text], show_progress_bar=False)[0].tolist()

    try:
        results = chroma_collection.query(
            query_embeddings=[query_embedding],
            n_results=num_candidates_to_fetch,
            include=["documents", "metadatas", "distances"]
        )
    except Exception as e:
        log_error_color(f"RAG 查询ChromaDB失败: {e}")
        log_debug(f"ChromaDB Query Error: {e}", exc_info=True)
        return []

    final_rag_messages, used_chroma_doc_ids, added_message_contents_to_llm = [], set(), set()
    retrieved_blocks_count = 0

    if results and results.get('ids') and results['ids'][0]:
        log_debug(f"RAG: ChromaDB返回 {len(results['ids'][0])} 个候选结果。")
        for i in range(len(results['ids'][0])):
            if retrieved_blocks_count >= config.RAG_RETRIEVAL_COUNT:
                log_debug(f"RAG: 已达到期望的 {config.RAG_RETRIEVAL_COUNT} 个独立上下文块。停止处理候选。")
                break
            try:
                core_doc_id, core_doc_content = results['ids'][0][i], results['documents'][0][i]
                metadata, distance = results['metadatas'][0][i], results['distances'][0][i]
            except (IndexError, TypeError, KeyError) as e:
                log_warning(f"RAG: ChromaDB结果索引 {i} 处数据不完整或格式错误。跳过。详细: {e}")
                continue

            if core_doc_id in used_chroma_doc_ids or core_doc_content == query_text:
                log_debug(f"RAG: 跳过已使用或与查询相同的文档 ID {core_doc_id}.")
                continue

            source_file, original_idx = metadata.get("source_file"), metadata.get("original_idx")
            if source_file not in historical_sessions_map or not isinstance(original_idx, int):
                log_warning(f"RAG: 文档 {core_doc_id} 元数据不完整或会话未在Map中找到。跳过。")
                continue

            current_session_messages = historical_sessions_map[source_file]
            if not (0 <= original_idx < len(current_session_messages)):
                log_warning(f"RAG: 原始索引 {original_idx} 超出 '{source_file}' 会话边界。跳过。")
                continue

            start_idx = max(0, original_idx - config.RAG_CONTEXT_M_BEFORE)
            end_idx = min(len(current_session_messages), original_idx + config.RAG_CONTEXT_N_AFTER + 1)

            context_block_for_llm, context_block_display_info, potential_block_messages = [], [], []
            for j in range(start_idx, end_idx):
                msg_obj = current_session_messages[j]
                msg_content, msg_role = msg_obj.get("content"), msg_obj.get("role", "unknown")
                session_time_str = msg_obj.get("_session_timestamp_str", "未知时间")

                if msg_content and msg_content not in added_message_contents_to_llm:
                    contextualized_content = f"[历史对话片段 - {session_time_str}] {msg_content}"
                    potential_block_messages.append({"role": msg_role, "content": contextualized_content})
                    is_core = " (核心检索)" if j == original_idx else ""
                    context_block_display_info.append(
                        f"  - ({session_time_str}) [{msg_role}]{is_core}: \"{msg_content[:50]}...\"")

            if potential_block_messages:
                context_block_for_llm.extend(potential_block_messages)
                for msg in potential_block_messages: added_message_contents_to_llm.add(msg['content'])
                used_chroma_doc_ids.add(core_doc_id)
                retrieved_blocks_count += 1
                final_rag_messages.extend(context_block_for_llm)
                log_info_color(
                    f"\nRAG 系统检索到历史对话片段 (核心距离: {distance:.4f}, 源: {source_file}, 核心索引: {original_idx}):",
                    # MODIFIED
                    TermColors.MAGENTA)
                for line in context_block_display_info:
                    log_info_color(f"\n{line}", TermColors.MAGENTA)  # MODIFIED
                log_debug(f"RAG: 添加上下文块 (ID {core_doc_id}). LLM的RAG消息总数: {len(final_rag_messages)}")
            else:
                log_debug(f"RAG: 核心文档ID {core_doc_id} 的上下文块为空或所有消息已去重。")

    if not final_rag_messages:
        log_info_color("RAG 系统: 未在历史记录中找到与当前问题相关的、非重复的消息。", TermColors.YELLOW)
    else:
        log_info_color(
            f"RAG: 为LLM准备了 {len(final_rag_messages)} 条消息，来自 {retrieved_blocks_count} 个不同的RAG上下文块。",
            TermColors.GREEN)
    return final_rag_messages

# --- DeepSeek API 调用 ---
def chat_with_deepseek(messages_payload):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {config.API_KEY}"}
    payload = {
        "model": config.MODEL_NAME, "messages": messages_payload, "stream": True,
        "max_tokens": config.MAX_TOKENS, "temperature": config.TEMPERATURE
    }

    if config.DEBUG_MODE:
        log_debug("--- 发送给 DeepSeek API 的 Payload (内容已截断) ---")
        debug_payload_display = json.loads(json.dumps(payload))
        for msg in debug_payload_display.get("messages", []):
            if 'content' in msg and isinstance(msg['content'], str):
                msg['content'] = msg['content'][:150] + ("..." if len(msg['content']) > 150 else "")
        formatted_payload_str = json.dumps(debug_payload_display, ensure_ascii=False, indent=2)
        for line in formatted_payload_str.splitlines(): log_debug(line)
        log_debug("--- Payload 结束 ---")

    assistant_full_response = ""
    api_call_succeeded = False
    animation_stopped_internally = False

    try:
        log_info_color(f"{config.AI_NAME}正在连接DeepSeek ({config.MODEL_NAME})... 请稍候。", TermColors.BLUE)
        start_loading_animation(
            message=f"{TermColors.LIGHT_BLUE}{config.AI_NAME}正在发呆{TermColors.RESET}",
            animation_style_key='moon',
            animation_color=TermColors.LIGHT_BLUE
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
                        log_debug("API Stream: [DONE] 标记已收到。")
                        break
                    try:
                        data = json.loads(json_data_str)
                        content_piece = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if content_piece:
                            if not first_chunk_received:
                                stop_loading_animation(success=True)
                                animation_stopped_internally = True
                                print(f"{TermColors.CYAN}{config.AI_NAME}: {TermColors.RESET}", end="", flush=True)
                                first_chunk_received = True
                            sys.stdout.write(f"{TermColors.CYAN}{content_piece}{TermColors.RESET}")
                            sys.stdout.flush()
                            assistant_full_response += content_piece
                    except (json.JSONDecodeError, IndexError):
                        log_warning(f"API Stream: 解码或索引错误，数据块: {json_data_str}")

        if first_chunk_received:
            print();
            api_call_succeeded = True
        elif response.ok:
            log_info("API 响应流结束，但未返回任何文本内容。");
            api_call_succeeded = True

    except requests.exceptions.HTTPError as e_http:
        log_error_color(f"\nAPI请求HTTP错误: {e_http} - {e_http.response.status_code} {e_http.response.reason}")
        try:
            log_error_color(f"错误详情: {json.dumps(e_http.response.json(), ensure_ascii=False, indent=2)}")
        except ValueError:
            log_error_color(f"错误响应体 (非JSON): {e_http.response.text}")
        log_debug(f"API HTTPError: {e_http}", exc_info=True)
    except requests.exceptions.Timeout:
        log_error_color(f"\nAPI请求超时 (超过 {config.API_TIMEOUT_SECONDS} 秒)。")
        log_debug("API Request Timeout", exc_info=True)
    except requests.exceptions.RequestException as e_req:
        log_error_color(f"\nAPI请求失败: {e_req}")
        log_debug(f"API Request Exception: {e_req}", exc_info=True)
    except Exception as e_unknown:
        log_error_color(f"\n处理API响应时发生未知错误: {e_unknown}")
        log_debug(f"Unknown error during API response processing: {e_unknown}", exc_info=True)
    finally:
        if not animation_stopped_internally:
            final_msg = None
            if not api_call_succeeded:
                final_msg = "与API的通信出现问题"
            elif not assistant_full_response and api_call_succeeded:
                final_msg = "API已响应 (无文本内容)"
            stop_loading_animation(success=api_call_succeeded, final_message=final_msg)

    if api_call_succeeded and assistant_full_response:
        log_debug(f"API完整响应已接收 (长度: {len(assistant_full_response)}).")
        return assistant_full_response
    return None


# --- 主程序 ---
def main():
    initialize_logger(config_debug_mode=config.DEBUG_MODE, app_name=f"{config.AI_NAME}_ChatRAG")

    rag_initialized_successfully = False
    flat_historical_messages, historical_sessions_map = [], {}

    start_loading_animation(
        message=f"{TermColors.CYAN}{config.AI_NAME}正在整理回忆思绪{TermColors.RESET}",
        animation_style_key='dots')

    init_success = False
    init_final_message = "系统初始化失败" # 默认失败消息

    try:
        if initialize_rag_components():
            rag_initialized_successfully = True
            log_debug("开始加载历史记录并更新RAG索引...")
            flat_historical_messages, historical_sessions_map = load_all_historical_data()

            if flat_historical_messages and chroma_collection is not None:
                add_messages_to_rag_index(flat_historical_messages)
                init_final_message = f"程序已就绪"
                log_debug("系统初始化完成。RAG索引包含 {chroma_collection.count()} 条记录。")
            elif chroma_collection is not None:
                init_final_message = "系统初始化完成。RAG就绪 (无历史数据索引)。"
            else:
                init_final_message = "系统初始化完成，但RAG数据处理异常或RAG未启用。"
            init_success = True # RAG组件初始化成功并处理完数据，标记为成功

        else:
            log_info_color("RAG组件初始化失败。尝试仅加载历史记录...", TermColors.YELLOW)
            flat_historical_messages, historical_sessions_map = load_all_historical_data()
            init_final_message = "RAG组件初始化失败。RAG功能将不可用。历史记录已加载（如果存在）。"
            init_success = True # 加载历史记录本身可以认为是部分的成功

    except Exception as e:
        log_error_color(f"初始化过程中发生意外严重错误: {e}")
        log_debug(f"Unexpected initialization error: {e}", exc_info=True)
        init_final_message = "初始化过程中发生严重错误"
        init_success = False # 任何非预期的错误都标记为失败
    finally:
        stop_loading_animation(success=init_success, final_message=init_final_message)

    if rag_initialized_successfully and chroma_collection:
        log_debug(f"RAG已准备就绪，知识库包含 {chroma_collection.count()} 条向量化历史消息。")

    elif config.USE_RAG:
        log_debug("RAG初始化失败或历史为空。问答可能仅依赖当前会话。")

    else:
        log_info("RAG功能已禁用。问答将仅依赖当前会话。")


    # --- 会话主循环开始 ---
    current_session_messages = []
    session_filepath = get_history_filepath()
    print(f"{TermColors.GREY}输入 'exit' 或 'quit' 退出。本次会话记录到: {session_filepath}{TermColors.RESET}")

    while True:
        try:
            user_input = input(f"{TermColors.YELLOW}你: {TermColors.RESET}")
        except UnicodeDecodeError:
            log_error_color("系统检测到无法识别的输入字符。");
            continue
        except EOFError:
            print("\n再见！(EOF)");
            break
        except KeyboardInterrupt:
            print("\n再见！(中断)");
            break

        if user_input.lower() in ["exit", "quit", "退出"]:
            print("再见！");
            break
        if not user_input.strip():
            continue

        api_payload_messages = []

        # --- 步骤 A: 准备各种消息组件 ---

        # A1. 获取当前时间并创建时间提示 (每次请求都获取)
        current_time_str = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        time_system_message = {"role": "system", "content": f"assistant_hint: 当前提问时间是 {current_time_str}。"}
        # log_debug 移动到添加时记录

        # A2. 准备配置中的系统提示 (如果存在)
        config_system_prompt_message = None
        if config.SYSTEM_PROMPT and config.SYSTEM_PROMPT.strip():
            config_system_prompt_message = {"role": "system", "content": config.SYSTEM_PROMPT}
            # log_debug 移动到添加时记录

        # A3. 处理 RAG 检索，并将结果收集到 rag_messages_to_add 列表
        rag_messages_to_add = []
        if config.USE_RAG and rag_initialized_successfully and chroma_collection and chroma_collection.count() > 0:
            start_loading_animation(
                message=f"{TermColors.MAGENTA}{config.AI_NAME}正在翻看记事本{TermColors.RESET}",
                animation_style_key='arrows', animation_color=TermColors.MAGENTA
            )
            rag_success_flag, rag_final_msg = False, "RAG检索完成"
            rag_context_messages = []
            try:
                rag_context_messages = get_rag_messages_chroma(user_input, historical_sessions_map)
                rag_success_flag = True
                if rag_context_messages:
                    rag_final_msg = f"RAG检索完毕 (找到 {len(rag_context_messages)} 条相关历史)"
                else:
                    rag_final_msg = "RAG检索完毕 (未找到相关历史)"
            except Exception as e_rag:
                log_error_color(f"RAG检索过程中发生错误: {e_rag}")
                log_debug(f"RAG retrieval error: {e_rag}", exc_info=True)
                rag_final_msg = "RAG检索失败"
                rag_success_flag = False # RAG 检索失败
            finally:
                stop_loading_animation(success=rag_success_flag, final_message=rag_final_msg)

            if rag_context_messages:
                rag_prefix_content = config.RAG_PROMPT_PREFIX
                if not rag_prefix_content or not rag_prefix_content.strip():
                    rag_prefix_content = "以下是根据你的问题从历史对话中检索到的相关片段，其中包含了对话发生的大致时间："
                rag_messages_to_add.append({"role": "system", "content": rag_prefix_content})
                rag_messages_to_add.extend(rag_context_messages)
                if config.RAG_PROMPT_SUFFIX and config.RAG_PROMPT_SUFFIX.strip():
                    rag_messages_to_add.append({"role": "system", "content": config.RAG_PROMPT_SUFFIX})
                # log_debug 移动到添加时记录
        else:
            reasons = [r for r, c in [("USE_RAG为False", not config.USE_RAG),
                                      ("RAG未成功初始化", not rag_initialized_successfully),
                                      ("Chroma集合不可用", chroma_collection is None),
                                      ("Chroma集合为空",
                                       chroma_collection is not None and chroma_collection.count() == 0)] if c]
            if reasons: log_debug(f"跳过RAG检索，原因: {', '.join(reasons)}。")

        # --- 步骤 B: 按新顺序组装 api_payload_messages ---

        # B1. 添加 RAG 消息 (如果存在)
        if rag_messages_to_add:
            api_payload_messages.extend(rag_messages_to_add)
            log_debug(f"已添加 {len(rag_messages_to_add)} 条RAG消息(包括前后缀)。")

        # B2. 添加配置中的系统提示 (在RAG之后)
        if config_system_prompt_message:
            api_payload_messages.append(config_system_prompt_message)
            log_debug(f"已添加系统提示: \"{config_system_prompt_message['content'][:100].strip().replace(chr(10), ' ')}...\"")

        # B3. 添加当前时间提示 (在配置系统提示之后)
        api_payload_messages.append(time_system_message)
        log_debug(f"已添加当前时间提示: \"{time_system_message['content']}\"")

        # B4. 添加当前会话的滑动窗口历史
        temp_sliding_window = current_session_messages[-(
            config.MAX_CONTEXT_MESSAGES_SLIDING_WINDOW - 1 if config.MAX_CONTEXT_MESSAGES_SLIDING_WINDOW > 0 else 0):]
        if temp_sliding_window: # 仅当有历史时才添加和记录
            api_payload_messages.extend(temp_sliding_window)
            log_debug(f"已从当前会话添加 {len(temp_sliding_window)} 条历史消息。")
        else:
            log_debug("当前会话无历史消息可添加。")


        # B5. 添加当前用户输入消息
        user_message_for_payload = {"role": "user", "content": user_input}
        api_payload_messages.append(user_message_for_payload)
        log_debug(f"已添加当前用户消息。最终Payload消息总数: {len(api_payload_messages)}")

        current_session_messages.append(user_message_for_payload)

        assistant_response = chat_with_deepseek(api_payload_messages)

        if assistant_response and assistant_response.strip():
            current_session_messages.append({"role": "assistant", "content": assistant_response})
            save_session_history(current_session_messages, session_filepath)
        else:
            log_warning_color("API调用未返回有效响应或响应为空。", TermColors.YELLOW)
            if current_session_messages and current_session_messages[-1]["role"] == "user":
                log_debug("由于API调用失败/响应无效，从当前会话记录中移除最后用户消息。")
                current_session_messages.pop()

if __name__ == "__main__":
    if not hasattr(config, 'API_KEY') or not config.API_KEY or \
            config.API_KEY.lower() in ["your_deepseek_api_key", "sk-114514", "sk-1234"] or \
            "actual_deepseek_api_key" in config.API_KEY.lower():
        log_error("错误：请在 config.py 文件中正确设置您的 DeepSeek API_KEY。")

    default_history_path = "./chat_history_data"
    if not hasattr(config, 'HISTORY_BASE_PATH') or not config.HISTORY_BASE_PATH:
        sys.stderr.write(
            f"{TermColors.YELLOW}警告: config.py 中未定义或 HISTORY_BASE_PATH 为空。将使用默认路径: {default_history_path}{TermColors.RESET}\n")
        sys.stderr.flush()
        setattr(config, 'HISTORY_BASE_PATH', default_history_path)
    try:
        os.makedirs(config.HISTORY_BASE_PATH, exist_ok=True)
    except OSError as e:
        sys.stderr.write(
            f"{TermColors.RED}错误: 无法创建历史记录目录 {config.HISTORY_BASE_PATH}: {e}{TermColors.RESET}\n")
        sys.stderr.flush()

    main()
```

### 文件: `test.py`

```python
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
```
