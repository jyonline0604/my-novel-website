#!/usr/bin/env python3
import json
from pathlib import Path

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
CONFIG_FILE = REPO_DIR / "auto-update-scripts" / "update_config.json"

def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_game_data(game_key):
    games = {
        "game_guide": {"name": "問劍長生", "primary": "#d4a017", "bg": "#0a0a0a", "style": "cyberpunk"},
        "saint_seiya": {"name": "聖鬥士星矢重生2", "primary": "#ffd700", "bg": "#1a1a2e", "style": "cosmic"},
        "beapro_football": {"name": "Be A Pro Football", "primary": "#2ecc71", "bg": "#0d1b2a", "style": "stadium"},
        "kai_tian": {"name": "開天", "primary": "#9b59b6", "bg": "#1a0a2e", "style": "ethereal"}
    }
    return games.get(game_key, games["game_guide"])

def generate_hero(game):
    if game["style"] == "stadium":
        return f'''<section style="background: linear-gradient(180deg, #2d5a27, #1a3518); color: white; padding: 4rem 2rem; text-align: center;">
            <h1 style="font-size: 3.5rem; margin-bottom: 0.5rem; color: {game["primary"]};">{game["name"]}</h1>
            <p>打造冠军阵容 | 战术大师指南</p>
            <a href="#guides" style="background: {game["primary"]}; color: #000; padding: 1rem 2rem; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 1rem;">开始攻略</a>
        </section>'''
    elif game["style"] == "cosmic":
        return f'''<section style="background: radial-gradient(circle at 50%, #2d1b69, #000); color: white; padding: 4rem 2rem; text-align: center;">
            <h1 style="font-size: 4rem; background: linear-gradient(to right, {game["primary"]}, #9b4ee6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{game["name"]}</h1>
            <p>燃烧小宇宙 · 黄金圣斗士之路</p>
            <a href="#guides" style="border: 2px solid {game["primary"]}; color: {game["primary"]}; padding: 1rem 2rem; border-radius: 50px; text-decoration: none; display: inline-block; margin-top: 1rem;">展开圣域</a>
        </section>'''
    elif game["style"] == "ethereal":
        return f'''<section style="background: linear-gradient(45deg, #2c003e, #512b58); color: white; padding: 4rem 2rem; text-align: center;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">☯</div>
            <h1 style="font-size: 3.5rem; color: {game["primary"]};">{game["name"]}</h1>
            <p>修真飞升 · 渡劫成仙</p>
            <a href="#guides" style="background: {game["primary"]}; padding: 1rem 2rem; border-radius: 50px; text-decoration: none; display: inline-block; margin-top: 1rem;">开始修炼</a>
        </section>'''
    else:
        return f'''<section style="background: {game["bg"]}; color: white; padding: 4rem 2rem; text-align: center;">
            <h1 style="font-size: 3rem; color: {game["primary"]};">{game["name"]}</h1>
            <p>最完整的攻略平台</p>
        </section>'''

