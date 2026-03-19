#!/usr/bin/env python3
"""统一圣斗士所有详细页的样式，修复返回按钮"""

from pathlib import Path
import re

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
theme = {"primary": "#ffd700", "bg": "#1a1a2e"}

# 完整样式模板
STYLE_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 聖鬥士星矢重生2 | 科技修真傳</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        :root {{ --primary: {primary}; --bg: {bg}; --text: #fff; --card-bg: rgba(255,255,255,0.05); }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 80px 2rem 2rem; max-width: 900px; margin: 0 auto; line-height: 1.8; }}
        .back-link {{ color: var(--primary); margin-bottom: 2rem; display: block; text-decoration: none; font-size: 1.1rem; }}
        .back-link:hover {{ opacity: 0.8; text-decoration: underline; }}
        .guide-content {{ background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--primary); }}
        h1 {{ color: var(--primary); font-size: 2rem; margin-bottom: 1rem; }}
        h2 {{ color: var(--primary); font-size: 1.5rem; margin: 2rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 1rem; }}
        p, li, td, th {{ color: #ccc; }}
        ul, ol {{ margin-left: 2rem; margin-bottom: 1rem; }}
        li {{ margin-bottom: 0.5rem; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
        th, td {{ border: 1px solid var(--primary); padding: 0.8rem; text-align: left; }}
        th {{ background: rgba(255,215,0,0.1); color: var(--primary); }}
        code {{ background: rgba(255,255,255,0.1); padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; }}
        strong {{ color: #fff; }}
    </style>
</head>
<body>
    <a href="/saint-seiya-guide.html" class="back-link"><i class="fas fa-arrow-left"></i> 返回攻略中心</a>
    <div class="guide-content">
        {content}
        <p style="margin-top:2rem; color:#888; font-size:0.9rem;">最后更新：2026-03-18 | 作者：小肥喵</p>
    </div>
</body></html>'''

# 需要更新的详细页（列表）
detailed_pages = [
    "guides/saint_seiya/cosmo-guide.html",
    "guides/saint_seiya/armor-guide.html",
    "guides/saint_seiya/team-composition-guide.html",
    "guides/saint_seiya/gacha-guide.html",
    "guides/saint_seiya/pvp-strategy-guide.html",
    "guides/saint_seiya/zodiac-temple-guide.html",
    "guides/saint_seiya/news-updates-guide.html",
    "guides/saint_seiya/events-guide.html",
    "guides/saint_seiya/community-guide.html",
]

for page_path in detailed_pages:
    p = REPO / page_path
    if not p.exists():
        print(f"❌ 跳过：{page_path} 不存在")
        continue
    
    html = p.read_text(encoding='utf-8')
    
    # 提取当前标题
    title_match = re.search(r'<h1>([^<]+)</h1>', html)
    title = title_match.group(1) if title_match else "攻略"
    
    # 提取内容（去掉 head 和 body 标签）
    content_match = re.search(r'<div class="guide-content">(.+?)</div>\s*</body>', html, re.DOTALL)
    if content_match:
        content = content_match.group(1).strip()
    else:
        # 简单提取 body 内容
        body_match = re.search(r'<div class="guide-content">(.+?)</div>', html, re.DOTALL)
        content = body_match.group(1).strip() if body_match else ""
    
    # 生成新的完整 HTML
    new_html = STYLE_TEMPLATE.format(
        title=title,
        primary=theme["primary"],
        bg=theme["bg"],
        content=content
    )
    
    p.write_text(new_html, encoding='utf-8')
    print(f"✅ 已修复样式：{page_path}")

print("\n✨ 所有圣斗士详细页样式已统一！")
