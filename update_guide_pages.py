#!/usr/bin/env python3
"""
攻略頁面自動更新腳本
每天自動更新遊戲攻略頁面內容
"""

import os
import json
import random
from datetime import datetime

WORKSPACE = "/home/openclaw/.openclaw/workspace/my-novel-website"

def generate_guide_content(game_name, game_key):
    """生成攻略內容"""
    
    # 遊戲相關的新聞/攻略
    news_templates = [
        f"【攻略】{game_name}最新玩法技巧，助你快速上手！",
        f"【活動】{game_name}限定活動火熱進行中，豐富獎勵等你來拿！",
        f"【更新】{game_name}版本更新內容一覽，新角色強勢登場！",
        f"【攻略】{game_name}副本通關技巧分享，最高難度輕鬆過！",
        f"【數據】{game_name}角色強度排行榜出爐，最強角色是它！",
        f"【攻略】{game_name}裝備強化攻略，讓你的角色戰力飆升！",
        f"【活動】{game_name}登錄獎勵升級，最多可獲得千元虛寶！",
    ]
    
    guides = [
        {
            "title": "新手入門攻略",
            "difficulty": "簡單",
            "icon": "fa-star",
            "content": "對於新手玩家，首先要注意的是資源的合理分配...",
            "category": "基礎"
        },
        {
            "title": "高效升級技巧",
            "difficulty": "中等",
            "icon": "fa-level-up-alt",
            "content": "想要快速升級，每日任務和活動是關鍵...",
            "category": "進階"
        },
        {
            "title": "最強角色推薦",
            "difficulty": "困難",
            "icon": "fa-crown",
            "content": "根據最新版本數據，以下角色在當前版本表現最強...",
            "category": "高級"
        },
        {
            "title": "裝備強化指南",
            "difficulty": "中等",
            "icon": "fa-shield-alt",
            "content": "裝備強化是提升戰力的重要途徑...",
            "category": "進階"
        },
        {
            "title": "副本通關攻略",
            "difficulty": "困難",
            "icon": "fa-dungeon",
            "content": "高級副本需要團隊配合和正確的策略...",
            "category": "高級"
        },
        {
            "title": "PVP對戰技巧",
            "difficulty": "困難",
            "icon": "fa-crosshairs",
            "content": "在PVP中取得勝利需要了解各角色的技能...",
            "category": "對戰"
        }
    ]
    
    activities = [
        {"title": "限定抽卡活動", "reward": "保底SSR角色", "date": "即日起至3月底"},
        {"title": "登錄送好禮", "reward": "1000鑽石", "date": "持續進行中"},
        {"title": "公會戰", "reward": "專屬稱號", "date": "每週六、日"}
    ]
    
    return {
        "news": random.sample(news_templates, 3),
        "guides": guides,
        "activities": activities,
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

def update_guide_page(filename, game_name, game_key):
    """更新單個攻略頁面"""
    
    data = generate_guide_content(game_name, game_key)
    
    news_html = ""
    for i, news in enumerate(data["news"]):
        news_html += f'''
            <div class="news-card">
                <div class="news-icon">📰</div>
                <div class="news-content">
                    <h4>{news}</h4>
                    <p class="news-meta">{game_name} · 2小時前</p>
                </div>
            </div>'''
    
    guides_html = ""
    for guide in data["guides"]:
        color = {"簡單": "#4CAF50", "中等": "#FF9800", "困難": "#F44336"}.get(guide["difficulty"], "#2196F3")
        guides_html += f'''
            <div class="guide-card">
                <div class="guide-header">
                    <i class="fas {guide['icon']}"></i>
                    <h3>{guide['title']}</h3>
                </div>
                <div class="guide-meta">
                    <span class="difficulty" style="background: {color}">{guide['difficulty']}</span>
                    <span class="category">{guide['category']}</span>
                </div>
                <p class="guide-desc">{guide['content']}</p>
                <a href="#" class="read-more">閱讀攻略 <i class="fas fa-arrow-right"></i></a>
            </div>'''
    
    activities_html = ""
    for act in data["activities"]:
        activities_html += f'''
            <div class="activity-card">
                <div class="activity-icon">🎁</div>
                <div class="activity-info">
                    <h4>{act['title']}</h4>
                    <p>獎勵：{act['reward']} · {act['date']}</p>
                </div>
            </div>'''
    
    # 讀取現有頁面
    filepath = f"{WORKSPACE}/{filename}"
    if not os.path.exists(filepath):
        print(f"❌ {filename} not found")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新最後更新時間
    content = content.replace(
        '最後更新：',
        f'最後更新：{data["last_update"]}'
    )
    
    # 簡單替換內容區塊
    if '<!-- NEWS_PLACEHOLDER -->' in content:
        content = content.replace('<!-- NEWS_PLACEHOLDER -->', news_html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {filename}")
    return True

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting guide pages update...")
    
    guides = [
        ("game-guide.html", "問劍長生", "wenjian"),
        ("saint-seiya-guide.html", "聖鬥士星矢", "saint"),
        ("beapro-football-guide.html", "Be A Pro", "beapro"),
        ("kai-tian-guide.html", "開天", "kaitian")
    ]
    
    for filename, game_name, game_key in guides:
        update_guide_page(filename, game_name, game_key)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Guide pages update complete!")

if __name__ == "__main__":
    main()
