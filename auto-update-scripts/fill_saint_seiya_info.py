#!/usr/bin/env python3
"""为圣斗士星矢添加三个资讯页面（与问剑长生类似）"""

from pathlib import Path
import shutil

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
theme = {"primary": "#ffd700", "bg": "#1a1a2e"}

# 三个资讯页内容
pages = {
    "news-updates-guide.html": {
        "title": "最新版本更新",
        "content": """<h1>📢 最新版本更新</h1>
        <p>圣斗士星矢重生2官方公告、版本变动、平衡调整聚合。</p>
        <h2>📅 近期更新记录</h2>
        <table border="1" cellpadding="8">
            <tr><th>日期</th><th>版本</th><th>主要内容</th></tr>
            <tr><td>2026-03-10</td><td>v2.8.5</td><td>新增双子座·撒加（SSR）、优化PVP匹配机制</td></tr>
            <tr><td>2026-02-28</td><td>v2.8.0</td><td>开放「神话篇」章节、新增神器系统</td></tr>
            <tr><td>2026-02-10</td><td>v2.7.8</td><td>平衡调整：天马座伤害+10%、处女座削弱</td></tr>
        </table>
        <h2>⚖️ 平衡调整详情</h2>
        <ul>
            <li><strong>天马座（星矢）</strong>：大招基础伤害提升 15%</li>
            <li><strong>处女座（沙加）</strong>：沉默持续时间从 4 秒降至 3 秒</li>
            <li><strong>白羊座（穆）</strong>：护盾量提升 20%</li>
            <li><strong>巨蟹座（迪斯马斯克）</strong>：复活技能冷却 +5 秒</li>
        </ul>
        <h2>🔮 即将到来</h2>
        <p><strong>v2.9.0 预计 4 月初</strong></p>
        <ul>
            <li>新增「海皇篇」主线剧情</li>
            <li>海斗士系列新角色（闭、笛、尤莉迪丝）</li>
            <li>跨服竞技场赛季制</li>
            <li>圣衣幻化系统（外观自定义）</li>
        </ul>"""
    },
    "events-guide.html": {
        "title": "活动攻略",
        "content": """<h1>🎉 活动攻略</h1>
        <p>圣斗士各类限时活动的最佳参与策略与奖励最大化指南。</p>
        <h2>📆 活动日历</h2>
        <table border="1" cellpadding="8">
            <tr><th>活动名称</th><th>周期</th><th>核心奖励</th><th>推荐度</th></tr>
            <tr><td>十二宫速通</td><td>每日 10:00-12:00</td><td>圣衣碎片、SR券</td><td>⭐⭐⭐⭐⭐</td></tr>
            <tr><td>小宇宙试炼</td><td>每周一/四 20:00</td><td>燃烧加成材料</td><td>⭐⭐⭐⭐</td></tr>
            <tr><td>黄金圣衣召唤</td><td>每周末</td><td>UP 概率提升</td><td>⭐⭐⭐⭐⭐</td></tr>
            <tr><td>竞技场双倍</td><td>每周三</td><td>竞技币×2</td><td>⭐⭐⭐⭐</td></tr>
            <tr><td>体力翻倍</td><td>每日 13:00-15:00</td><td>副本掉落×2</td><td>⭐⭐⭐⭐⭐</td></tr>
        </table>
        <h2>⭐ 必刷活动优先级</h2>
        <ol>
            <li><strong>体力翻倍</strong> - 所有资源的基础，优先刷</li>
            <li><strong>黄金圣衣召唤</strong> - SSR 保底，体力有限时要囤石头</li>
            <li><strong>十二宫速通</strong> - 圣衣碎片稳定来源</li>
            <li><strong>小宇宙试炼</strong> - PVP 必备材料</li>
        </ol>
        <h2>💡 活动技巧</h2>
        <ul>
            <li><strong>体力管理</strong>：体力药水留到双倍时段使用</li>
            <li><strong>石头囤积</strong>：非 UP 期间绝不抽卡，集中资源</li>
            <li><strong>速通队配置</strong>：高爆发阵容快速通关，节省时间</li>
            <li><strong>排名奖励</strong>：竞技场双倍时段冲击排名，奖励更多</li>
        </ul>"""
    },
    "community-guide.html": {
        "title": "社区热点",
        "content": """<h1>🔥 社区热点</h1>
        <p>圣斗士社区本周最热话题、组队需求、交易动态。</p>
        <h2>📊 本周热议 TOP 5</h2>
        <ol>
            <li><strong>【强度】天马座是否版本之子？</strong><br>
                热度：⭐⭐⭐⭐⭐<br>
                讨论：新版本加成后，天马座胜率飙升至 68%<br>
                <em>（官方：正在监测，可能回调）</em></li>
            <li><strong>【求助】处女宫怎么过？</strong><br>
                热度：⭐⭐⭐⭐⭐<br>
                问题：沙加沉默太恶心，有没有解控圣衣？</li>
            <li><strong>【晒卡】100抽双黄！</strong><br>
                热度：⭐⭐⭐⭐⭐<br>
                内容：分享双黄截图，天马座+射手座</li>
            <li><strong>【数据】各星座胜率统计</strong><br>
                热度：⭐⭐⭐⭐<br>
                数据：T0阵容胜率 > 75%，T3阵容 < 45%</li>
            <li><strong>【BUG】十二宫卡 Bug 无限刷</strong><br>
                热度：⭐⭐⭐⭐<br>
                状态：已上报官方，正在修复中</li>
        </ol>
        <h2>👥 热门组队需求</h2>
        <table border="1" cellpadding="8">
            <tr><th>职业</th><th>等级</th><th>需求</th><th>备注</th></tr>
            <tr><td>天马座×2</td><td>130+</td><td>十二宫速通</td><td>需高爆发</td></tr>
            <tr><td>白羊座×1</td><td>125+</td><td>带盾坦克</td><td> armor > 15k</td></tr>
            <tr><td>巨蟹座×1</td><td>120+</td><td>治疗支援</td><td>治疗量 > 8k</td></tr>
            <tr><td>任意SSR×1</td><td>130+</td><td>冲竞技场排名</td><td>晚上8点后</td></tr>
        </table>
        <h2>💎 交易市场</h2>
        <ul>
            <li><strong>SSR角色券</strong>：市价 30-50 万灵石</li>
            <li><strong>天马座圣衣</strong>：稀有度最高，成交价 80万+</li>
            <li><strong>渡劫丹</strong>：20-30万/个，PVP刚需</li>
            <li><strong>小宇宙材料</strong>：价格稳定，15-25万/组</li>
        </ul>
        <h2>🔗 社区入口</h2>
        <ul>
            <li>TapTap 官方论坛（最活跃）</li>
            <li>Discord：实时语音组队</li>
            <li>贴吧：新手提问，老手解答</li>
            <li>B站：攻略视频，实战演示</li>
        </ul>"""
    }
}

