#!/usr/bin/env python3
"""
新一代攻略页面生成器 - 每个游戏都有独特设计
"""

import json
from pathlib import Path

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
CONFIG_FILE = REPO_DIR / "auto-update-scripts" / "update_config.json"

def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_game_data(game_key):
    """返回游戏数据 + 设计配置"""
    games = {
        "game_guide": {
            "name": "問劍長生",
            "theme": {
                "primary": "#d4a017",
                "secondary": "#8b6914",
                "accent": "#ff6b35",
                "bg": "#0a0a0a",
                "card_bg": "rgba(255,255,255,0.05)",
                "text": "#ffffff",
                "text_sec": "#b0b0b0",
                "gradient": "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)"
            },
            "design": {
                "style": "cyberpunk",
                "hero_type": "particles",
                "card_shape": "rounded",
                "accent_element": "glow"
            }
        },
        "saint_seiya": {
            "name": "聖鬥士星矢重生2",
            "theme": {
                "primary": "#ffd700",
                "secondary": "#9b4ee6",
                "accent": "#ff6b6b",
                "bg": "#1a1a2e",
                "card_bg": "rgba(255,255,255,0.08)",
                "text": "#ffffff",
                "text_sec": "#cccccc",
                "gradient": "radial-gradient(circle at 50% 50%, #2d1b69, #0f0c29)"
            },
            "design": {
                "style": "cosmic",
                "hero_type": "constellation",
                "card_shape": "hexagon",
                "accent_element": "stars"
            }
        },
        "beapro_football": {
            "name": "Be A Pro Football",
            "theme": {
                "primary": "#2ecc71",
                "secondary": "#27ae60",
                "accent": "#e74c3c",
                "bg": "#0d1b2a",
                "card_bg": "rgba(255,255,255,0.06)",
                "text": "#ffffff",
                "text_sec": "#a0a0a0",
                "gradient": "linear-gradient(180deg, #1b4332 0%, #0d1b2a 100%)"
            },
            "design": {
                "style": "stadium",
                "hero_type": "field",
                "card_shape": "badge",
                "accent_element": "lines"
            }
        },
        "kai_tian": {
            "name": "開天",
            "theme": {
                "primary": "#9b59b6",
                "secondary": "#8e44ad",
                "accent": "#ff6b6b",
                "bg": "#1a0a2e",
                "card_bg": "rgba(255,255,255,0.07)",
                "text": "#ffffff",
                "text_sec": "#c0c0c0",
                "gradient": "linear-gradient(45deg, #2c003e, #512b58, #8e44ad)"
            },
            "design": {
                "style": "ethereal",
                "hero_type": "clouds",
                "card_shape": "floating",
                "accent_element": "aurora"
            }
        }
    }
    return games.get(game_key, games["game_guide"])

def get_game_guide_dir(game_key):
    mapping = {"game_guide": "game_guide", "saint_seiya": "saint_seiya", "beapro_football": "beapro_football", "kai_tian": "kai_tian"}
    return mapping.get(game_key, game_key)