def generate_guides_grid(game):
    game_key_map = {"問劍長生": "game_guide", "聖鬥士星矢重生2": "saint_seiya", "Be A Pro Football": "beapro_football", "開天": "kai_tian"}
    game_dir = game_key_map.get(game["name"], "game_guide")
    
    if game["style"] == "stadium":
        guides = [
            {"icon": "fa-users", "title": "战术阵型大全", "id": "formation"},
            {"icon": "fa-user-plus", "title": "球员培养指南", "id": "training"},
            {"icon": "fa-exchange-alt", "title": "转会市场攻略", "id": "transfer"},
            {"icon": "fa-chart-line", "title": "数据分析入门", "id": "analytics"},
            {"icon": "fa-trophy", "title": "冠军杯通关", "id": "cup"},
            {"icon": "fa-futbol", "title": "技巧训练场", "id": "skills"}
        ]
    elif game["style"] == "cosmic":
        guides = [
            {"icon": "fa-star", "title": "小宇宙燃烧", "id": "cosmo"},
            {"icon": "fa-shield-alt", "title": "圣衣装备", "id": "armor"},
            {"icon": "fa-users-cog", "title": "阵容搭配", "id": "team"},
            {"icon": "fa-crown", "title": "黄金抽卡", "id": "gacha"},
            {"icon": "fa-fist-raised", "title": "竞技场攻略", "id": "pvp"},
            {"icon": "fa-dungeon", "title": "十二宫副本", "id": "temple"}
        ]
    elif game["style"] == "ethereal":
        guides = [
            {"icon": "fa-cloud", "title": "灵气修炼与渡劫", "id": "cultivation"},
            {"icon": "fa-dragon", "title": "灵兽捕捉与培养", "id": "spirit"},
            {"icon": "fa-gem", "title": "法宝炼器系统", "id": "artifact"},
            {"icon": "fa-landmark", "title": "宗门任务攻略", "id": "sect"},
            {"icon": "fa-flask", "title": "炼丹系统详解", "id": "alchemy"},
            {"icon": "fa-chart-line", "title": "境界提升路线", "id": "realm"}
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
    
    html = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">'
    for g in guides:
        html += f'''
        <a href="/guides/{game_dir}/{g['id']}.html" style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 10px; display: flex; align-items: center; gap: 1rem; border: 1px solid {game["primary"]}33; text-decoration: none; color: white;">
            <i class="fas {g['icon']}" style="color: {game["primary"]}; font-size: 1.5rem;"></i>
            <div>
                <strong>{g['title']}</strong><br>
                <small style="color: {game['primary']};">查看详情 →</small>
            </div>
        </a>'''
    html += '</div>'
    return html

def generate_page(game_key, file):
    game = get_game_data(game_key)
    guides = get_game_data(game_key)
    game_dir = get_game_guide_dir(game_key)
    
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game["name"]}攻略中心</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        body {{ margin: 0; font-family: system-ui, -apple-system, sans-serif; background: {game["bg"]}; color: white; padding: 100px 2rem 2rem; max-width: 1200px; margin: 0 auto; }}
        a {{ color: {game["primary"]} !important; }}
        .news-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }}
        .news-card {{ background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid {game["primary"]}22; }}
        .news-card h3 {{ margin: 0 0 0.5rem 0; }}
        .news-card p {{ color: #aaa; margin: 0 0 1rem 0; }}
        .section {{ margin: 3rem 0; }}
        .section h2 {{ font-size: 2rem; color: {game["primary"]}; border-bottom: 2px solid {game["primary"]}; padding-bottom: 0.5rem; }}
    </style>
</head>
<body>
    {generate_hero(game)}
    
    <section class="section" id="news">
        <h2>📰 最新资讯</h2>
        <div class="news-grid">
            <div class="news-card"><h3>最新版本更新</h3><p>新增内容与平衡调整</p></div>
            <div class="news-card"><h3>活动攻略</h3><p>限时活动最佳完成路线</p></div>
            <div class="news-card"><h3>社区热点</h3><p>玩家讨论最多的话题</p></div>
        </div>
    </section>
    
    <section class="section" id="guides">
        <h2>📚 精选攻略</h2>
        {generate_guides_grid(game)}
    </section>
    
    <footer style="text-align: center; padding: 2rem; color: #666; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.1);">
        返回 <a href="index.html">首页</a>
    </footer>
</body>
</html>'''

def get_game_guide_dir(game_key):
    mapping = {"game_guide": "game_guide", "saint_seiya": "saint_seiya", "beapro_football": "beapro_football", "kai_tian": "kai_tian"}
    return mapping.get(game_key, game_key)

if __name__ == "__main__":
    config = load_config()
    for game_key, game_cfg in config["update_schedule"].items():
        if not game_cfg.get("enabled"): continue
        html = generate_page(game_key, game_cfg["file"])
        output = REPO_DIR / game_cfg["file"]
        with open(output, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {game_cfg['file']}")
    print("✅ 完成")
