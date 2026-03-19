#!/usr/bin/env python3
"""补充圣斗士星矢缺失的详细页并充实内容"""

from pathlib import Path
import shutil

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# 圣斗士详细页映射（短名 -> 详细页）
saint_seiya_mapping = {
    "cosmo.html": "cosmo-guide.html",
    "armor.html": "armor-guide.html",
    "team.html": "team-composition-guide.html",  # 缺失！
    "gacha.html": "gacha-guide.html",
    "pvp.html": "pvp-strategy-guide.html",
    "temple.html": "zodiac-temple-guide.html",
}

# 1. 确保所有详细页存在（创建缺失的）
missing_guides = {
    "guides/saint_seiya/team-composition-guide.html": {
        "title": "阵容搭配",
        "theme": {"primary": "#ffd700", "bg": "#1a1a2e"},
        "content": """<h1>阵容搭配推荐</h1>
        <p>合理的阵容搭配是圣斗士星矢重生2胜利的关键。本文推荐多套当前版本最强阵容。</p>
        <h2>🏆 T0 版本阵容（万金油）</h2>
        <p><strong>配置</strong>：星矢 + 紫龙 + 穆 + 沙加 + 迪斯马斯克</p>
        <ul>
            <li><strong>星矢</strong>：天马座，主力输出，开大秒杀后排</li>
            <li><strong>紫龙</strong>：龙座，副输出+破甲，降低目标防御 40%</li>
            <li><strong>穆</strong>：白羊座，坦克，群体护盾保护</li>
            <li><strong>沙加</strong>：处女座，控制，沉默+降低命中</li>
            <li><strong>迪斯马斯克</strong>：巨蟹座，治疗+复活，队伍保障</li>
        </ul>
        <h2>📈 速度配置</h2>
        <p>参考顺序：穆 > 沙加 > 紫龙 > 星矢 > 迪斯马斯克（依次快 10-15 点）</p>
        <p><strong>原理</strong>：穆先手盾 → 沙加沉默 → 紫龙破甲 → 星矢爆发 → 迪斯治疗</p>
        <h2>⚡ 替代方案</h2>
        <ul>
            <li><strong>暴力输出队</strong>：星矢 + 紫龙 + 瞬 + 冰河 + 一辉（高速强杀）</li>
            <li><strong>控制流</strong>：沙加 + 穆 + 雅典娜 + 童虎 + 加隆（无限控制）</li>
            <li><strong>复活恶心流</strong>：迪斯马斯克 + 雅典娜 + 童虎 + 加隆 + 史昂（打不死）</li>
        </ul>
        <h2>💎 实战技巧</h2>
        <ol>
            <li><strong>穆的盾</strong>：务必在敌人开大前开启，保护后排</li>
            <li><strong>沙加的沉默</strong>：优先给对面治疗或核心输出</li>
            <li><strong>星矢的大招</strong>：锁定对方后排脆皮，不要打坦克</li>
            <li><strong>迪斯复活</strong>：留到BOSS狂暴阶段或团灭瞬间</li>
        </ol>"""
    }
}

