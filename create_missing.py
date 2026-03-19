from pathlib import Path

# 需要创建的缺失文件映射（使用简单占位内容）
missing = [
    ("guides/game_guide/boss.html", "BOSS攻略", "game_guide"),
    ("guides/beapro_football/formation.html", "战术阵型大全", "beapro_football"),
    ("guides/beapro_football/training.html", "球员培养指南", "beapro_football"),
    ("guides/kai_tian/realm.html", "境界提升路线", "kai_tian"),
]

theme_map = {
    "game_guide": {"primary": "#d4a017", "bg": "#0a0a0a", "name": "問劍長生"},
    "beapro_football": {"primary": "#2ecc71", "bg": "#0d1b2a", "name": "Be A Pro Football"},
    "kai_tian": {"primary": "#9b59b6", "bg": "#1a0a2e", "name": "開天"}
}

for path_str, title, game_type in missing:
    path = Path(path_str)
    if path.exists():
        print(f"⚠️ {path} 已存在，跳过")
        continue
    
    theme = theme_map[game_type]
    # 创建占位页
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>:root{{--primary:{theme["primary"]};--bg:{theme["bg"]};--text:#fff}}body{{background:var(--bg);color:var(--text");padding:2rem;max-width:900px;margin:0 auto}}.back{{color:var(--primary");display:block;margin-bottom:2rem}}</style>
</head><body>
    <a href="/{game_type}-guide.html" class="back">← 返回攻略中心</a>
    <h1>{title}</h1>
    <p>此攻略正在撰写中，敬请期待完整内容。</p>
</body></html>'''
    path.write_text(html, encoding='utf-8')
    print(f"✅ 创建占位页: {path}")
    
    # 创建软链接
    if path.name.endswith('-guide.html'):
        link = path.parent / (path.stem + '.html')
        if link.exists():
            link.unlink()
        link.symlink_to(path.name)
        print(f"  🔗 软链接: {link.name}")

print("\n✨ 所有缺失占位页已创建")
