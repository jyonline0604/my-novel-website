#!/usr/bin/env python3
"""为所有缺失的详细攻略页创建占位符（确保每个卡片都有对应的详细页）"""

from pathlib import Path
import re

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# 所有需要的详细页清单（基于 rebuild_guides_structure.py 的 GAME_GUIDES）
needed_guides = {
    "game_guide": [
        {"id": "sword", "title": "剑修神通", "file": "sword-guide.html", "has_content": True},
        {"id": "pet", "title": "灵兽驯养", "file": "pet-guide.html", "has_content": True},
        {"id": "craft", "title": "炼器系统", "file": "craft-guide.html", "has_content": True},
        {"id": "ascend", "title": "飞升渡劫", "file": "ascension-guide.html", "has_content": True},
        {"id": "resource", "title": "资源管理", "file": "resource-guide.html", "has_content": True},
        {"id": "boss", "title": "BOSS攻略", "file": "boss-guide.html", "has_content": True},
    ],
    "saint_seiya": [
        {"id": "cosmo", "title": "小宇宙燃烧", "file": "cosmo-guide.html", "has_content": True},
        {"id": "armor", "title": "圣衣装备", "file": "armor-guide.html", "has_content": True},
        {"id": "team", "title": "阵容搭配", "file": "team-composition-guide.html", "has_content": True},
        {"id": "gacha", "title": "黄金抽卡", "file": "gacha-guide.html", "has_content": True},
        {"id": "pvp", "title": "竞技场攻略", "file": "pvp-strategy-guide.html", "has_content": True},
        {"id": "temple", "title": "十二宫副本", "file": "zodiac-temple-guide.html", "has_content": True},
    ],
    "beapro_football": [
        {"id": "formation", "title": "战术阵型大全", "file": "formation-433-guide.html", "has_content": True},
        {"id": "training", "title": "球员培养指南", "file": "player-training-guide.html", "has_content": True},
        {"id": "transfer", "title": "转会市场攻略", "file": "transfer-market-guide.html", "has_content": True},
        {"id": "analytics", "title": "数据分析入门", "file": "data-analytics-guide.html", "has_content": True},
        {"id": "cup", "title": "冠军杯通关", "file": "champions-cup-guide.html", "has_content": True},
        {"id": "skills", "title": "技巧训练场", "file": "skills-training-guide.html", "has_content": True},
    ],
    "kai_tian": [
        {"id": "cultivation", "title": "灵气修炼与渡劫", "file": "cultivation-guide.html", "has_content": True},
        {"id": "spirit", "title": "灵兽捕捉与培养", "file": "spirit-beast-guide.html", "has_content": True},
        {"id": "artifact", "title": "法宝炼器系统", "file": "artifact-forging-guide.html", "has_content": True},
        {"id": "sect", "title": "宗门任务攻略", "file": "sect-mission-guide.html", "has_content": True},
        {"id": "alchemy", "title": "炼丹系统详解", "file": "alchemy-guide.html", "has_content": True},
        {"id": "realm", "title": "境界提升路线", "file": "realm-progression-guide.html", "has_content": True},
        {"id": "sword", "title": "剑修神通", "file": "sword-cultivation-guide.html", "has_content": False},
        {"id": "pet", "title": "灵兽养成指南", "file": "pet-nurturing-guide.html", "has_content": False},
        {"id": "resource", "title": "资源管理技巧", "file": "resource-management-guide.html", "has_content": False},
        {"id": "boss", "title": "BOSS战攻略", "file": "boss-battle-guide.html", "has_content": False},
        {"id": "ascend", "title": "飞升渡劫指南", "file": "ascension-guide.html", "has_content": True},
        {"id": "craft", "title": "炼器系统攻略", "file": "crafting-system-guide.html", "has_content": False},
    ]
}

# 主题配色
themes = {
    "game_guide": {"primary": "#d4a017", "bg": "#0a0a0a"},
    "saint_seiya": {"primary": "#ffd700", "bg": "#1a1a2e"},
    "beapro_football": {"primary": "#2ecc71", "bg": "#0d1b2a"},
    "kai_tian": {"primary": "#9b59b6", "bg": "#1a0a2e"}
}

def create_placeholder(game_type, guide_info):
    """创建占位详细页"""
    dir_path = REPO_DIR / "guides" / game_type
    file_path = dir_path / guide_info["file"]
    
    if file_path.exists():
        return False  # 已存在
    
    theme = themes[game_type]
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>:root{{--primary:{theme["primary"]};--bg:{theme["bg"]};--text:#fff}}body{{background:var(--bg");color:var(--text");padding:2rem;max-width:900px;margin:0 auto}}.back{{color:var(--primary");display:block;margin-bottom:2rem}}</style>
</head><body>
    <a href="/{game_type}-guide.html" class="back">← 返回攻略中心</a>
    <h1>{guide_info["title"]}</h1>
    <p>此攻略正在撰写中，近期会更新详细内容。</p>
</body></html>'''
    
    file_path.write_text(html, encoding='utf-8')
    return True

def main():
    created = 0
    for game_type, guides in needed_guides.items():
        dir_path = REPO_DIR / "guides" / game_type
        dir_path.mkdir(parents=True, exist_ok=True)
        
        for guide in guides:
            if create_placeholder(game_type, guide):
                print(f"✅ {game_type}/{guide['file']} - {guide['title']}")
                created += 1
    
    print(f"\n✨ 共创建 {created} 个占位详细页")
    return created

if __name__ == "__main__":
    main()
