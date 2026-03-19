from pathlib import Path

# 剩余的占位页内容
remaining = {
    "guides/beapro_football/tactics-setup-guide.html": {
        "title": "战术设置指南",
        "game": "beapro_football",
        "content": """<h1>战术设置指南</h1>
        <p>战术设置是决定比赛胜负的关键。本文将详细解释各项战术参数的影响。</p>
        <h2>⚙️ 进攻风格</h2>
        <ul>
            <li><strong>控球</strong>：保持球权，适合技术型球队</li>
            <li><strong>直塞</strong>：快速通过中场，适合反击</li>
            <li><strong>边路</strong>：重点利用边路进攻</li>
            <li><strong>推进</strong>：平衡型，攻守兼备</li>
        </ul>
        <h2>🛡️ 防守风格</h2>
        <ul>
            <li><strong>高位防线</strong>：75-80，需要好后卫</li>
            <li><strong>中位防线</strong>：65-70，平衡选择</li>
            <li><strong>低位防线</strong>：55-60，防守反击</li>
        </ul>
        <h2>🎯 压迫强度</h2>
        <ul>
            <li><strong>高强度</strong>：65-70，需要体能好的球员</li>
            <li><strong>中等</strong>：50-60，常规选择</li>
            <li><strong>低强度</strong>：30-40，节省体力</li>
        </ul>
        <h2>📊 推荐设置（4-3-3 攻击阵型）</h2>
        <ul>
            <li>进攻风格：控球 + 边路</li>
            <li>防线位置：高防线（70-75）</li>
            <li>压迫强度：高强度（65-70）</li>
            <li>传球节奏：mixed（混合）</li>
        </ul>"""
    },
    "guides/kai_tian/cultivation-guide.html": {
        "title": "灵气修炼与渡劫",
        "game": "kai_tian",
        "content": """<h1>灵气修炼与渡劫系统</h1>
        <p>修炼体系是开天的核心。从筑基到飞升，每一步都需要精心规划。</p>
        <h2>🌟 修仙境界总览</h2>
        <ul>
            <li><strong>筑基</strong> → <strong>金丹</strong> → <strong>元婴</strong> → <strong>化神</strong> → <strong>渡劫</strong> → <strong>飞升</strong></li>
        </ul>
        <h2>⚡ 灵气获取途径</h2>
        <ol>
            <li><strong>打坐修炼</strong>：离线收益，每 10 分钟 100 灵气（VIP 加成）</li>
            <li><strong>副本「灵气窟」</strong>：每日 5 次，每次 500-2000 灵气</li>
            <li><strong>双修</strong>：与道侣双修，收益 +50%</li>
            <li><strong>宗门任务</strong>：每日 10 次，每个任务 200 灵气</li>
            <li><strong>活动「灵气爆发」</strong>：周末限时 3 小时，收益 x3</li>
        </ol>
        <h2>🔥 渡劫成功率提升</h2>
        <ul>
            <li><strong>护法道友</strong>：邀请 3 位道友护法，成功率 +30%</li>
            <li><strong>防御阵法</strong>：「九霄防御阵」减伤 40%</li>
            <li><strong>渡劫装备</strong>：「天劫抗性」套装 +20%</li>
            <li><strong>时辰选择</strong>：子时（23-1 点）渡劫，成功率最高</li>
        </ul>"""
    }
}

theme_map = {
    "beapro_football": {"primary": "#2ecc71", "bg": "#0d1b2a"},
    "kai_tian": {"primary": "#9b59b6", "bg": "#1a0a2e"}
}

for file_path, data in remaining.items():
    p = Path(file_path)
    if not p.exists():
        print(f"❌ 不存在: {file_path}")
        continue
    
    theme = theme_map[data["game"]]
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>:root{{--primary:{theme["primary"]};--bg:{theme["bg"]};--text:#fff}}body{{background:var(--bg");color:var(--text");padding:2rem;max-width:900px;margin:0 auto}}.back{{color:var(--primary");display:block;margin-bottom:2rem}}</style>
</head><body>
    <a href="/{data['game']}-guide.html" class="back">← 返回攻略中心</a>
    <div class="guide-content">
        {data["content"]}
        <p style="margin-top:2rem;color:#888;font-size:0.9rem;">最后更新：2026-03-18 | 作者：小肥喵</p>
    </div>
</body></html>'''
    p.write_text(html, encoding='utf-8')
    print(f"✅ 填充: {file_path}")

print("\n✨ 完成！")
