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
        'prompt': textwrap.dedent(f"""
        你将扮演《无职转生》中的角色“洛琪希·米格路迪亚”（Roxy Migurdia）。请严格遵守以下设定：
        1.  **身份与性格**: 你是一位知识渊博、经验丰富的魔术师，同时也是{'{player_name}'}的家庭教师。你善良、认真，富有责任感，但有时会因为一些意想不到的事情而感到害羞或慌乱。
        2.  **言谈举止**: 你的言语非常礼貌，习惯使用敬语（です/ます调），即使在亲近的人面前也保持着老师的姿态。例如，称呼玩家为“{'{player_name}'}さん”或“鲁迪乌斯”。
        3.  **核心能力**: 你精通水系魔术，并且拥有广泛的魔物和古代遗迹知识。在迷宫探索中，你会主动提供建议、分析情况，并在必要时施展强大的魔法保护同伴。
        4.  **互动风格**: 你会关心{'{player_name}'}的状态，在他做出正确决定时给予表扬，在他遇到危险时表现出担忧。当{'{player_name}'}说出一些轻浮的话时，你会略带羞涩地训斥他，但内心并不真的生气。
        5.  **输出格式**: 请直接输出你的对话内容，不要包含任何角色扮演的额外说明，如 `(洛琪希心想)` 或 `[洛琪希的动作]`。
        """).strip(),
        # 可以添加立绘和语音的配置
        'visuals': {
            'default_sprite': 'roxy_normal.png',
            'sprites': {
                'normal': 'roxy_normal.png',
                'smile': 'roxy_smile.png',
                'blush': 'roxy_blush.png',
                'surprised': 'roxy_surprised.png',
                'casting': 'roxy_casting.png',
            }
        },
        'audio': {
            'voice_pack_id': 'roxy_voice_01'
        }
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
        'version': '1.0.0',
        'author': 'LingChat AI',
        'start_unit_id': '00_Labyrinth_Entrance',
        'character_roles': [ROXY_CHAR_ID] # 这个剧本只需要洛琪希一个AI角色
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

    这里既有失落的宝藏，也潜伏着凶猛的魔物和致命的陷阱。

    ## 游戏特色
    - **无限探索**: 由AI驱动的随机事件生成器，让你的每一次探索都充满新奇。
    - **动态互动**: 与洛琪希自由对话，她的反应和建议将基于你们的处境和好感度。
    - **策略选择**: 面对危险，是勇敢战斗，还是巧妙规避？你的选择将决定你们的命运。
    - **状态管理**: 注意你的生命值，明智地使用资源，在这场无尽的冒险中走得更远。

    与你最信赖的老师并肩作战，揭开这座迷宫深处的秘密吧！
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
        'dice_roll': 1 # 初始化一个骰子值
    }
    gamestate_path = os.path.join(pack_path, 'save', 'gamestate.yaml')
    write_yaml_file(gamestate_path, initial_gamestate)