def generate_hero_section(game):
    """为每个游戏生成不同风格的 Hero"""
    theme = game["theme"]
    name = game["name"]
    design = game["design"]
    
    if design["hero_type"] == "field":
        # Be A Pro Football: 足球场风格
        return f'''
        <section class="hero football-hero" style="--primary: {theme["primary"]}; --bg: {theme["bg"]}; --card-bg: {theme["card_bg"]}; --text: {theme["text"]}; --text-sec: {theme["text_sec"]};">
            <div class="field-lines"></div>
            <div class="hero-content">
                <div class="score-board">
                    <span class="team-name"> tactical</span>
                    <span class="score">4 - 2</span>
                    <span class="team-name"> formation</span>
                </div>
                <h1 class="hero-title">{name}</h1>
                <p class="hero-subtitle">打造冠军阵容 | 战术大师指南</p>
                <div class="hero-stats" style="display: flex; gap: 2rem; justify-content: center; margin: 2rem 0;">
                    <div class="stat"><strong>100+</strong><br><small>战术配置</small></div>
                    <div class="stat"><strong>50K+</strong><br><small>玩家使用</small></div>
                    <div class="stat"><strong>4.9</strong><br><small>用户评分</small></div>
                </div>
                <a href="#guides" class="btn-primary">开始攻略</a>
            </div>
        </section>
        '''
    elif design["hero_type"] == "constellation":
        # 圣斗士：星空风格
        return f'''
        <section class="hero constellation-hero" style="--primary: {theme["primary"]}; --bg: {theme["bg"]}; --card-bg: {theme["card_bg"]}; --text: {theme["text"]}; --text-sec: {theme["text_sec"]};">
            <div class="zodiac-wheel"></div>
            <div class="hero-content">
                <h1 class="cosmic-title">{name}</h1>
                <p class="cosmic-subtitle">燃烧小宇宙 · 黄金圣斗士之路</p>
                <div class="constellation-stats">
                    <div class="stat"><span class="num">12</span><span class="lab">黄金星座</span></div>
                    <div class="stat"><span class="num">88</span><span class="lab">总星座数</span></div>
                    <div class="stat"><span class="num">∞</span><span class="lab">潜能上限</span></div>
                </div>
                <a href="#guides" class="cosmic-btn">展开圣域</a>
            </div>
        </section>
        '''
    elif design["hero_type"] == "clouds":
        # 开天：仙侠云雾风格
        return f'''
        <section class="hero cloud-hero" style="--primary: {theme["primary"]}; --bg: {theme["bg"]}; --card-bg: {theme["card_bg"]}; --text: {theme["text"]}; --text-sec: {theme["text_sec"]};">
            <div class="floating-clouds"></div>
            <div class="hero-content">
                <div class="daoist-badge">☯</div>
                <h1 class="daoist-title">{name}</h1>
                <p class="daoist-subtitle">修真飞升 · 渡劫成仙</p>
                <div class="cultivation-stats">
                    <div class="stat">筑基: <strong>100%</strong></div>
                    <div class="stat">金丹: <strong>85%</strong></div>
                    <div class="stat">元婴: <strong>60%</strong></div>
                    <div class="stat">渡劫: <strong>30%</strong></div>
                </div>
                <a href="#guides" class="dao-btn">开始修炼</a>
            </div>
        </section>
        '''
    else:
        # 默认：粒子风格（问剑长生）
        return f'''
        <section class="hero" style="--primary: {theme["primary"]}; --bg: {theme["bg"]}; --card-bg: {theme["card_bg"]}; --text: {theme["text"]}; --text-sec: {theme["text_sec"]};">
            <div class="hero-content">
                <h1 class="hero-title">{name}</h1>
                <p class="hero-description">最完整的攻略平台</p>
                <a href="#guides" class="btn btn-primary">开始攻略</a>
            </div>
        </section>
        '''

def generate_news_cards(game):
    """生成新闻卡片"""
    theme = game["theme"]
    name = game["name"]
    
    if "Football" in name:
        items = [
            {"title": "夏季转会窗口重磅交易一览", "excerpt": "顶级球星转会动态、球队阵容变动全记录", "cat": "转会动态", "color": theme["accent"]},
            {"title": "新版本战术系统深度解析", "excerpt": "4-3-3 vs 3-5-2 哪个更适合你？", "cat": "战术分析", "color": theme["primary"]},
            {"title": "青年球员培养完全指南", "excerpt": "如何打造下一代超级巨星？潜力评估 + 训练方案", "cat": "青训系统", "color": theme["secondary"]}
        ]
    elif "聖鬥士" in name:
        items = [
            {"title": "新黄金圣斗士『水瓶座』上线", "excerpt": "技能机制全解析，值得抽吗？", "cat": "版本更新", "color": theme["accent"]},
            {"title": "小宇宙燃烧极限配装推荐", "excerpt": "如何突破100万战力？装备搭配全攻略", "cat": "战力提升", "color": theme["primary"]},
            {"title": " Athenian 流派最强陣容", "excerpt": "十二宫排名赛T0队伍配置", "cat": "PVP攻略", "color": theme["secondary"]}
        ]
    else:
        items = [
            {"title": "V3.5 版本更新公告", "excerpt": "新灵兽、新副本、大量优化内容", "cat": "版本更新", "color": theme["accent"]},
            {"title": "新手必读：前30级快速攻略", "excerpt": "3天到满级，避开所有坑", "cat": "新手入门", "color": theme["primary"]},
            {"title": "门派技能极限搭配方案", "excerpt": "DPS提升50%的 secret combo", "cat": "深度攻略", "color": theme["secondary"]}
        ]
    
    html = ""
    for news in items:
        html += f'''
        <article class="news-card">
            <div class="card-image" style="background: linear-gradient(135deg, {news['color']}22, {news['color']}44);"></div>
            <div class="card-content">
                <h3>{news['title']}</h3>
                <p>{news['excerpt']}</p>
                <a href="https://www.taptap.cn/app/713640/topic" target="_blank" style="color: {theme["primary"]};">阅读全文 →</a>
            </div>
        </article>
        '''
    return html

