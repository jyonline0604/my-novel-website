#!/usr/bin/env python3
"""
自动修复缺失的攻略页链接
 - 根据主页中引用的链接，自动创建占位攻略页
 - 使用模板填充基本内容
"""

import re
from pathlib import Path

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
GUIDE_PAGES = ["game-guide.html", "saint-seiya-guide.html", "beapro-football-guide.html", "kai-tian-guide.html"]

# 链接到游戏类型的映射
GAME_DIR_MAP = {
    "game_guide": "game_guide",
    "saint_seiya": "saint_seiya",
    "beapro_football": "beapro_football",
    "kai_tian": "kai_tian"
}

# 游戏主题色
THEME_MAP = {
    "game_guide": {"primary": "#d4a017", "bg": "#0a0a0a", "name": "問劍長生"},
    "saint_seiya": {"primary": "#ffd700", "bg": "#1a1a2e", "name": "聖鬥士星矢重生2"},
    "beapro_football": {"primary": "#2ecc71", "bg": "#0d1b2a", "name": "Be A Pro Football"},
    "kai_tian": {"primary": "#9b59b6", "bg": "#1a0a2e", "name": "開天"}
}

# 通用攻略模板
def generate_guide_html(game_type, guide_id, guide_title):
    """生成简单但完整的攻略页"""
    theme = THEME_MAP[game_type]
    game_dir = GAME_DIR_MAP[game_type]
    
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{guide_title} - {theme["name"]} | 科技修真傳</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        :root {{ --primary: {theme["primary"]}; --bg: {theme["bg"]}; --text: #fff; --card-bg: rgba(255,255,255,0.05); }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 80px 2rem 2rem; max-width: 900px; margin: 0 auto; line-height: 1.8; }}
        .back-link {{ color: var(--primary); margin-bottom: 2rem; display: block; text-decoration: none; }}
        .guide-content {{ background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--primary); }}
        h1 {{ color: var(--primary); font-size: 2rem; margin-bottom: 1rem; }}
        p {{ margin-bottom: 1rem; color: #bbb; }}
        .tag {{ display: inline-block; background: var(--primary); color: #000; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.85rem; margin-right: 0.5rem; }}
        .placeholder-note {{ background: rgba(255,193,7,0.1); border-left: 4px solid #ffc107; padding: 1rem; margin: 2rem 0; }}
    </style>
</head>
<body>
    <a href="/{game_dir}-guide.html" class="back-link"><i class="fas fa-arrow-left"></i> 返回攻略中心</a>
    
    <div class="guide-content">
        <span class="tag">占位符</span>
        <h1>{guide_title}</h1>
        <p>本篇攻略正在编写中，敬请期待完整内容。</p>
        
        <div class="placeholder-note">
            <strong>🔧 自动生成占位页</strong><br>
            检测到此攻略链接存在，但缺少实际内容。作者正在撰写中，稍后会更新为详细攻略。
        </div>
        
        <h2>📋 计划包含内容</h2>
        <ul>
            <li>核心机制详解</li>
            <li>实用技巧与策略</li>
            <li>常见问题解答</li>
            <li>数据表格与计算</li>
        </ul>
        
        <p style="margin-top:2rem; color:#888; font-size:0.9rem;">最后更新：2026-03-18 | 作者：小肥喵</p>
    </div>
</body>
</html>'''

def extract_links_from_page(page_file):
    """从页面提取所有内部link，返回(游戏类型, 完整链接, 标题)列表"""
    html = (REPO_DIR / page_file).read_text(encoding='utf-8')
    # 匹配攻略卡片链接: href="/guides/game_guide/sword.html"
    pattern = r'href="(/guides/([^/]+)/([^"]+))\.html"[^>]*>.*?<strong>([^<]+)</strong>'
    matches = re.findall(pattern, html, re.DOTALL)
    
    results = []
    for full_link, game_type, guide_id, title in matches:
        results.append((game_type, f"/guides/{game_type}/{guide_id}.html", title.strip()))
    
    return results

def main():
    print("🔧 开始修复缺失的攻略页...")
    created_count = 0
    
    for page in GUIDE_PAGES:
        if not (REPO_DIR / page).exists():
            print(f"❌ 跳过: {page} 不存在")
            continue
            
        print(f"\n📄 处理 {page}...")
        links = extract_links_from_page(page)
        
        for game_type, link, title in links:
            full_path = REPO_DIR / Path(link.lstrip('/'))
            if not full_path.exists():
                # 创建目录
                full_path.parent.mkdir(parents=True, exist_ok=True)
                # 生成内容
                html = generate_guide_html(game_type, Path(link).stem, title)
                full_path.write_text(html, encoding='utf-8')
                print(f"  ✅ 创建: {link} - {title}")
                created_count += 1
    
    print(f"\n✅ 完成！共创建 {created_count} 个占位攻略页")
    return 0

if __name__ == "__main__":
    main()
