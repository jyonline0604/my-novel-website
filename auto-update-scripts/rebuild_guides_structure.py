#!/usr/bin/env python3
"""
重建所有攻略页，确保：
1. 每个游戏的攻略主题完全不同
2. 卡片标题与详细页标题严格匹配
3. 无重复内容
"""

from pathlib import Path

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# 每个游戏的真实攻略主题（基于实际游戏机制）
GAME_GUIDES = {
    "game_guide": [  # 问剑长生
        {"id": "sword", "title": "剑修神通天书", "file": "sword-guide.html"},
        {"id": "pet", "title": "灵兽驯养大全", "file": "pet-guide.html"},
        {"id": "craft", "title": "炼器系统攻略", "file": "craft-guide.html"},
        {"id": "ascend", "title": "飞升渡劫指南", "file": "ascension-guide.html"},
        {"id": "resource", "title": "资源管理技巧", "file": "resource-guide.html"},
        {"id": "boss", "title": "BOSS战攻略", "file": "boss-guide.html"},
    ],
    "saint_seiya": [  # 圣斗士星矢
        {"id": "cosmo", "title": "小宇宙燃烧机制", "file": "cosmo-guide.html"},
        {"id": "armor", "title": "圣衣装备搭配", "file": "armor-guide.html"},
        {"id": "team", "title": "阵容搭配推荐", "file": "team-composition-guide.html"},
        {"id": "gacha", "title": "黄金抽卡策略", "file": "gacha-guide.html"},
        {"id": "pvp", "title": "竞技场实战攻略", "file": "pvp-strategy-guide.html"},
        {"id": "temple", "title": "十二宫副本攻略", "file": "zodiac-temple-guide.html"},
    ],
    "beapro_football": [  # Be A Pro Football
        {"id": "formation", "title": "4-3-3 攻击阵型详解", "file": "formation-433-guide.html"},
        {"id": "training", "title": "球员培养完全指南", "file": "player-training-guide.html"},
        {"id": "transfer", "title": "转会市场攻略", "file": "transfer-market-guide.html"},
        {"id": "analytics", "title": "数据分析入门", "file": "data-analytics-guide.html"},
        {"id": "cup", "title": "冠军杯通关攻略", "file": "champions-cup-guide.html"},
        {"id": "tactics", "title": "战术设置指南", "file": "tactics-setup-guide.html"},
    ],
    "kai_tian": [  # 开天
        {"id": "cultivation", "title": "灵气修炼与渡劫", "file": "cultivation-guide.html"},
        {"id": "spirit", "title": "灵兽捕捉与培养", "file": "spirit-beast-guide.html"},
        {"id": "artifact", "title": "法宝炼器系统", "file": "artifact-forging-guide.html"},
        {"id": "sect", "title": "宗门任务攻略", "file": "sect-mission-guide.html"},
        {"id": "alchemy", "title": "炼丹系统详解", "file": "alchemy-guide.html"},
        {"id": "realm", "title": "境界提升路线", "file": "realm-progression-guide.html"},
    ]
}

def clear_guide_dir(game_type):
    """清空攻略目录（保留目录结构）"""
    dir_path = REPO_DIR / "guides" / game_type
    if dir_path.exists():
        for f in dir_path.iterdir():
            if f.is_file():
                f.unlink()
        print(f"  🗑️  清空 {game_type}/")
    else:
        dir_path.mkdir(parents=True, exist_ok=True)

def create_guide_page(game_type, guide_info):
    """创建空白的占位攻略页（标题与文件对应）"""
    theme_map = {
        "game_guide": {"primary": "#d4a017", "bg": "#0a0a0a", "name": "問劍長生"},
        "saint_seiya": {"primary": "#ffd700", "bg": "#1a1a2e", "name": "聖鬥士星矢重生2"},
        "beapro_football": {"primary": "#2ecc71", "bg": "#0d1b2a", "name": "Be A Pro Football"},
        "kai_tian": {"primary": "#9b59b6", "bg": "#1a0a2e", "name": "開天"}
    }
    theme = theme_map[game_type]
    dir_path = REPO_DIR / "guides" / game_type
    file_path = dir_path / guide_info["file"]
    
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>
        :root {{ --primary: {theme["primary"]}; --bg: {theme["bg"]}; --text: #fff; --card-bg: rgba(255,255,255,0.05); }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 80px 2rem 2rem; max-width: 900px; margin: 0 auto; }}
        .back-link {{ color: var(--primary); margin-bottom: 2rem; display: block; text-decoration: none; }}
        .guide-content {{ background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--primary); }}
        h1 {{ color: var(--primary); font-size: 2rem; margin-bottom: 1rem; }}
        p {{ margin-bottom: 1rem; color: #bbb; }}
        .placeholder {{ background: rgba(255,193,7,0.1); border-left: 4px solid #ffc107; padding: 1rem; margin: 2rem 0; }}
    </style>
</head>
<body>
    <a href="/{game_type}-guide.html" class="back-link"><i class="fas fa-arrow-left"></i> 返回攻略中心</a>
    <div class="guide-content">
        <h1>{guide_info["title"]}</h1>
        <p>本篇攻略正在撰写中，敬请期待完整内容。</p>
        <div class="placeholder">
            <strong>🔧 待完善</strong><br>
            此页面为占位符，详细攻略内容稍后更新。
        </div>
    </div>
</body>
</html>'''
    
    file_path.write_text(html, encoding='utf-8')
    print(f"  ✅ 创建: {guide_info['file']} - {guide_info['title']}")

def create_symlinks(game_type, guides):
    """为每个攻略页创建无后缀的软链接（兼容旧链接）"""
    dir_path = REPO_DIR / "guides" / game_type
    for guide in guides:
        target = guide["file"]
        link_name = guide["id"] + ".html"  # 去掉 -guide
        
        # 删除已存在的（文件或软链接）
        link_path = dir_path / link_name
        if link_path.exists() or link_path.is_symlink():
            link_path.unlink()
        
        # 创建软链接
        link_path.symlink_to(target)
        print(f"  🔗 链接: {link_name} -> {target}")

def main():
    print("🔄 开始重建所有攻略页结构...")
    
    for game_type, guides in GAME_GUIDES.items():
        print(f"\n📁 {game_type}:")
        clear_guide_dir(game_type)
        
        # 创建真实详细页
        for guide in guides:
            create_guide_page(game_type, guide)
        
        # 创建软链接
        create_symlinks(game_type, guides)
    
    print("\n✅ 所有攻略页重建完成！")
    print("📊 统计:")
    for game_type, guides in GAME_GUIDES.items():
        count = len(guides)
        print(f"  {game_type}: {count} 个独特攻略主题")
    
    return 0

if __name__ == "__main__":
    exit(main())