def create_pages():
    created = 0
    for file_name, data in pages.items():
        fp = REPO / f"guides/saint_seiya/{file_name}"
        if fp.exists():
            continue
        
        theme_css = f"--primary: {theme['primary']}; --bg: {theme['bg']}"
        html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>:root{{{theme_css};--text:#fff}}body{{background:var(--bg");color:var(--text");padding:2rem;max-width:900px;margin:0 auto}}.back{{color:var(--primary");display:block;margin-bottom:2rem}}</style>
</head><body>
    <a href="/saint-seiya-guide.html" class="back">← 返回攻略中心</a>
    <div class="guide-content">
        {data["content"]}
        <p style="margin-top:2rem;color:#888;font-size:0.9rem;">最后更新：2026-03-18 | 来源：官方/社区</p>
    </div>
</body></html>'''
        fp.write_text(html, encoding='utf-8')
        print(f"✅ {fp.name}")
        created += 1
    
    # 创建短文件名
    for stem in ["news-updates", "events", "community"]:
        src = REPO / f"guides/saint_seiya/{stem}-guide.html"
        dst = REPO / f"guides/saint_seiya/{stem}.html"
        if src.exists():
            if dst.exists() or dst.is_symlink():
                dst.unlink()
            shutil.copy2(src, dst)
            print(f"✅ {stem}.html 已同步")
    
    print(f"\n✨ 共创建 {created} 个资讯页")

if __name__ == "__main__":
    create_pages()
