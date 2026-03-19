#!/usr/bin/env python3
"""
攻略页面内容生成器 - 最终版本
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
CONFIG_FILE = REPO_DIR / "auto-update-scripts" / "update_config.json"

def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_game_name(key):
    names = {
        "game_guide": "問劍長生",
        "saint_seiya": "聖鬥士星矢重生2",
        "beapro_football": "Be A Pro Football",
        "kai_tian": "開天"
    }
    return names.get(key, key)

def generate_news(game_key):
    now = datetime.now()
    base_news = [
        {"title": "最新版本更新公告", "date": (now - timedelta(days=2)).strftime("%m-%d"), "excerpt": "本次更新带来了多项内容优化和bug修复，新增了若干趣味玩法...", "category": "版本更新", "link": "https://www.taptap.cn"},
        {"title": "新手快速上手指南", "date": (now - timedelta(days=5)).strftime("%m-%d"), "excerpt": "详细讲解游戏基础操作和核心机制，帮助你快速度过前期...", "category": "新手攻略", "link": "https://www.taptap.cn"},
        {"title": "进阶技巧与策略分享", "date": (now - timedelta(days=8)).strftime("%m-%d"), "excerpt": "高级玩家实战经验总结，包含阵容搭配、资源管理等核心内容...", "category": "深度攻略", "link": "https://www.taptap.cn"}
    ]
    
    if game_key == "game_guide":
        base_news[0]["title"] = "問劍長生 V3.5 版本：新靈獸「玄武」登場"
        base_news[1]["title"] = "新手必看：前30級快速升級攻略"
        base_news[2]["title"] = "劍修神通搭配推薦：打出最高輸出"
        base_news[0]["link"] = "https://www.taptap.cn/app/713640/topic"
        base_news[1]["link"] = "https://www.taptap.cn/app/713640/topic"
        base_news[2]["link"] = "https://www.taptap.cn/app/713640/topic"
    elif game_key == "saint_seiya":
        base_news[0]["title"] = "聖鬥士星矢重生2：黃金聖鬥士抽取攻略"
        base_news[1]["title"] = "小宇宙配置指南：最大化屬性加成"
        base_news[2]["title"] = "PVP競技場 Top10 陣容推薦"
        base_news[0]["link"] = "https://www.taptap.cn/app/507373/topic"
        base_news[1]["link"] = "https://www.taptap.cn/app/507373/topic"
        base_news[2]["link"] = "https://www.taptap.cn/app/507373/topic"
    elif game_key == "beapro_football":
        base_news[0]["title"] = "Be A Pro Football 第三賽季更新：新增歐洲冠軍聯賽模式"
        base_news[1]["title"] = "球員培養攻略：如何打造夢幻陣容"
        base_news[2]["title"] = "戰術系統深度解析：4-3-3 vs 4-4-2"
        base_news[0]["link"] = "https://www.taptap.cn/app/593794?os=android"
        base_news[1]["link"] = "https://www.taptap.cn/app/593794?os=android"
        base_news[2]["link"] = "https://www.taptap.cn/app/593794?os=android"
    
    return base_news

def generate_guides(game_key):
    common = [
        {"title": "新手入門指南", "icon": "fa-book-open", "difficulty": "入門", "desc": "從零開始，快速上手"},
        {"title": "核心玩法解析", "icon": "fa-gamepad", "difficulty": "中級", "desc": "深度了解遊戲機制"},
    ]
    
    if game_key == "game_guide":
        return common + [
            {"title": "劍修神通搭配", "icon": "fa-khanda", "difficulty": "高級", "desc": "極限輸出循環"},
            {"title": "靈獸馴養", "icon": "fa-dragon", "difficulty": "中級", "desc": "捕捉培養進階"},
            {"title": "煉器系統", "icon": "fa-gem", "difficulty": "中級", "desc": "打造極品裝"},
            {"title": "飛升攻略", "icon": "fa-feather-alt", "difficulty": "高級", "desc": "渡劫全流程"}
        ]
    elif game_key == "saint_seiya":
        return common + [
            {"title": "小宇宙配置", "icon": "fa-circle-notch", "difficulty": "高級", "desc": "完美配裝方案"},
            {"title": "聖衣強化", "icon": "fa-shield-alt", "difficulty": "中級", "desc": "最大化屬性"},
            {"title": "黃金聖鬥士", "icon": "fa-crown", "difficulty": "入門", "desc": "全角色圖鑒"},
            {"title": "PVP陣容", "icon": "fa-trophy", "difficulty": "高級", "desc": "竞技场制霸"}
        ]
    elif game_key == "beapro_football":
        return common + [
            {"title": "球員轉會", "icon": "fa-user-circle", "difficulty": "中級", "desc": "低價淘寶"},
            {"title": "戰術板設置", "icon": "fa-chess-board", "difficulty": "高級", "desc": "戰術定制"},
            {"title": "青訓系統", "icon": "fa-users", "difficulty": "中級", "desc": "培養新星"},
            {"title": "聯賽攻略", "icon": "fa-trophy", "difficulty": "高級", "desc": "贏下冠軍"}
        ]
    else:  # kai_tian
        return common + [
            {"title": "法寶煉器", "icon": "fa-gem", "difficulty": "高級", "desc": "極品打造"},
            {"title": "渡劫飛升", "icon": "fa-cloud", "difficulty": "高級", "desc": "天劫應對"},
            {"title": "靈獸馴養", "icon": "fa-dragon", "difficulty": "中級", "desc": "獲取培養"},
            {"title": "門派選擇", "icon": "fa-landmark", "difficulty": "入門", "desc": "特點分析"}
        ]

def generate_html(game_key, config):
    theme_color = config.get("theme_color", "#2563eb")
    game_name = get_game_name(game_key)
    description = config.get("description", f"{game_name}完整攻略")
    keywords = config.get("keywords", [game_name, "攻略"])
    tap_tap_url = config.get("tap_tap_url", "https://www.taptap.cn")
    
    news = generate_news(game_key)
    guides = generate_guides(game_key)
    highlights = [
        {"title": "限時登入獎勵：連續7天送橙武", "tag": "活動", "color": "#ff6b6b"},
        {"title": "本周竞技场双倍奖励", "tag": "福利", "color": "#4ecdc4"},
        {"title": "新版本攻略征集大赛", "tag": "社区", "color": "#ffd93d"}
    ]
    
    r, g, b = int(theme_color[1:3], 16), int(theme_color[3:5], 16), int(theme_color[5:7], 16)
    
    news_cards = ""
    for i, n in enumerate(news):
        # Use placehold.co for reliable image display
        color_hex = theme_color.lstrip('#')
        img_url = f"https://placehold.co/400x200/{color_hex}/FFF?text={n['category']}"
        news_cards += f'''
        <article class="news-card {'highlight' if i==0 else ''}">
            <div class="news-card-image">
                <img src="{img_url}" alt="{n['title']}" loading="lazy">
                <span class="category-tag">{n['category']}</span>
            </div>
            <div class="news-card-body">
                <h3 class="news-card-title">{n['title']}</h3>
                <p class="news-card-excerpt">{n['excerpt']}</p>
                <div class="news-card-meta">
                    <span class="news-card-date">{n['date']}</span>
                </div>
                <a href="{n['link']}" target="_blank" class="news-card-link">
                    <i class="fas fa-external-link-alt"></i> 查看詳情
                </a>
            </div>
        </article>
        '''
    
    guides_grid = ""
    for g in guides:
        guides_grid += f'''
        <article class="news-card">
            <div class="news-card-body">
                <div style="text-align: center; margin-bottom: 15px;">
                    <i class="fas {g['icon']}" style="font-size: 3rem; color: {theme_color};"></i>
                </div>
                <h3 class="news-card-title">{g['title']}</h3>
                <p class="news-card-excerpt">{g['desc']}</p>
                <div class="news-card-meta">
                    <span class="news-card-source">{g['difficulty']}</span>
                </div>
                <a href="#" class="news-card-link">
                    <i class="fas fa-book-open"></i> 閱讀攻略
                </a>
            </div>
        </article>
        '''
    
    highlights_html = ""
    for h in highlights:
        highlights_html += f'''
        <article class="news-card highlight">
            <div class="news-card-body">
                <span class="category-tag" style="position:static; margin-bottom:12px; background-color: {h['color']}; border-radius: 20px; padding: 6px 16px; color: white;">{h['tag']}</span>
                <h3 class="news-card-title">{h['title']}</h3>
                <a href="#" class="news-card-link"><i class="fas fa-bolt"></i> 查看詳情</a>
            </div>
        </article>
        '''
    
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game_name}攻略中心 | 科技修真傳</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{', '.join(keywords)}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="style.css">
    <style>
        :root {{ --primary-color: {theme_color}; --bg-gradient: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); }}
        .hero-banner {{ background: var(--bg-gradient); padding: 100px 20px 60px; text-align: center; color: white; }}
        .hero-banner h1 {{ font-size: 3.5rem; margin-bottom: 15px; text-shadow: 0 4px 15px rgba({r},{g},{b},0.5); }}
        .hero-banner .tagline {{ font-size: 1.4rem; opacity: 0.9; margin-bottom: 20px; }}
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 28px; max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .news-card {{ background: white; border-radius: 18px; overflow: hidden; box-shadow: 0 6px 25px rgba(0,0,0,0.08); display: flex; flex-direction: column; }}
        .news-card-image {{ height: 200px; position: relative; overflow: hidden; }}
        .news-card-image img {{ width: 100%; height: 100%; object-fit: cover; }}
        .news-card-image .category-tag {{ position: absolute; top: 15px; left: 15px; background: var(--primary-color); color: white; padding: 6px 16px; border-radius: 25px; font-size: 0.75rem; }}
        .news-card-body {{ padding: 24px; flex: 1; display: flex; flex-direction: column; }}
        .news-card-title {{ font-size: 1.2rem; font-weight: 700; margin-bottom: 12px; }}
        .news-card-excerpt {{ color: #555; font-size: 0.9rem; line-height: 1.7; flex: 1; margin-bottom: 16px; }}
        .news-card-meta {{ display: flex; justify-content: space-between; font-size: 0.8rem; color: #888; padding-top: 14px; border-top: 1px solid #eee; }}
        .news-card-link {{ display: inline-flex; align-items: center; gap: 8px; color: var(--primary-color); font-weight: 700; text-decoration: none; margin-top: 14px; padding: 8px 16px; border: 2px solid var(--primary-color); border-radius: 25px; }}
        .section-divider {{ max-width: 1200px; margin: 60px auto; padding: 0 20px; text-align: center; }}
        .quick-links {{ background: #f8f9fa; padding: 60px 20px; margin-top: 40px; }}
        .quick-links-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 20px; max-width: 1000px; margin: 0 auto; }}
        .quick-link-card {{ background: white; padding: 24px; border-radius: 16px; text-align: center; text-decoration: none; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .cta-section {{ background: var(--bg-gradient); color: white; text-align: center; padding: 60px 20px; margin-top: 40px; }}
        .cta-button {{ display: inline-block; background: var(--primary-color); color: white; padding: 14px 32px; border-radius: 30px; text-decoration: none; margin-top: 15px; }}
        @media (max-width: 768px) {{ .news-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <header class="main-header">
        <div class="novel-title">科技修真傳</div>
        <nav class="main-nav">
            <a href="index.html" class="nav-link">🏠 首頁</a>
            <a href="game-guide.html" class="nav-link{' active' if '問劍' in game_name else ''}">🎮 問劍長生</a>
            <a href="saint-seiya-guide.html" class="nav-link{' active' if '聖鬥士' in game_name else ''}">⚔️ 聖鬥士星矢</a>
            <a href="beapro-football-guide.html" class="nav-link{' active' if 'Be A Pro' in game_name else ''}">⚽ Be A Pro</a>
            <a href="kai-tian-guide.html" class="nav-link{' active' if '開天' in game_name else ''}">🗡️ 開天</a>
            <a href="ai-news.html" class="nav-link">🤖 AI 資訊</a>
        </nav>
    </header>

    <div class="hero-banner">
        <h1>🎮 {game_name}</h1>
        <p class="tagline">{description}</p>
        <p class="update-time">最後更新：{datetime.now().strftime('%Y年%m月%d日 %H:%M')}</p>
    </div>

    <section class="news-container">
        <div class="section-header"><h2>📰 最新資訊</h2></div>
        <div class="news-grid">{news_cards}</div>
    </section>

    <div class="section-divider"><h3>✨ 精選攻略 ✨</h3></div>

    <section class="news-container">
        <div class="section-header"><h2>📚 攻略大全</h2></div>
        <div class="news-grid">{guides_grid}</div>
    </section>

    <div class="section-divider"><h3>🎯 當前活動 🎯</h3></div>

    <section class="news-container">
        <div class="section-header"><h2>🎉 活動一覽</h2></div>
        <div class="news-grid">{highlights_html}</div>
    </section>

    <div class="quick-links">
        <div class="section-header" style="text-align: center;"><h2>🔗 快速連結</h2></div>
        <div class="quick-links-grid">
            <a href="index.html" class="quick-link-card"><i class="fas fa-home"></i><h4>返回首頁</h4></a>
            <a href="game-guide.html" class="quick-link-card"><i class="fas fa-gamepad"></i><h4>問劍長生</h4></a>
            <a href="saint-seiya-guide.html" class="quick-link-card"><i class="fas fa-star"></i><h4>聖鬥士</h4></a>
            <a href="beapro-football-guide.html" class="quick-link-card"><i class="fas fa-futbol"></i><h4>Be A Pro</h4></a>
            <a href="kai-tian-guide.html" class="quick-link-card"><i class="fas fa-khanda"></i><h4>開天攻略</h4></a>
            <a href="ai-news.html" class="quick-link-card"><i class="fas fa-robot"></i><h4>AI 資訊</h4></a>
        </div>
    </div>

    <div class="cta-section">
        <h3>💬 加入 TapTap 討論社群</h3>
        <p>有問題或想分享你的攻略心得？快來 TapTap 論壇與其他玩家交流！</p>
        <a href="{tap_tap_url}" target="_blank" class="cta-button">
            <i class="fas fa-comments"></i> 前往 TapTap 論壇
        </a>
    </div>

    <footer class="main-footer">
        <p>© 2026 大肥瞄．科技修真傳．{game_name}攻略中心</p>
    </footer>
</body>
</html>'''

def main():
    config = load_config()
    for key, cfg in config["update_schedule"].items():
        if cfg.get("enabled"):
            html = generate_html(key, cfg)
            outfile = REPO_DIR / cfg["file"]
            with open(outfile, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✅ {cfg['file']}")

if __name__ == "__main__":
    print("🚀 生成攻略頁面...")
    main()
    print("✅ 完成！")