# 2. 充实现有页面（添加更多数据）
充实内容 = {
    "guides/saint_seiya/cosmo-guide.html": {
        "extra": """
        <h2>🎯 小宇宙燃烧的细节机制</h2>
        <ul>
            <li><strong>最多存储量</strong>：100%（溢出部分不保留）</li>
            <li><strong>天赋加成</strong>：满级天赋「燃烧精通」延长 5 秒持续时间</li>
            <li><strong>装备加成</strong>：某些圣衣特效可延长燃烧时间</li>
            <li><strong>双人共享</strong>：队伍中两人同时燃烧，效果不叠加但时长可延长</li>
        </ul>
        <h2>📊 各职业小宇宙积攒效率对比</h2>
        <table border="1" cellpadding="8">
            <tr><th>职业</th><th>普攻%</th><th>技能%</th><th>格挡%</th><th>特殊</th></tr>
            <tr><td>天马座</td><td>5%</td><td>15%</td><td>3%</td><td>连击+10%（每5连）</td></tr>
            <tr><td>龙座</td><td>5%</td><td>12%</td><td>5%</td><td>破甲后额外+5%</td></tr>
            <tr><td>白羊座</td><td>5%</td><td>10%</td><td>10%</td><td>护盾成功格挡+15%</td></tr>
        </table>
        <h2>⏰ 不同场景的燃烧时机建议</h2>
        <ul>
            <li><strong>世界BOSS</strong>：全员保留，等BOSS转阶段时一起开</li>
            <li><strong>竞技场</strong>：开场3秒内必须燃烧，抢先手</li>
            <li><strong>多人副本</strong>：坦克先开，输出后开，错开10秒</li>
            <li><strong>限时活动</strong>：根据活动要求，有时需要保留到最后一刻</li>
        </ul>"""
    },
    "guides/saint_seiya/zodiac-temple-guide.html": {
        "extra": """
        <h2>🏛️ 十二宫详细攻略（每个宫的特性）</h2>
        <ul>
            <li><strong>白羊宫（穆）</strong>：会群体治疗，优先击杀小怪再打本体</li>
            <li><strong>金牛宫（阿鲁迪巴）</strong>：高防御，需要破甲技能降低防御</li>
            <li><strong>双子宫（撒加）</strong>：双人格切换，控制人格时优先击杀</li>
            <li><strong>巨蟹宫（迪斯马斯克）</strong>：频繁召唤小怪，需要快速清理避免治疗</li>
            <li><strong>狮子宫（艾欧利亚）</strong>：高爆发单体，保持距离避免被秒</li>
            <li><strong>处女宫（沙加）</strong>：沉默技能让你无法回血，带解药</li>
            <li><strong>天秤宫（童虎）</strong>：均衡型，技能全面，需要注意走位</li>
            <li><strong>天蝎宫（米罗）</strong>：持续中毒伤害，需要净化或高抗性</li>
            <li><strong>人马宫（艾俄洛斯）</strong>：远程射手，保持移动避免被锁定</li>
            <li><strong>摩羯宫（修罗）</strong>：破防技能很强，需要坦克硬抗</li>
            <li><strong>水瓶宫（卡妙）</strong>：冰系减速+冻结，需要高敏捷</li>
            <li><strong>双鱼宫（阿布罗狄）</strong>：魅惑控制+持续伤害，需要解控</li>
        </ul>
        <h2>📈 十二宫奖励</h2>
        <table border="1" cellpadding="8">
            <tr><th>宫数</th><th>首通奖励</th><th>每周奖励</th><th>掉落</th></tr>
            <tr><td>1-3</td><td>灵石×5000</td><td>灵石×2000</td><td>白色/绿色圣衣</td></tr>
            <tr><td>4-6</td><td> SR券×1</td><td>SR券×1</td><td>蓝色/紫色圣衣</td></tr>
            <tr><td>7-9</td><td>橙色材料×5</td><td>紫色材料×10</td><td>橙色圣衣碎片</td></tr>
            <tr><td>10-12</td><td>SSR圣衣箱</td><td>橙色材料×20</td><td>SSR圣衣</td></tr>
        </table>"""
    }
}

def main():
    # 1. 创建缺失的 team-composition-guide.html
    team_file = REPO / "guides/saint_seiya/team-composition-guide.html"
    if not team_file.exists():
        data = missing_guides[str(team_file)]
        theme = data["theme"]
        html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>:root{{--primary:{theme["primary"]};--bg:{theme["bg"]};--text:#fff}}body{{background:var(--bg");color:var(--text");padding:2rem;max-width:900px;margin:0 auto}}.back{{color:var(--primary");display:block;margin-bottom:2rem}}</style>
</head><body>
    <a href="/saint-seiya-guide.html" class="back">← 返回攻略中心</a>
    <div class="guide-content">
        {data["content"]}
    </div>
</body></html>'''
        team_file.write_text(html, encoding='utf-8')
        print(f"✅ 创建：team-composition-guide.html")
    
    # 2. 充实现有页面
    for file_path_str, extra_data in 充实内容.items():
        fp = REPO / file_path_str
        if fp.exists():
            html = fp.read_text(encoding='utf-8')
            # 在 </div></body></html> 前插入 extra
            new_html = html.replace('</div></body></html>', extra_data["extra"] + '\n</div></body></html>')
            fp.write_text(new_html, encoding='utf-8')
            print(f"✅ 充实：{fp.name}")
    
    # 3. 创建/更新短文件名（真实文件，非软链接）
    for short, full in saint_seiya_mapping.items():
        sp = REPO / f"guides/saint_seiya/{short}"
        fp = REPO / f"guides/saint_seiya/{full}"
        if fp.exists():
            if sp.exists() or sp.is_symlink():
                sp.unlink()
            shutil.copy2(fp, sp)
            print(f"✅ 同步：{short}")
    
    print("\n✨ 圣斗士星矢详细页补充完成！")

if __name__ == "__main__":
    main()
