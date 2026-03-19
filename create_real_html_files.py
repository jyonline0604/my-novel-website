import shutil
from pathlib import Path

REPO = Path(".")

# 需要创建的短文件名映射（从实际存在的 -guide.html 复制）
mapping = {
    "guides/game_guide/sword.html": "guides/game_guide/sword-guide.html",
    "guides/game_guide/pet.html": "guides/game_guide/pet-guide.html",
    "guides/game_guide/craft.html": "guides/game_guide/craft-guide.html",
    "guides/game_guide/ascend.html": "guides/game_guide/ascension-guide.html",
    "guides/game_guide/resource.html": "guides/game_guide/resource-guide.html",
    "guides/game_guide/boss.html": "guides/game_guide/boss-guide.html",
    "guides/saint_seiya/cosmo.html": "guides/saint_seiya/cosmo-guide.html",
    "guides/saint_seiya/armor.html": "guides/saint_seiya/armor-guide.html",
    "guides/saint_seiya/team.html": "guides/saint_seiya/team-composition-guide.html",
    "guides/saint_seiya/gacha.html": "guides/saint_seiya/gacha-guide.html",
    "guides/saint_seiya/pvp.html": "guides/saint_seiya/pvp-strategy-guide.html",
    "guides/saint_seiya/temple.html": "guides/saint_seiya/zodiac-temple-guide.html",
    "guides/beapro_football/formation.html": "guides/beapro_football/formation-433-guide.html",
    "guides/beapro_football/training.html": "guides/beapro_football/player-training-guide.html",
    "guides/beapro_football/transfer.html": "guides/beapro_football/transfer-market-guide.html",
    "guides/beapro_football/analytics.html": "guides/beapro_football/data-analytics-guide.html",
    "guides/beapro_football/cup.html": "guides/beapro_football/champions-cup-guide.html",
    "guides/beapro_football/skills.html": "guides/beapro_football/skills-training-guide.html",
    "guides/kai_tian/cultivation.html": "guides/kai_tian/cultivation-guide.html",
    "guides/kai_tian/spirit.html": "guides/kai_tian/spirit-beast-guide.html",
    "guides/kai_tian/artifact.html": "guides/kai_tian/artifact-forging-guide.html",
    "guides/kai_tian/sect.html": "guides/kai_tian/sect-mission-guide.html",
    "guides/kai_tian/alchemy.html": "guides/kai_tian/alchemy-guide.html",
    "guides/kai_tian/realm.html": "guides/kai_tian/realm-progression-guide.html",
    "guides/kai_tian/sword.html": "guides/kai_tian/sword-cultivation-guide.html",
    "guides/kai_tian/pet.html": "guides/kai_tian/pet-nurturing-guide.html",
    "guides/kai_tian/resource.html": "guides/kai_tian/resource-management-guide.html",
    "guides/kai_tian/craft.html": "guides/kai_tian/crafting-system-guide.html",
    "guides/kai_tian/boss.html": "guides/kai_tian/boss-battle-guide.html",
    "guides/kai_tian/ascend.html": "guides/kai_tian/ascension-guide.html",
}

created = 0
for short, full in mapping.items():
    sp = Path(short)
    fp = Path(full)
    
    if not fp.exists():
        print(f"❌ 源文件缺失: {full}")
        continue
    
    # 删除已存在的（软链接或旧文件）
    if sp.exists() or sp.is_symlink():
        sp.unlink()
    
    # 复制真实文件
    shutil.copy2(fp, sp)
    print(f"✅ {short} 已创建（真实文件）")
    created += 1

print(f"\n✨ 共创建 {created} 个真实 HTML 文件（无软链接）")