def generate_guides_grid(game):
    """为每个游戏生成不同的攻略卡片"""
    name = game["name"]
    if "Football" in name:
        guides = [
            {"icon": "fa-users", "title": "战术阵型大全", "id": "formation"},
            {"icon": "fa-user-plus", "title": "球员培养指南", "id": "training"},
            {"icon": "fa-exchange-alt", "title": "转会市场攻略", "id": "transfer"},
            {"icon": "fa-chart-line", "title": "数据分析入门", "id": "analytics"},
            {"icon": "fa-trophy", "title": "冠军杯通关", "id": "cup"},
            {"icon": "fa-futbol", "title": "技巧训练场", "id": "skills"}
        ]
    elif "聖鬥士" in name:
        guides = [
            {"icon": "fa-star", "title": "小宇宙燃烧", "id": "cosmo"},
            {"icon": "fa-shield-alt", "title": "圣衣装备", "id": "armor"},
            {"icon": "fa-users-cog", "title": "阵容搭配", "id": "team"},
            {"icon": "fa-crown", "title": "黄金抽卡", "id": "gacha"},
            {"icon": "fa-fist-raised", "title": "竞技场攻略", "id": "pvp"},
            {"icon": "fa-dungeon", "title": "十二宫副本", "id": "temple"}
        ]
    else:
        guides = [
            {"icon": "fa-sword", "title": "剑修神通", "id": "sword"},
            {"icon": "fa-dragon", "title": "灵兽驯养", "id": "pet"},
            {"icon": "fa-gem", "title": "炼器系统", "id": "craft"},
            {"icon": "fa-feather-alt", "title": "飞升渡劫", "id": "ascend"},
            {"icon": "fa-coins", "title": "资源管理", "id": "resource"},
            {"icon": "fa-trophy", "title": "BOSS攻略", "id": "boss"}
        ]
    
    game_dir = get_game_guide_dir(get_game_key_by_name(name))
    grid = '<div class="guides-grid">'
    for g in guides:
        grid += f'''
        <a href="/guides/{game_dir}/{g['id']}.html" class="guide-card" style="border: 1px solid {theme["primary"]}33;">
            <i class="fas {g['icon']}" style="color: {theme["primary"]}; font-size: 1.5rem;"></i>
            <div>
                <h3>{g['title']}</h3>
                <a href="/guides/{game_dir}/{g['id']}.html" style="color: {theme["accent"]};">查看 →</a>
            </div>
        </a>
        '''
    grid += '</div>'
    return grid

def get_game_key_by_name(name):
    if "問劍" in name: return "game_guide"
    if "聖鬥士" in name: return "saint_seiya"
    if "Football" in name: return "beapro_football"
    return "kai_tian"

def generate_videos(game):
    name = game["name"]
    if "Football" in name:
        return '''
        <div class="video-embed"><iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen></iframe></div>
        '''
    else:
        return '''
        <div class="video-embed"><iframe src="https://player.bilibili.com/player.html?bvid=BV1xx411c79p" frameborder="0" allowfullscreen></iframe></div>
        '''

