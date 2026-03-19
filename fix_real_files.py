from pathlib import Path
import shutil

# 需要确保存在的短文件名（.html）列表
short_names = [
    "guides/game_guide/ascend.html",
    "guides/game_guide/boss.html",
    "guides/game_guide/resource.html",
    "guides/game_guide/sword.html",
    "guides/game_guide/pet.html",
    "guides/game_guide/craft.html",
    "guides/saint_seiya/cosmo.html",
    "guides/saint_seiya/armor.html",
    "guides/saint_seiya/team.html",
    "guides/saint_seiya/gacha.html",
    "guides/saint_seiya/pvp.html",
    "guides/saint_seiya/temple.html",
    "guides/beapro_football/formation.html",
    "guides/beapro_football/training.html",
    "guides/beapro_football/transfer.html",
    "guides/beapro_football/analytics.html",
    "guides/beapro_football/cup.html",
    "guides/beapro_football/tactics.html",
    "guides/beapro_football/skills.html",
    "guides/kai_tian/cultivation.html",
    "guides/kai_tian/spirit.html",
    "guides/kai_tian/artifact.html",
    "guides/kai_tian/sect.html",
    "guides/kai_tian/alchemy.html",
    "guides/kai_tian/realm.html",
    "guides/kai_tian/sword.html",
    "guides/kai_tian/pet.html",
    "guides/kai_tian/resource.html",
    "guides/kai_tian/craft.html",
    "guides/kai_tian/boss.html",
    "guides/kai_tian/ascend.html",
]

# 删除所有错误的 .html.html 文件
count = 0
for f in Path(".").rglob("*.html.html"):
    f.unlink()
    count += 1
print(f"🗑️ 已删除 {count} 个 .html.html 错误文件")

# 为每个短文件名创建真实文件（复制对应的 -guide.html 内容）
created = 0
for short in short_names:
    sp = Path(short)
    guide_file = sp.parent / f"{sp.stem}-guide.html"
    
    if guide_file.exists():
        # 删除已存在的软链接或文件
        if sp.exists() or sp.is_symlink():
            sp.unlink()
        # 复制内容
        shutil.copy2(guide_file, sp)
        print(f"✅ {short} -> {guide_file.name}")
        created += 1
    else:
        print(f"❌ 源文件不存在: {guide_file}")

print(f"\n✨ 共创建 {created} 个真实文件")
