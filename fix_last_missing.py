from pathlib import Path

# 最后3个缺失文件（占位符）
missing = [
    ("guides/game_guide/boss.html", "BOSS攻略", "game_guide"),
    ("guides/beapro_football/formation.html", "战术阵型大全", "beapro_football"),
    ("guides/beapro_football/training.html", "球员培养指南", "beapro_football"),
]

theme_map = {
    "game_guide": {"primary": "#d4a017", "bg": "#0a0a0a"},
    "beapro_football": {"primary": "#2ecc71", "bg": "#0d1b2a"}
}

for path_str, title, game_type in missing:
    path = Path(path_str)
    if path.exists():
        print(f"⚠️ {path} 已存在")
        continue
    
    theme = theme_map[game_type]
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head><meta charset="UTF-8"><style>:root{{--primary:{theme["primary"]};--bg:{theme["bg"]};--text:#fff}}body{{background:var(--bg");color:var(--text");padding:2rem;max-width:900px;margin:0 auto}}.back{{color:var(--primary");display:block;margin-bottom:2rem}}</style></head>
<body><a href="/{game_type}-guide.html" class="back">← 返回攻略中心</a><h1>{title}</h1><p>此攻略正在撰写中。</p></body></html>'''
    path.write_text(html, encoding='utf-8')
    print(f"✅ 创建: {title}")
    
    # 创建软链接（如有需要）
    if path.name.endswith('-guide.html'):
        link = path.parent / (path.stem + '.html')
        if link.exists():
            link.unlink()
        link.symlink_to(path.name)

print("\n✨ 完成！")