def generate_css(game):
    """为每个游戏生成独特的CSS"""
    theme = game["theme"]
    design = game["design"]
    
    base_css = f'''
    :root {{
        --primary: {theme["primary"]};
        --bg: {theme["bg"]};
        --card-bg: {theme["card_bg"]};
        --text: {theme["text"]};
        --text-sec: {theme["text_sec"]};
    }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); padding: 100px 2rem 2rem; max-width: 1200px; margin: 0 auto; }}
    .hero {{ text-align: center; padding: 4rem 0; margin-bottom: 3rem; background: {theme["gradient"]}; border-radius: 20px; }}
    .hero h1 {{ font-size: 3rem; margin-bottom: 1rem; color: var(--primary); }}
    .hero p {{ font-size: 1.2rem; color: var(--text-sec'); }}
    .section {{ margin: 3rem 0; }}
    .section h2 {{ font-size: 2rem; color: var(--primary); border-bottom: 2px solid var(--primary"); padding-bottom: 0.5rem; }}
    .news-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }}
    .news-card {{ background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border: 1px solid {theme["primary"]}22; }}
    .guides-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }}
    .guide-card {{ background: var(--card-bg); padding: 1.5rem; border-radius: 12px; display: flex; align-items: center; gap: 1rem; }}
    .guide-card i {{ font-size: 2rem; }}
    a {{ color: var(--primary"); text-decoration: none; }}
    a:hover {{ color: var(--accent"); }}
    '''
    
    # 添加游戏专属样式
    if design["style"] == "stadium":
        extra = '''
        .football-hero { position: relative; overflow: hidden; background: linear-gradient(180deg, #2d5a27 0%, #1a3518 100%); border: 4px solid #fff; }
        .field-lines { position: absolute; inset: 0; background: repeating-linear-gradient(90deg, transparent, transparent 49%, rgba(255,255,255,0.1) 50%, transparent 51%); }
        .score-board { background: rgba(0,0,0,0.5); color: #fff; padding: 1rem 2rem; border-radius: 10px; display: inline-flex; gap: 2rem; margin-bottom: 2rem; }
        .btn-primary { background: {theme["primary"]}; color: #000; padding: 1rem 2rem; border-radius: 50px; font-weight: bold; }
        '''
    elif design["style"] == "cosmic":
        extra = '''
        .constellation-hero { background: radial-gradient(circle at 50% 50%, #1a1a2e, #000); position: relative; }
        .zodiac-wheel { position: absolute; width: 600px; height: 600px; border: 2px dashed {theme["primary"]}; border-radius: 50%; opacity: 0.3; animation: rotate 60s linear infinite; }
        @keyframes rotate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
        .cosmic-title {{ font-size: 4rem; background: linear-gradient(to right, {theme["primary"]}, {theme["secondary"]}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        '''
    else:
        extra = ''
    
    return base_css + extra

def generate_html(game_key, game):
    game_dir = get_game_guide_dir(game_key)
    theme = game["theme"]
    
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>{game['name']}攻略中心</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
    {generate_css(game)}
    </style>
</head>
<body>
    {generate_hero_section(game)}
    
    <section class="section" id="news">
        <h2>📰 最新资讯</h2>
        <div class="news-grid">{generate_news_cards(game)}</div>
    </section>
    
    <section class="section" id="guides">
        <h2>📚 精选攻略</h2>
        {generate_guides_grid(game)}
    </section>
    
    <section class="section" id="videos">
        <h2>🎥 视频教程</h2>
        {generate_videos(game)}
    </section>
    
    <footer style="text-align: center; padding: 2rem; color: var(--text-sec"); margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.1);">
        <p>© 2026 大肥喵 · 科技修真传</p>
    </footer>
</body>
</html>'''

def generate_all():
    config = load_config()
    for game_key, game_cfg in config["update_schedule"].items():
        if not game_cfg.get("enabled"): continue
        game_data = get_game_data(game_key)
        html = generate_html(game_key, game_data)
        output = REPO_DIR / game_cfg["file"]
        with open(output, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {game_cfg['file']} - {game_data['name']} ({game_data['design']['style']})")

if __name__ == "__main__":
    print("🚀 重新生成所有攻略页面（独特设计）...")
    generate_all()
    print("✅ 完成")
