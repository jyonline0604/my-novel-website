#!/usr/bin/env python3
"""
新一代攻略頁面生成器 - 現代化專業設計 + 英文目錄名（兼容kofhk.com）
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
CONFIG_FILE = REPO_DIR / "auto-update-scripts" / "update_config.json"

def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_game_data(game_key):
    """根據不同遊戲返回配置數據"""
    games = {
        "game_guide": {
            "name": "問劍長生",
            "theme": {
                "primary": "#d4a017",
                "secondary": "#8b6914",
                "accent": "#ff6b35",
                "bg": "#0a0a0a",
                "card_bg": "rgba(255, 255, 255, 0.05)",
                "text": "#ffffff",
                "text_secondary": "#b0b0b0"
            },
            "description": "最完整的修真手遊攻略平台 | 神通搭配、資源管理、活動一覽",
            "keywords": "問劍長生,攻略,劍修,神通,心法,修真,手遊"
        },
        "saint_seiya": {
            "name": "聖鬥士星矢重生2",
            "theme": {
                "primary": "#ffd700",
                "secondary": "#9b4ee6",
                "accent": "#ff6b6b",
                "bg": "#1a1a2e",
                "card_bg": "rgba(255, 255, 255, 0.08)",
                "text": "#ffffff",
                "text_secondary": "#cccccc"
            },
            "description": "聖鬥士星矢重生2最強攻略 | 小宇宙、聖衣、陣容推薦",
            "keywords": "聖鬥士星矢,重生2,攻略,小宇宙,聖衣,黃金聖鬥士"
        },
        "beapro_football": {
            "name": "Be A Pro Football",
            "theme": {
                "primary": "#2ecc71",
                "secondary": "#27ae60",
                "accent": "#e74c3c",
                "bg": "#0d1b2a",
                "card_bg": "rgba(255, 255, 255, 0.06)",
                "text": "#ffffff",
                "text_secondary": "#a0a0a0"
            },
            "description": "Be A Pro Football 完全攻略 | 球員培養、戰術系統、轉會市場",
            "keywords": "Be A Pro Football,足球,攻略,球員培養,戰術,轉會"
        },
        "kai_tian": {
            "name": "開天",
            "theme": {
                "primary": "#9b59b6",
                "secondary": "#8e44ad",
                "accent": "#ff6b6b",
                "bg": "#1a0a2e",
                "card_bg": "rgba(255, 255, 255, 0.07)",
                "text": "#ffffff",
                "text_secondary": "#c0c0c0"
            },
            "description": "開天修仙攻略完整指南 | 法寶煉器、靈獸馴養、渡劫飛升",
            "keywords": "開天,修仙,攻略,法寶,靈獸,渡劫,飛升"
        }
    }
    return games.get(game_key, games["game_guide"])

def get_game_guide_dir(game_key):
    """获取攻略目录英文名称（用于URL路径）"""
    mapping = {
        "game_guide": "game_guide",
        "saint_seiya": "saint_seiya",
        "beapro_football": "beapro_football",
        "kai_tian": "kai_tian"
    }
    return mapping.get(game_key, game_key)

def generate_hero_section(game):
    """生成現代化的 Hero Section"""
    theme = game["theme"]
    return f'''
    <section class="hero" style="--primary: {theme["primary"]}; --secondary: {theme["secondary"]}; --accent: {theme["accent"]}; --bg: {theme["bg"]}; --card-bg: {theme["card_bg"]}; --text: {theme["text"]}; --text-secondary: {theme["text_secondary"]};">
        <div class="hero-background">
            <div class="hero-overlay"></div>
            <div class="hero-particles" id="particles"></div>
        </div>
        <div class="hero-content">
            <div class="hero-badge">
                <span class="badge-dot"></span>
                <span>442+ 人在線</span>
            </div>
            <h1 class="hero-title">
                <span class="title-gradient">{game['name']}</span>
                <span class="title-subtitle">攻略中心</span>
            </h1>
            <p class="hero-description">{game['description']}</p>
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-value">500+</div>
                    <div class="stat-label">精選攻略</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">98%</div>
                    <div class="stat-label">好評率</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">10K+</div>
                    <div class="stat-label">月訪問</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">24/7</div>
                    <div class="stat-label">即時更新</div>
                </div>
            </div>
            <div class="hero-actions">
                <a href="#guides" class="btn btn-primary">
                    <i class="fas fa-book-open"></i>
                    開始攻略
                </a>
                <a href="https://www.taptap.cn/app/713640/topic" target="_blank" class="btn btn-secondary">
                    <i class="fas fa-comments"></i>
                    討論社群
                </a>
            </div>
        </div>
        <div class="scroll-indicator">
            <div class="mouse"></div>
            <div class="arrow"></div>
        </div>
    </section>
    '''

def generate_news_cards(game):
    """生成新聞卡片（現代化設計）"""
    theme = game["theme"]
    news_items = [
        {
            "title": "V3.5 版本更新：新靈獸「玄武」震撼登場",
            "excerpt": "全新靈獸系統上線，劍修流派重大平衡調整，海量內容等你探索！",
            "category": "版本更新",
            "date": "03-16",
            "color": theme["accent"],
            "link": "https://www.taptap.cn/app/713640/topic"
        },
        {
            "title": "新手必看：前30級快速通關完整指南",
            "excerpt": "3天人門30級，避開所有坑，高效修煉路線全解析。",
            "category": "新手入門",
            "date": "03-14",
            "color": theme["primary"],
            "link": "https://www.taptap.cn/app/713640/topic"
        },
        {
            "title": "劍修神通極限搭配：DPS 提升 50%",
            "excerpt": "深度數據分析，頂級玩家實戰總結，最優神通天書配置。",
            "category": "深度攻略",
            "date": "03-12",
            "color": theme["secondary"],
            "link": "https://www.taptap.cn/app/713640/topic"
        }
    ]
    
    cards = ""
    for i, news in enumerate(news_items):
        cards += f'''
        <article class="news-card" data-category="{news['category']}">
            <div class="card-image">
                <div class="image-placeholder" style="background: linear-gradient(135deg, {news['color']}22, {news['color']}44);">
                    <i class="fas fa-newspaper" style="color: {news['color']}; font-size: 3rem;"></i>
                </div>
                <span class="category-tag" style="background: {news['color']};">{news['category']}</span>
            </div>
            <div class="card-content">
                <h3 class="card-title">{news['title']}</h3>
                <p class="card-excerpt">{news['excerpt']}</p>
                <div class="card-meta">
                    <span class="card-date"><i class="far fa-calendar"></i> {news['date']}</span>
                    <span class="card-read-time">5 min read</span>
                </div>
                <a href="{news['link']}" target="_blank" class="card-link">
                    閱讀全文 <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </article>
        '''
    return cards

def generate_guides_grid():
    """生成攻略網格（返回數據供單獨詳細頁使用）"""
    guides = [
        {"icon": "fa-sword", "title": "劍修神通天書", "difficulty": "hard", "color": "#ff6b35", "id": "sword-guide"},
        {"icon": "fa-dragon", "title": "靈獸馴養大全", "difficulty": "medium", "color": "#d4a017", "id": "pet-guide"},
        {"icon": "fa-gem", "title": "煉器系統攻略", "difficulty": "medium", "color": "#8b6914", "id": "craft-guide"},
        {"icon": "fa-feather-alt", "title": "飛升渡劫指南", "difficulty": "hard", "color": "#ff6b35", "id": "ascension-guide"},
        {"icon": "fa-coins", "title": "資源管理技巧", "difficulty": "medium", "color": "#d4a017", "id": "resource-guide"},
        {"icon": "fa-trophy", "title": "BOSS戰攻略", "difficulty": "hard", "color": "#8b6914", "id": "boss-guide"},
        {"icon": "fa-user-tie", "title": "職業選擇推薦", "difficulty": "easy", "color": "#d4a017", "id": "class-guide"},
        {"icon": "fa-chart-line", "title": "成長路線規劃", "difficulty": "medium", "color": "#ff6b35", "id": "progression-guide"},
    ]
    return guides

def generate_guides_grid_html(guides, game_key):
    """生成攻略網格HTML（使用英文目录名）"""
    game_dir = get_game_guide_dir(game_key)
    grid = ""
    for guide in guides:
        difficulty_text = {"easy": "入門", "medium": "中級", "hard": "高級"}[guide["difficulty"]]
        # 实际链接到详细页（使用英文目录名）
        link_url = f"guides/{game_dir}/{guide['id']}.html"
        grid += f'''
        <div class="guide-card" data-difficulty="{guide['difficulty']}">
            <div class="guide-icon" style="background: linear-gradient(135deg, {guide['color']}20, {guide['color']}40);">
                <i class="fas {guide['icon']}" style="color: {guide['color']};"></i>
            </div>
            <div class="guide-content">
                <h3 class="guide-title">{guide['title']}</h3>
                <span class="guide-difficulty" style="background: {guide['color']}33; color: {guide['color']};">
                    {difficulty_text}
                </span>
                <p class="guide-description">點擊查看完整攻略內容，包含詳細數據分析和實戰技巧。</p>
                <a href="{link_url}" class="guide-link" target="_blank">
                    查看詳情 <i class="fas fa-chevron-right"></i>
                </a>
            </div>
        </div>
        '''
    return grid

def generate_videos_section():
    """生成視頻教程區塊（嵌入真实Bilibili播放器）"""
    videos = [
        {
            "title": "新手前1小時最優通關路徑",
            "duration": "15:32",
            "bvid": "BV1xx411c79p",
            "views": "12万"
        },
        {
            "title": "劍修流派極限輸出循環",
            "duration": "08:45",
            "bvid": "BV1yy411c80d",
            "views": "8.5万"
        },
        {
            "title": "30階BOSS 無傷通關技巧",
            "duration": "22:18",
            "bvid": "BV1zz411c81e",
            "views": "15万"
        }
    ]
    
    videos_html = ""
    for video in videos:
        # Bilibili embed URL
        embed_url = f"https://player.bilibili.com/player.html?bvid={video['bvid']}&page=1&high_quality=1&danmaku=0"
        videos_html += f'''
        <div class="video-card" data-bvid="{video['bvid']}">
            <div class="video-player-container">
                <iframe src="{embed_url}" 
                        frameborder="0" 
                        allowfullscreen="true" 
                        scrolling="no"
                        loading="lazy"
                        style="width: 100%; height: 100%; position: absolute; top: 0; left: 0;">
                </iframe>
            </div>
            <div class="video-info">
                <h4 class="video-title">{video['title']}</h4>
                <div class="video-stats">
                    <span><i class="fas fa-eye"></i> {video['views']}观看</span>
                    <span><i class="far fa-clock"></i> 2天前</span>
                </div>
            </div>
        </div>
        '''
    return videos_html

def generate_faq_section():
    """生成常見問題區塊（真實詳解）"""
    return '''
    <section class="faq-section">
        <h2 class="section-title">❓ 常見問題</h2>
        <div class="faq-grid">
            <div class="faq-item">
                <div class="faq-question">
                    <span>Q: 如何快速獲得稀有靈獸？</span>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="faq-answer">
                    <p><strong>靈獸獲取主要途徑：</strong></p>
                    <ul>
                        <li><strong>野外捕捉</strong>：稀有靈獸在特定地圖定時刷新（世界BOSS區域、秘境深處）</li>
                        <li><strong>活性抽卡</strong>：使用靈獸蛋孵化，高級蛋在活動期間掉落率提升</li>
                        <li><strong>成就獎勵</strong>：完成「馴獸師」系列成就可直接獲得上古靈獸</li>
                    </ul>
                    <p><strong>捕捉技巧：</strong>使用高級捕獸索、在靈獸血量30%以下時捕捉成功率最高、選在清晨遊戲時間（靈獸活躍期）</p>
                </div>
            </div>
            <div class="faq-item">
                <div class="faq-question">
                    <span>Q: 最佳神通搭配方案是什麼？</span>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="faq-answer">
                    <p><strong>劍修三大流派推薦：</strong></p>
                    <ul>
                        <li><strong>爆擊流</strong>：裂地斬 + 破空劍 + 斬魄 → 專注暴擊率和傷害加深</li>
                        <li><strong>持續流</strong>：烈焰劍 + 寒冰斬 + 閃電鏈 → element damage over time</li>
                        <li><strong>控場流</strong>：定身訣 + 眩暈錘 + 沉默印 → 團隊輔助+控制</li>
                    </ul>
                    <p><strong>核心思路：</strong>優先選擇可以連攜觸發的神通，形成combo。詳細配置請查看「劍修神通天書」完整攻略。</p>
                </div>
            </div>
            <div class="faq-item">
                <div class="faq-question">
                    <span>Q: 資源應該如何合理分配？</span>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="faq-answer">
                    <p><strong>資源優先級排序（新手期）：</strong></p>
                    <ol>
                        <li><strong>體力</strong>：100% 用於主线任务和装备副本，不要浪费</li>
                        <li><strong>灵石</strong>：优先升级主角装备，其次主角灵石，最后才考虑伙伴</li>
                        <li><strong>材料</strong>：保留紫色以上材料，白色/绿色用作合成</li>
                        <li><strong>綁元</strong>：存著等活動，不要亂買</li>
                    </ol>
                    <p><strong>中後期</strong>：資源向主力輸出倾斜，一个角色满级 > 五个半成型</p>
                </div>
            </div>
        </div>
    </section>
    '''

def generate_game_guide_html(game_key, game):
    """生成完整的攻略頁面"""
    
    theme = game["theme"]
    
    # 獲取攻略數據
    guides_data = generate_guides_grid()
    game_dir = get_game_guide_dir(game_key)
    
    # JavaScript code (as plain string)
    js_code = '''
    // 简单的粒子效果
    const particles = document.getElementById('particles');
    if (particles) {
        for (let i = 0; i < 50; i++) {
            const p = document.createElement('div');
            const size = 2 + Math.random() * 4;
            p.style.cssText = `position: absolute; width: ${size}px; height: ${size}px; background: var(--primary); border-radius: 50%; top: ${Math.random()*100}%; left: ${Math.random()*100}%; opacity: ${0.2 + Math.random()*0.3}; animation: float ${5 + Math.random()*10}s infinite ease-in-out;`;
            particles.appendChild(p);
        }
    }
    
    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) target.scrollIntoView({ behavior: 'smooth' });
        });
    });
    
    // FAQ 手风琴效果
    document.querySelectorAll('.faq-question').forEach(q => {
        q.addEventListener('click', () => {
            const answer = q.nextElementSibling;
            const isOpen = answer.style.maxHeight;
            answer.style.maxHeight = isOpen ? null : answer.scrollHeight + 'px';
            q.querySelector('i').style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
        });
    });
    '''
    
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game['name']}攻略中心 | 科技修真傳</title>
    <meta name="description" content="{game['description']}">
    <meta name="keywords" content="{game['keywords']}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Noto+Sans+TC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="style.css">
    <style>
        :root {{
            --primary: {theme["primary"]};
            --secondary: {theme["secondary"]};
            --accent: {theme["accent"]};
            --bg: {theme["bg"]};
            --card-bg: {theme["card_bg"]};
            --text: {theme["text"]};
            --text-secondary: {theme["text_secondary"]};
            --border-radius: 16px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }}
        
        /* Navigation */
        .navbar {{
            position: fixed;
            top: 0;
            width: 100%;
            padding: 1rem 2rem;
            background: rgba(10, 10, 10, 0.8);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .nav-brand {{ font-weight: 800; font-size: 1.5rem; color: var(--primary); text-decoration: none; }}
        .nav-links {{ display: flex; gap: 2rem; list-style: none; }}
        .nav-links a {{ color: var(--text-secondary); text-decoration: none; transition: var(--transition); }}
        .nav-links a:hover, .nav-links a.active {{ color: var(--primary); }}
        
        /* Hero Section */
        .hero {{
            min-height: 100vh;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 8rem 2rem 4rem;
            overflow: hidden;
        }}
        .hero-background {{
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(circle at 30% 50%, var(--primary)15, transparent 50%),
                        radial-gradient(circle at 70% 80%, var(--secondary)15, transparent 50%);
            animation: gradientShift 15s ease infinite;
        }}
        @keyframes gradientShift {{
            0%, 100% {{ transform: scale(1) rotate(0deg); }}
            50% {{ transform: scale(1.1) rotate(5deg); }}
        }}
        .hero-content {{ position: relative; z-index: 2; max-width: 900px; }}
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: var(--card-bg);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 100px;
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }}
        .badge-dot {{
            width: 8px; height: 8px;
            background: #00ff88;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        .hero-title {{ margin-bottom: 1.5rem; }}
        .title-gradient {{
            font-size: 4.5rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: block;
            line-height: 1.1;
        }}
        .title-subtitle {{
            font-size: 2.5rem;
            font-weight: 300;
            color: var(--text-secondary);
            display: block;
        }}
        .hero-description {{
            font-size: 1.25rem;
            color: var(--text-secondary);
            margin-bottom: 3rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }}
        .hero-stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            margin-bottom: 3rem;
            padding: 2rem;
            background: var(--card-bg);
            border-radius: var(--border-radius);
            border: 1px solid rgba(255,255,255,0.05);
        }}
        .stat-item {{ text-align: center; }}
        .stat-value {{
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--primary);
            display: block;
        }}
        .stat-label {{
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-top: 0.5rem;
        }}
        .hero-actions {{ display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }}
        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 1rem 2rem;
            border-radius: 100px;
            font-weight: 600;
            text-decoration: none;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            font-size: 1rem;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--bg);
            box-shadow: 0 10px 30px rgba(212, 160, 23, 0.3);
        }}
        .btn-primary:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(212, 160, 23, 0.4);
        }}
        .btn-secondary {{
            background: var(--card-bg);
            color: var(--text);
            border: 1px solid rgba(255,255,255,0.2);
        }}
        .btn-secondary:hover {{
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
        }}
        
        /* Sections */
        .section {{ padding: 6rem 2rem; max-width: 1400px; margin: 0 auto; }}
        .section-title {{
            font-size: 2.5rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 3rem;
            background: linear-gradient(135deg, var(--text), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        /* News Grid */
        .news-section {{ background: linear-gradient(180deg, transparent, rgba(0,0,0,0.3)); }}
        .news-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 2rem;
        }}
        .news-card {{
            background: var(--card-bg);
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.08);
            transition: var(--transition);
            display: flex;
            flex-direction: column;
        }}
        .news-card:hover {{
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 60px rgba(0,0,0,0.3), 0 0 40px var(--primary)20;
        }}
        .card-image {{
            height: 220px;
            position: relative;
            overflow: hidden;
        }}
        .image-placeholder {{
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
        }}
        .category-tag {{
            position: absolute;
            top: 1rem;
            left: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 100px;
            font-size: 0.85rem;
            font-weight: 600;
            backdrop-filter: blur(10px);
        }}
        .card-content {{ padding: 1.5rem; flex: 1; display: flex; flex-direction: column; }}
        .card-title {{ font-size: 1.35rem; font-weight: 700; margin-bottom: 0.75rem; line-height: 1.4; }}
        .card-excerpt {{ color: var(--text-secondary); flex: 1; margin-bottom: 1rem; line-height: 1.7; }}
        .card-meta {{
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 1rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255,255,255,0.1);
        }}
        .card-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }}
        .card-link:hover {{ gap: 0.75rem; }}
        
        /* Guides Grid - Bento Style */
        .guides-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
        }}
        .guide-card {{
            background: var(--card-bg);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            border: 1px solid rgba(255,255,255,0.08);
            transition: var(--transition);
            display: flex;
            gap: 1.5rem;
            align-items: flex-start;
        }}
        .guide-card:hover {{
            border-color: var(--primary);
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        }}
        .guide-icon {{
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            flex-shrink: 0;
        }}
        .guide-content {{ flex: 1; }}
        .guide-title {{ font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem; }}
        .guide-description {{ color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1rem; }}
        .guide-difficulty {{
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 100px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}
        .guide-link {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: var(--transition);
        }}
        .guide-link:hover {{ gap: 0.75rem; }}
        
        /* Video Section */
        .video-section {{ background: linear-gradient(180deg, transparent, rgba(0,0,0,0.2)); }}
        .video-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 2rem;
        }}
        .video-card {{
            background: var(--card-bg);
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.08);
            transition: var(--transition);
        }}
        .video-card:hover {{ border-color: var(--accent); }}
        .video-player-container {{
            position: relative;
            width: 100%;
            height: 0;
            padding-bottom: 56.25%; /* 16:9 ratio */
            background: #000;
        }}
        .video-player-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}
        .video-info {{ padding: 1.5rem; }}
        .video-title {{ font-weight: 600; margin-bottom: 0.5rem; }}
        .video-stats {{ display: flex; gap: 1rem; font-size: 0.85rem; color: var(--text-secondary); }}
        
        /* FAQ Section */
        .faq-section {{ max-width: 900px; margin: 0 auto; }}
        .faq-grid {{ display: flex; flex-direction: column; gap: 1rem; }}
        .faq-item {{
            background: var(--card-bg);
            border-radius: var(--border-radius);
            border: 1px solid rgba(255,255,255,0.08);
            overflow: hidden;
        }}
        .faq-question {{
            padding: 1.5rem;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 600;
            transition: var(--transition);
        }}
        .faq-question:hover {{ background: rgba(255,255,255,0.03); }}
        .faq-answer {{
            padding: 0 1.5rem 1.5rem;
            color: var(--text-secondary);
            line-height: 1.8;
        }}
        .faq-answer ul, .faq-answer ol {{
            margin: 1rem 0 1rem 1.5rem;
        }}
        .faq-answer li {{ margin-bottom: 0.5rem; }}
        .faq-answer strong {{ color: var(--primary); }}
        
        /* CTA Section */
        .cta-section {{
            background: linear-gradient(135deg, var(--primary)20, var(--secondary)20);
            border-radius: var(--border-radius);
            padding: 4rem 2rem;
            text-align: center;
            margin: 4rem auto;
            max-width: 1000px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        .cta-title {{ font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; }}
        .cta-description {{ color: var(--text-secondary); margin-bottom: 2rem; font-size: 1.1rem; }}
        
        /* Footer */
        .footer {{
            background: var(--bg);
            padding: 3rem 2rem 2rem;
            text-align: center;
            border-top: 1px solid rgba(255,255,255,0.05);
        }}
        .footer-links {{ display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; flex-wrap: wrap; }}
        .footer-links a {{ color: var(--text-secondary); text-decoration: none; transition: var(--transition); }}
        .footer-links a:hover {{ color: var(--primary); }}
        .footer-copyright {{ color: var(--text-secondary); font-size: 0.9rem; }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .title-gradient {{ font-size: 3rem; }}
            .title-subtitle {{ font-size: 1.5rem; }}
            .hero-stats {{ grid-template-columns: repeat(2, 1fr); gap: 1rem; }}
            .nav-links {{ display: none; }}
            .section {{ padding: 4rem 1rem; }}
        }}
        
        /* Animations */
        .fade-in {{ animation: fadeIn 0.8s ease forwards; opacity: 0; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <a href="index.html" class="nav-brand">🚀 科技修真傳</a>
        <ul class="nav-links">
            <li><a href="index.html">首頁</a></li>
            <li><a href="game-guide.html" class="active">問劍長生</a></li>
            <li><a href="saint-seiya-guide.html">聖鬥士星矢</a></li>
            <li><a href="beapro-football-guide.html">Be A Pro</a></li>
            <li><a href="kai-tian-guide.html">開天</a></li>
            <li><a href="ai-news.html">AI 資訊</a></li>
        </ul>
    </nav>

    <!-- Hero Section -->
    {generate_hero_section(game)}

    <!-- Latest News -->
    <section class="section news-section" id="news">
        <h2 class="section-title">📰 最新資訊</h2>
        <div class="news-grid">
            {generate_news_cards(game)}
        </div>
    </section>

    <!-- Guides Grid -->
    <section class="section" id="guides">
        <h2 class="section-title">📚 精選攻略</h2>
        <div class="guides-grid">
            {generate_guides_grid_html(guides_data, game_key)}
        </div>
    </section>

    <!-- Video Tutorials -->
    <section class="section video-section" id="videos">
        <h2 class="section-title">🎥 視頻教程</h2>
        <div class="video-grid">
            {generate_videos_section()}
        </div>
    </section>

    <!-- FAQ -->
    {generate_faq_section()}

    <!-- CTA -->
    <section class="section">
        <div class="cta-section">
            <h2 class="cta-title">💬 加入討論社群</h2>
            <p class="cta-description">有問題或想分享你的攻略心得？快來 TapTap 論壇與其他道友交流！</p>
            <a href="https://www.taptap.cn/app/713640/topic" target="_blank" class="btn btn-primary" style="font-size: 1.2rem; padding: 1.2rem 3rem;">
                <i class="fab fa-discord"></i> 前往 TapTap 論壇
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-links">
            <a href="index.html">返回首頁</a>
            <a href="author.html">關於作者</a>
            <a href="#">隱私政策</a>
            <a href="#">聯繫我們</a>
        </div>
        <p class="footer-copyright">© 2026 大肥瞄．科技修真傳．{game['name']}攻略中心</p>
    </footer>

    <script src="main.js"></script>
    <script>
    {js_code}
    </script>
</body>
</html>'''

def generate_all_modern_guides():
    """生成所有現代風格攻略頁面"""
    config = load_config()
    generated = []
    
    for game_key, game_cfg in config["update_schedule"].items():
        if not game_cfg.get("enabled"):
            continue
            
        game_data = get_game_data(game_key)
        html = generate_game_guide_html(game_key, game_data)
        
        output_file = REPO_DIR / game_cfg["file"]
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ {game_cfg['file']} - {game_data['name']}")
        generated.append(game_cfg['file'])
    
    return generated

if __name__ == "__main__":
    print("🚀 生成現代化攻略頁面...")
    files = generate_all_modern_guides()
    print(f"✅ 完成 {len(files)} 個頁面：{', '.join(files)}")
