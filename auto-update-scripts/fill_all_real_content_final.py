#!/usr/bin/env python3
"""
批量填充所有占位攻略页，确保每个详细页都有真实内容
"""

from pathlib import Path
import re

REPO_DIR = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# 完整真实内容库（基于前期创作的真实内容 + 新补充）
REAL_GUIDE_CONTENT = {
    # 问剑长生
    "guides/game_guide/sword-guide.html": {
        "title": "剑修神通",
        "content": """<h1>剑修神通（完整版）</h1>
        <p>剑修是问道长生的核心输出职业。本文将深入剖析剑修神通的最佳搭配。</p>
        <h2>⚔️ 神通体系总览</h2>
        <ul>
            <li><strong>裂地斩</strong>：200% 攻击力，附加地脉状态（+20%易伤）</li>
            <li><strong>破空剑</strong>：180% 攻击力，无视 30% 防御</li>
            <li><strong>斩魄</strong>：降低目标防御，持续 8 秒</li>
        </ul>
        <h2>🔥 搭配方案</h2>
        <p><strong>爆击流</strong>：裂地斩 + 破空剑 + 斩魄 + 疾风步<br>
        核心：快速积攒爆击值，3秒内打出爆发伤害。</p>
        <p><strong>持续流</strong>：烈焰剑 + 寒冰斩 + 闪电链 + 金刚护体<br>
        核心：元素 combination，持续灼烧+冰冻+麻痹。</p>
        <h2>💡 操作技巧</h2>
        <ol>
            <li>开战先上「斩魄」减防，再接「裂地斩」</li>
            <li>「破空剑」留到敌人血量 < 50% 时收割</li>
            <li>BOSS 狂暴阶段（< 30%）开所有技能 + 攻击药水</li>
        </ol>"""
    },
    "guides/game_guide/pet-guide.html": {
        "title": "灵兽驯养",
        "content": """<h1>灵兽驯养大全</h1>
        <p>灵兽是问道长生中最重要的战斗伙伴。本文将详细介绍如何捕捉、培养极品灵兽。</p>
        <h2>🐉 灵兽品质与资质</h2>
        <ul>
            <li><strong>普通（白）</strong>：资质 100-300，过渡用</li>
            <li><strong>优秀（绿）</strong>：资质 300-600，日常任务</li>
            <li><strong>稀有（紫）</strong>：资质 900-1200，团队战</li>
            <li><strong>史诗（橙）</strong>：资质 1200-1500，PVE/PVE 核心</li>
            <li><strong>传说（红）</strong>：资质 1500-2000，渡劫必备</li>
        </ul>
        <h2>📍 稀有灵兽刷新地点</h2>
        <ul>
            <li><strong>玄武</strong>：北境冰川，每日 20:00-22:00（传说）</li>
            <li><strong>青龙</strong>：东海龙宫，周三/周六 整点（史诗）</li>
            <li><strong>朱雀</strong>：南疆火山，需完成任务（史诗）</li>
        </ul>
        <h2>🎣 捕捉技巧</h2>
        <ol>
            <li>使用对应属性高级捕捉符（成功率 +30%）</li>
            <li>在灵兽 HP < 30% 时捕捉，成功率最高</li>
            <li>清晨 6-8 点是灵兽活跃期</li>
            <li>使用「灵兽诱饵」提升出现几率 20%</li>
        </ol>
        <h2>💎 培养建议</h2>
        <ul>
            <li><strong>精养一只</strong>：一个极品灵兽 > 五个平庸的</li>
            <li><strong>技能</strong>：被动技能优先（生存/增伤）</li>
            <li><strong>资质上限</strong>：极品资质 ≥ 1800</li>
        </ul>"""
    },
    "guides/game_guide/craft-guide.html": {
        "title": "炼器系统",
        "content": """<h1>炼器系统攻略</h1>
        <p>炼器是提升战力的核心途径。本文将解密炼器机制，教你如何炼出极品属性。</p>
        <h2>🔥 装备品质分级</h2>
        <ul>
            <li><strong>白色</strong>：基础属性，无附加</li>
            <li><strong>绿色</strong>：+1 条附加属性</li>
            <li><strong>蓝色</strong>：+2 条附加属性</li>
            <li><strong>紫色</strong>：+3 条附加，解锁 1 个词缀槽</li>
            <li><strong>橙色</strong>：+4 条附加，解锁 2 个词缀槽，可附魔</li>
            <li><strong>红色</strong>：+5 条附加，解锁 3 个词缀槽，可附魔+洗练</li>
        </ul>
        <h2>📊 成功率与保底</h2>
        <p>炼器成功率 30%，幸运符可提升至 60%。失败 10 次后下一次必成功（保底机制）。</p>
        <h2>💎 极品属性搭配</h2>
        <ul>
            <li><strong>武器</strong>：攻击% + 暴击率% + 伤害加深%</li>
            <li><strong>防具</strong>：生命% + 防御% + 减伤%</li>
            <li><strong>饰品</strong>：暴击伤害% + 穿透% + 吸血%</li>
        </ul>
        <h2>⏰ 最佳炼器时机</h2>
        <ol>
            <li>每日 <strong>整点</strong>（0:00-23:00）系统有小幅成功率提升</li>
            <li>每月 <strong>1 号和 15 号</strong> 有「炼器狂欢」活动，成功率 +20%</li>
            <li>周日全天是双倍祝福值时间</li>
        </ol>"""
    },
    "guides/game_guide/ascension-guide.html": {
        "title": "飞升渡劫",
        "content": """<h1>飞升渡劫完整指南</h1>
        <p>渡劫是问道长生中最具挑战性的系统。本文将详细介绍如何成功渡劫。</p>
        <h2>⚡ 渡劫机制</h2>
        <ul>
            <li><strong>天劫类型</strong>：九重天雷、三昧真火、空间裂缝</li>
            <li><strong>渡劫时间</strong>：每条天雷间隔 10 秒，共 9 波</li>
            <li><strong>保命手段</strong>：每次渡劫有 3 次「替身符」机会</li>
        </ul>
        <h2>🔥 渡劫准备清单</h2>
        <ol>
            <li><strong>抗性装备</strong>：至少 3 件 +30% 雷抗/火抗/空间抗性装备</li>
            <li><strong>血瓶</strong>：红药 50 个 + 瞬回药 10 个</li>
            <li><strong>护盾符</strong>：「九天护盾符」x20，可抵消一次即死</li>
            <li><strong>道友护法</strong>：邀请 3 位道友为你分担 60% 伤害</li>
        </ol>
        <h2>💎 实战技巧</h2>
        <ul>
            <li><strong>走位</strong>：保持移动，不要站在同一位置超过 3 秒</li>
            <li><strong>技能</strong>：开渡劫瞬间立刻开无敌技能（如有）</li>
            <li><strong>节奏</strong>：每波天雷之间有 2 秒安全期，用于补血</li>
        </ul>"""
    },
    "guides/game_guide/resource-guide.html": {
        "title": "资源管理",
        "content": """<h1>资源管理完全指南</h1>
        <p>资源管理决定了你能走多远。本篇教你如何最大化资源利用效率。</p>
        <h2>💰 资源优先级排序</h2>
        <table border="1" cellpadding="8">
            <tr><th>资源类型</th><th>优先级</th><th>说明</th></tr>
            <tr><td>体力</td><td>S</td><td>100% 用于主线+装备副本，绝不浪费</td></tr>
            <tr><td>灵石</td><td>A</td><td>优先主角装备，其次主角灵石，最后伙伴</td></tr>
            <tr><td>材料</td><td>B</td><td>紫色以上保留，白色绿色用于合成</td></tr>
            <tr><td>绑元</td><td>A</td><td>存起来等活动，不要乱买</td></tr>
        </table>
        <h2>⏰ 资源重置时间</h2>
        <ul>
            <li><strong>体力</strong>：每日 6:00 和 18:00 各恢复 100 点</li>
            <li><strong>副本次数</strong>：每日 5:00 重置</li>
            <li><strong>商店刷新</strong>：每 6 小时自动刷新，可手动</li>
        </ul>
        <h2>💎 省资源技巧</h2>
        <ol>
            <li><strong>不要升级低品质装备</strong>：只在紫色以上装备上投入资源</li>
            <li><strong>合成保留</strong>：将 3 件相同品质装备合成下一级</li>
            <li><strong>活动囤货</strong>：双倍掉落活动期间集中刷资源</li>
            <li><strong>投资性价比</strong>：一个满级主角 > 五个半成型角色</li>
        </ol>"""
    },
    "guides/game_guide/boss-guide.html": {
        "title": "BOSS攻略",
        "content": """<h1>BOSS战通关攻略</h1>
        <p>BOSS战是问道长生中最具挑战性的 PVE 内容。本文将为你剖析所有 BOSS 机制与应对策略。</p>
        <h2>📈 BOSS 机制分类</h2>
        <ul>
            <li><strong>狂暴型</strong>：血量 < 30% 后大幅提升伤害与速度</li>
            <li><strong>召唤型</strong>：周期性召唤小怪，需要优先清理</li>
            <li><strong>控制型</strong>：频繁使用眩晕、减速、沉默技能</li>
            <li><strong>即死型</strong>：某些技能命中直接秒杀，必须躲避</li>
        </ul>
        <h2>⚔️ 通用打法模板</h2>
        <ol>
            <li><strong>第一阶段</strong>：熟悉技能，不要贪输出，活着最重要</li>
            <li><strong>第二阶段</strong>：BOSS 狂暴，开启所有加攻击技能</li>
            <li><strong>第三阶段</strong>：如果 BOSS 召唤小怪，立即转火清理</li>
            <li><strong>关键技能</strong>：计算 BOSS 大招冷却，提前开无敌或闪避</li>
        </ol>
        <h2>🔥 剑修 BOSS 战技巧</h2>
        <p><strong>神通优先级</strong>：斩魄（减防）→ 裂地斩（伤害）→ 破空剑（收割）</p>
        <p><strong>走位要点</strong>：保持中距离，利用剑气范围优势，不要贴脸</p>
        <p><strong>爆发时机</strong>：BOSS 释放长技能时，是其硬直期，全力输出</p>"""
    },

    # 圣斗士星矢
    "guides/saint_seiya/cosmo-guide.html": {
        "title": "小宇宙燃烧",
        "content": """<h1>小宇宙燃烧机制详解</h1>
        <p>小宇宙系统是圣斗士星矢重生2最核心的战斗机制。理解并善用小宇宙燃烧，是提升战斗力的关键。</p>
        <h2>⚡ 什么是小宇宙燃烧</h2>
        <ul>
            <li><strong>攻击力提升</strong>：+50%</li>
            <li><strong>防御力提升</strong>：+30%</li>
            <li><strong>技能冷却缩短</strong>：-20%</li>
            <li><strong>持续时间</strong>：15 秒（可通过天赋延长至 20 秒）</li>
        </ul>
        <h2>🔥 如何快速积攒小宇宙</h2>
        <ul>
            <li><strong>普通攻击</strong>：每次攻击获得 5% 小宇宙</li>
            <li><strong>技能释放</strong>：释放技能获得 15% 小宇宙</li>
            <li><strong>受到攻击</strong>：格挡或闪避时获得 3% 小宇宙</li>
            <li><strong>连击数</strong>：每达成 5 连击额外获得 10%</li>
        </ul>
        <h2>💎 燃烧时机策略</h2>
        <ul>
            <li><strong>BOSS 战</strong>：留到 BOSS 狂暴阶段（< 30% 血）再燃烧</li>
            <li><strong>多人副本</strong>：队伍中 1-2 人保持燃烧，不要全部同时</li>
            <li><strong>竞技场 PVP</strong>：开场 10 秒内必须燃烧，否则被压制</li>
        </ul>"""
    },
    "guides/saint_seiya/team-composition-guide.html": {
        "title": "阵容搭配",
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
        <p><strong>原理</strong>：穆先手盾 → 沙加沉默 → 紫龙破甲 → 星矢爆发 → 迪斯治疗</p>"""
    },
    "guides/saint_seiya/gacha-guide.html": {
        "title": "黄金抽卡",
        "content": """<h1>黄金抽卡策略</h1>
        <p>抽卡是圣斗士最贵的系统。本文将教你如何最大化石头利用率。</p>
        <h2>🎯 抽取优先级排名</h2>
        <ol>
            <li><strong>T0（必抽）</strong>：射手座、双子座、天马座</li>
            <li><strong>T1（强力替代）</strong>：龙座、白羊座、处女座</li>
            <li><strong>T2（过渡用）</strong>：青铜圣斗士，中前期可使用</li>
        </ol>
        <h2>💎 抽卡技巧</h2>
        <ul>
            <li><strong>UP 活动期间</strong>：绝对不要在其他时间抽，专注攒石头</li>
            <li><strong>保底机制</strong>：每 10 连抽必定出 SR，90 抽必出 SSR</li>
            <li><strong>时机选择</strong>：新角色上线第一周有加强概率</li>
            <li><strong>资源分配</strong>：一个 SSR 满命 > 三个 SSR 零命</li>
        </ul>
        <h2>📊 性价比赛算</h2>
        <p><strong>一个 SSR 满命</strong>：约 18000 石头（≈ 300 抽）</p>
        <p><strong>建议</strong>：买月卡 + 通行证，45 天攒 18000+ 石头，等 UP 版本才抽</p>"""
    },
    "guides/saint_seiya/pvp-strategy-guide.html": {
        "title": "竞技场攻略",
        "content": """<h1>竞技场实战攻略</h1>
        <p>排名赛、竞技场实战解析，教你把把赢的终极阵容。</p>
        <h2>🏆 T0 竞技场阵容</h2>
        <p><strong>配置</strong>：星矢 + 紫龙 + 穆 + 沙加 + 迪斯马斯克</p>
        <h2>⚔️ 对位克制策略</h2>
        <ul>
            <li><strong>遇到控场队</strong>：给星矢装备抗性 + 免控石，优先点掉对面控制</li>
            <li><strong>遇到爆发队</strong>：穆的护盾一定要在敌人开大前开启</li>
            <li><strong>遇到治疗队</strong>：沙加的沉默是关键，务必锁定对面治疗</li>
        </ul>
        <h2>📈 词条优先级</h2>
        <p><strong>输出</strong>：暴击率 > 暴击伤害 > 攻击% > 穿透<br>
        <strong>坦克</strong>：生命% > 防御% > 抗性 > 格挡<br>
        <strong>速度</strong>：加速度词条，PVP 速度没有上限</p>"""
    },
    "guides/saint_seiya/zodiac-temple-guide.html": {
        "title": "十二宫副本",
        "content": """<h1>十二宫副本完全攻略</h1>
        <p>十二宫是圣斗士星矢重生2最高难度的副本。本文将为你详解 12 宫的每个 BOSS 打法。</p>
        <h2>🏛️ 十二宫顺序</h2>
        <ol>
            <li>白羊宫 - 穆（治疗+BOSS）</li>
            <li>金牛宫 - 阿鲁迪巴（高防御坦克）</li>
            <li>双子宫 - 撒加（双人格，控制+输出）</li>
            <li>巨蟹宫 - 迪斯马斯克（召唤+治疗）</li>
            <li>狮子宫 - 艾欧利亚（高爆发）</li>
            <li>处女宫 - 沙加（沉默+减益）</li>
            <li>天秤宫 - 童虎（均衡型，技能全面）</li>
            <li>天蝎宫 - 米罗（持续伤害+中毒）</li>
            <li>人马宫 - 艾俄洛斯（远程射手）</li>
            <li>摩羯宫 - 修罗（破防+高攻）</li>
            <li>水瓶宫 - 卡妙（冰系控制）</li>
            <li>双鱼宫 - 阿布罗狄（魅惑+持续伤害）</li>
        </ol>
        <h2>⚔️ 组队建议</h2>
        <ul>
            <li><strong>最低配置</strong>：2 个输出 + 1 个坦克 + 1 个治疗 + 1 个控制</li>
            <li><strong>推荐配置</strong>：星矢 + 紫龙 + 穆 + 沙加 + 迪斯马斯克（标准阵容）</li>
        </ul>
        <h2>💎 BOSS special机制</h2>
        <p><strong>双子宫</strong>：撒加会切换人格，控制人格时优先击杀<br>
        <strong>巨蟹宫</strong>：每波召唤小怪，需要快速清理避免治疗<br>
        <strong>处女宫</strong>：沉默会使你无法回血，带解药</p>"""
    },

    # Be A Pro Football
    "guides/beapro_football/formation-433-guide.html": {
        "title": "战术阵型大全",
        "content": """<h1>4-3-3 攻击阵型详解</h1>
        <p>4-3-3 是最经典也是最有效的进攻阵型，提供强大的边路进攻和禁区渗透能力。</p>
        <h2>📋 阵型站位</h2>
        <ul>
            <li><strong>GK</strong>：门将（1 人）</li>
            <li><strong>DEF</strong>：中后卫 x2 + 边后卫 x2</li>
            <li><strong>MID</strong>：后腰 x1 + 中前卫 x2</li>
            <li><strong>ATT</strong>：左边锋 + 中锋 + 右边锋</li>
        </ul>
        <h2>⚽ 球员属性要求</h2>
        <h3>边锋（LW/RW）</h3>
        <ul>
            <li>速度：> 85（必须）</li>
            <li>盘带：> 80</li>
            <li>射门：> 75</li>
            <li>耐力：> 80（需要回防）</li>
        </ul>
        <h2>🎯 战术设置</h2>
        <ol>
            <li><strong>进攻风格</strong>：控球 + 边路突破</li>
            <li><strong>防线位置</strong>：高防线（70-75）</li>
            <li><strong>压迫强度</strong>：高强度（65-70）</li>
            <li><strong>传球节奏</strong>：mixed（混合）</li>
        </ol>
        <h2>📈 实战技巧</h2>
        <ul>
            <li><strong>边路配合</strong>：边锋内切 + 边后卫套上，形成人数优势</li>
            <li><strong>中锋跑位</strong>：设置「突前」或「伪九号」，拉扯对方中卫空间</li>
            <li><strong>转换防守</strong>：丢失球权后立即压迫对方边锋</li>
        </ul>"""
    },
    "guides/beapro_football/player-training-guide.html": {
        "title": "球员培养指南",
        "content": """<h1>球员培养完全指南</h1>
        <p>如何打造最强球员？本文详解训练项目、技能提升、转会策略。</p>
        <h2>📊 训练项目优先级</h2>
        <table border="1" cellpadding="8">
            <tr><th>位置</th><th>核心训练</th><th>次要训练</th></tr>
            <tr><td>前锋</td><td>射门、终结</td><td>盘带、速度</td></tr>
            <tr><td>中场</td><td>传球、视野</td><td>控球、体能</td></tr>
            <tr><td>后卫</td><td>防守、抢断</td><td>体能、头球</td></tr>
            <tr><td>门将</td><td>扑救、反应</td><td>手抛球、出击</td></tr>
        </table>
        <h2>🎯 潜力开发</h2>
        <ul>
            <li><strong>年轻球员</strong>：18-22 岁，训练速度 +30%，优先核心属性</li>
            <li><strong>黄金期</strong>：23-28 岁，属性达到峰值，可加练第二技能</li>
            <li><strong>衰退期</strong>：> 29 岁，训练效果减半，建议出售</li>
        </ul>
        <h2>💎 技能学习</h2>
        <p>每个球员可学习 2-3 个技能。最佳技能组合：<br>
        <strong>前锋</strong>：临门一脚 + 假动作 + 冒险突破<br>
        <strong>中场</strong>：组织核心 + 长传大师 + 远射</p>
        <h2>📈 转会市场策略</h2>
        <ol>
            <li><strong>低买高卖</strong>：18-22 岁潜力股，培养 1-2 年后高价卖出</li>
            <li><strong>合同管理</strong>：合同只剩 1 年时谈判，价格更低</li>
            <li><strong>薪资平衡</strong>：总薪资不超过预算的 70%</li>
        </ol>"""
    }
}

def fill_guides():
    filled = 0
    for file_path, data in REAL_GUIDE_CONTENT.items():
        p = Path(file_path)
        if not p.exists():
            print(f"❌ 不存在: {file_path}")
            continue
        
        html = p.read_text(encoding='utf-8')
        
        # 检查是否已有真实内容（非占位符）
        if "placeholder" in html or "正在撰写" in html:
            # 替换整个 body 内容
            theme_colors = {
                "game_guide": ("#d4a017", "#0a0a0a"),
                "saint_seiya": ("#ffd700", "#1a1a2e"),
                "beapro_football": ("#2ecc71", "#0d1b2a"),
                "kai_tian": ("#9b59b6", "#1a0a2e")
            }
            game_type = file_path.split('/')[1]
            primary, bg = theme_colors.get(game_type, ("#888", "#000"))
            
            new_html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data["title"]} - 科技修真傳</title>
    <style>
        :root {{ --primary: {primary}; --bg: {bg}; --text: #fff; --card-bg: rgba(255,255,255,0.05); }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 80px 2rem 2rem; max-width: 900px; margin: 0 auto; line-height: 1.8; }}
        .back-link {{ color: var(--primary); margin-bottom: 2rem; display: block; text-decoration: none; }}
        .guide-content {{ background: var(--card-bg); padding: 2rem; border-radius: 12px; border: 1px solid var(--primary); }}
        h1 {{ color: var(--primary); font-size: 2rem; margin-bottom: 1rem; }}
        h2 {{ color: var(--primary); font-size: 1.5rem; margin: 2rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 1rem; }}
        p {{ margin-bottom: 1rem; color: #bbb; }}
        ul, ol {{ margin-left: 2rem; margin-bottom: 1rem; color: #bbb; }}
        li {{ margin-bottom: 0.5rem; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
        th, td {{ border: 1px solid var(--primary); padding: 0.8rem; text-align: left; }}
        th {{ background: rgba(0,0,0,0.3); color: var(--primary); }}
    </style>
</head>
<body>
    <a href="/{game_type}-guide.html" class="back-link"><i class="fas fa-arrow-left"></i> 返回攻略中心</a>
    <div class="guide-content">
        {data["content"]}
        <p style="margin-top:2rem; color:#888; font-size:0.9rem;">最后更新：2026-03-18 | 作者：小肥喵</p>
    </div>
</body></html>'''
            
            p.write_text(new_html, encoding='utf-8')
            print(f"✅ 填充: {file_path} - {data['title']}")
            filled += 1
        else:
            print(f"⚠️ 跳过: {file_path} 已有内容")
    
    print(f"\n✨ 共填充 {filled} 个详细攻略页")
    return filled

if __name__ == "__main__":
    fill_guides()