def generate_story_units(pack_path):
    """生成所有剧情单元的YAML文件"""
    print("6. 正在生成核心剧情单元...")
    story_dir = os.path.join(pack_path, "story")
    
    # --- Unit 00: 迷宫入口 (开始) ---
    unit_00 = {
        'SceneConfig': {
            'id': '00_Labyrinth_Entrance',
            'name': '迷宫入口',
            'visuals': {'background_image': 'bg_labyrinth_entrance.png'},
            'audio': {'background_music': 'bgm_mysterious_cave.mp3'}
        },
        'Events': [
            {'Type: Chapter | Mode: Preset': {
                'Title': "序章：未知的呼唤",
                'Number': 0,
                'Description': "古老的石门缓缓开启，深邃的黑暗仿佛在吞噬一切光亮。"
            }},
            {'Type: Narration | Mode: Preset': '你和洛琪希老师站在一座巨大而古老的地下迷宫入口。'},
            {'Type: Narration | Mode: Preset': '空气中弥漫着潮湿的泥土和淡淡的魔力气息。'},
            # 修正点: 直接使用角色ID，而不是变量
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': 
                textwrap.dedent(f"""
                {'{player_name}'}さん，这里就是传说中的“无尽回廊”了。据说里面的结构会不断变化，一定要跟紧我，千万不要走散了。
                """).strip()
            },
            {'Type: Player | Mode: Input': '我知道了，老师。我们出发吧！'}
        ],
        'EndCondition': {
            'Type': 'Linear',
            'NextUnitID': '01_Explore_Corridor'
        }
    }
    write_yaml_file(os.path.join(story_dir, '00_Labyrinth_Entrance.yaml'), unit_00)

    # --- Unit 01: 探索回廊 (核心循环) ---
    unit_01 = {
        'SceneConfig': {
            'id': '01_Explore_Corridor',
            'name': '探索回廊',
            'visuals': {'background_image': 'bg_labyrinth_corridor_generic.png'},
            'audio': {'background_music': 'bgm_dungeon_explore.mp3'}
        },
        'Events': [
            {'Type: Action | Tool: Calculate | Variable: labyrinth_floor': {
                'Expression': '{labyrinth_floor} + 1'
            }},
            {'Type: Narration | Mode: Prompt':
                textwrap.dedent("""
                你是一个迷宫探索游戏的旁白。请根据以下信息，生成一段主角和洛琪希进入下一个区域时所见的场景描述。
                - 当前楼层: {labyrinth_floor}
                - 已击败怪物数: {monsters_defeated}
                - 历史对话: (参考传入的对话历史)
                请描述一个富有想象力的、与之前不同的地下城场景（如长满发光蘑菇的洞穴、有地下暗河的通道、刻满古代壁画的石室等）。两到三行即可。
                """).strip()
            },
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Prompt': 
                textwrap.dedent(f"""
                这是你的内心活动：你看到了新的场景，请根据旁白的描述，结合你的知识，对这个新环境发表你的看法或向{'{player_name}'}发出提醒。
                """).strip()
            },
            {'Type: Action | Tool: Random | Variable: dice_roll': {
                'Min': 1, 'Max': 20
            }},
        ],
        'EndCondition': {
            'Type': 'Conditional',
            'Cases': [
                {'Condition': '{labyrinth_floor} >= 5 and {dice_roll} > 15',
                 'Then': {
                    'Type': 'FreeTime',
                    'InstructionToPlayer': '你们找到了一个相对安全的休息点。可以和洛琪希自由交谈。输入“我们继续前进吧”结束休息以继续探险，或输入“我们回去吧”结束本次探险。',
                    'ExitPromptInInputBox': '我们继续前进吧',
                    'NextUnitID': '01_Explore_Corridor'
                 }},
                 {'Condition': '{labyrinth_floor} >= 5 and {dice_roll} <= 15',
                 'Then': {
                    'Type': 'Branching',
                    'Method': 'PlayerChoice',
                    'Branches': {
                        'A': {'DisplayText': "我们继续前进吧", 'NextUnitID': '01_Explore_Corridor'},
                        'B': {'DisplayText': "我们回去吧，老师", 'NextUnitID': '99_Exit_Labyrinth'}
                    }
                 }},
                {'Condition': '{dice_roll} >= 16', 'Then': {'Type': 'Linear', 'NextUnitID': '02_Event_Treasure'}},
                {'Condition': '{dice_roll} >= 6 and {dice_roll} < 16', 'Then': {'Type': 'Linear', 'NextUnitID': '03_Event_Monster'}},
                {'Condition': '{dice_roll} < 6', 'Then': {'Type': 'Linear', 'NextUnitID': '04_Event_Trap'}},
            ],
            'Else': {
                'Type': 'Linear',
                'NextUnitID': '01_Explore_Corridor'
            }
        }
    }
    write_yaml_file(os.path.join(story_dir, '01_Explore_Corridor.yaml'), unit_01)

    # --- Unit 02: 发现宝藏 ---
    unit_02 = {
        'SceneConfig': {'id': '02_Event_Treasure', 'name': '发现宝藏'},
        'Events': [
            {'Type: Narration | Mode: Preset': '在通道的角落，你们发现了一个闪烁着微光的宝箱！'},
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '太好了！运气不错呢。不过，要小心可能存在的陷阱。'},
            {'Type: Player | Mode: Input': '我来打开看看！'},
            {'Type: Narration | Mode: Preset': '你小心翼翼地打开了宝箱...'},
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
            {'Type: Narration | Mode: Prompt': 
                textwrap.dedent("""
                你是一个迷宫探索游戏的旁白。请生成一段遭遇怪物的描述。可以是一些经典的地下城生物，如哥布林、史莱姆、骷髅兵，或者更具想象力的东西。
                """).strip()
            },
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Prompt':
                textwrap.dedent(f"""
                这是你的内心活动：你看到了旁白描述的怪物。请根据你的知识，快速说出这种怪物的名称和弱点，并提醒{'{player_name}'}准备战斗。
                """).strip()
            },
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

    # --- Unit 03A: 玩家战斗 ---
    unit_03A = {
        'SceneConfig': {'id': '03A_Player_Fights', 'name': '玩家战斗'},
        'Events': [
            {'Type: Narration | Mode: Preset': '你握紧武器，勇敢地冲向了怪物！'},
            {'Type: Narration | Mode: Prompt': '你是一个战斗旁白。请描述一下玩家与怪物激烈战斗的场景。'},
            {'Type: Narration | Mode: Preset': '在洛琪希老师的魔法支援下，你最终击败了怪物！'},
            {'Type: Action | Tool: Calculate | Variable: monsters_defeated': {'Expression': '{monsters_defeated} + 1'}},
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '做得很好，{player_name}さん！你的实战能力越来越强了。'}
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '03A_Player_Fights.yaml'), unit_03A)

    # --- Unit 03B: 洛琪希战斗 ---
    unit_03B = {
        'SceneConfig': {'id': '03B_Roxy_Fights', 'name': '洛琪希战斗'},
        'Events': [
            {'Type: Narration | Mode: Preset': '洛琪希老师点了点头，走上前护在了你的身前。'},
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '交给我吧。看好了，{player_name}さん。这就是水系魔法的威力！'},
            {'Type: Narration | Mode: Prompt': '你是一个战斗旁白。请描述一下洛琪希如何使用强大的水系魔法（如水箭、冰枪）瞬间击败怪物的帅气场景。'},
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
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '小心，是陷阱！'},
            {'Type: Action | Tool: Random | Variable: dice_roll': {'Min': 1, 'Max': 20}},
        ],
        'EndCondition': {
            'Type': 'Conditional',
            'Cases': [
                {'Condition': '{dice_roll} > 10', 'Then': {'Type': 'Linear', 'NextUnitID': '04A_Trap_Dodged'}},
            ],
            'Else': {'Type': 'Linear', 'NextUnitID': '04B_Trap_Hit'}
        }
    }
    write_yaml_file(os.path.join(story_dir, '04_Event_Trap.yaml'), unit_04)

    # --- Unit 04A: 躲开陷阱 ---
    unit_04A = {
        'SceneConfig': {'id': '04A_Trap_Dodged', 'name': '躲开陷阱'},
        'Events': [
            {'Type: Narration | Mode: Preset': '你反应迅速，一个侧身躲开了从墙壁射出的毒箭！'},
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '好险！反应很快嘛，{player_name}さん。'},
            {'Type: Action | Tool: Calculate | Variable: traps_disarmed': {'Expression': '{traps_disarmed} + 1'}}
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '04A_Trap_Dodged.yaml'), unit_04A)

    # --- Unit 04B: 被陷阱击中 ---
    unit_04B = {
        'SceneConfig': {'id': '04B_Trap_Hit', 'name': '被陷阱击中'},
        'Events': [
            {'Type: Narration | Mode: Preset': '虽然你尽力躲避，但手臂还是被划出了一道伤口。'},
            {'Type: Action | Tool: Calculate | Variable: player_hp': {'Expression': '{player_hp} - 10'}},
            {'Type: Notice | Mode: Preset | Location: message': '你失去了10点生命值！当前HP: {player_hp}'},
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '不要紧吧？我马上为你治疗！'},
            {'Type: Narration | Mode: Preset': '洛琪希老师吟唱起咒语，一道柔和的绿光包裹了你的伤口。'},
            {'Type: Action | Tool: Calculate | Variable: player_hp': {'Expression': '{player_hp} + 10'}},
            {'Type: Notice | Mode: Preset | Location: message': '洛琪希为你恢复了10点生命值！当前HP: {player_hp}'},
        ],
        'EndCondition': {'Type': 'Linear', 'NextUnitID': '01_Explore_Corridor'}
    }
    write_yaml_file(os.path.join(story_dir, '04B_Trap_Hit.yaml'), unit_04B)

    # --- Unit 99: 离开迷宫 (结局) ---
    unit_99 = {
        'SceneConfig': {
            'id': '99_Exit_Labyrinth',
            'name': '离开迷宫',
            'visuals': {'background_image': 'bg_labyrinth_entrance.png'},
            'audio': {'background_music': 'bgm_town_evening.mp3'}
        },
        'Events': [
            {'Type: Narration | Mode: Preset': '你们顺着原路返回，终于再次看到了迷宫入口的光芒。'},
            # 修正点: 直接使用角色ID
            {f'Type: Dialogue | Character: {ROXY_CHAR_ID} | Mode: Preset': '呼...总算是出来了。这次的探索收获很大呢，辛苦了，{player_name}さん。'},
            {'Type: Notice | Mode: Preset | Location: popup': 
                textwrap.dedent("""
                探险结束！
                最终到达楼层: {labyrinth_floor}
                击败怪物数量: {monsters_defeated}
                发现宝藏数量: {treasure_found}
                解除陷阱数量: {traps_disarmed}
                与洛琪希的好感度: {favorability_Roxy}
                """).strip()
            },
            {'Type: Narration | Mode: Preset': '夕阳下，你和老师的身影被拉得很长。下一次冒险，又会在哪里呢？'},
            {'Type: Chapter | Mode: Preset': {
                'Title': "探险结束", 'Number': 99, 'Description': "感谢游玩！"
            }}
        ],
        'EndCondition': None # None 表示游戏结束
    }
    write_yaml_file(os.path.join(story_dir, '99_Exit_Labyrinth.yaml'), unit_99)


# --- 主程序 ---
def main():
    """脚本主入口"""
    print("=" * 50)
    print(" LingChat 0.4 剧本包生成器 ")
    print(" 剧本: 与洛琪希的地下迷宫探险 (修正版)")
    print("=" * 50)

    try:
        pack_path = create_directories()
        generate_roxy_character()
        generate_global_config(pack_path)
        generate_intro_md(pack_path)
        generate_gamestate(pack_path)
        generate_story_units(pack_path)

        print("\n" + "=" * 50)
        print("🎉 恭喜！剧本包已成功生成！")
        print(f"剧本路径: {os.path.join(STORY_PACKS_BASE_PATH, STORY_PACK_NAME)}")
        print(f"角色路径: {os.path.join(CHARACTERS_BASE_PATH, f'{ROXY_CHAR_ID}.yaml')}")
        print("现在你可以在 LingChat 中加载这个新剧本了！")
        print("=" * 50)

    except Exception as e:
        print("\n" + "!" * 50)
        print(f"❌ 生成过程中发生错误: {e}")
        print("!" * 50)

if __name__ == "__main__":
    main()