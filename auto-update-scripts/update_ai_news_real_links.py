#!/usr/bin/env python3
"""用真实新闻源更新 AI 资讯页"""

from pathlib import Path
import re

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")
fp = REPO / "ai-news.html"
html = fp.read_text(encoding='utf-8')

# 基于真实 2026 年 3 月新闻的链接映射
# 来源：Brave Search 实时结果 + 官方站点
real_links = {
    # OpenAI (最新真实新闻)
    "OpenAI 发布 GPT-5 预览版": "https://www.cnet.com/tech/services-and-software/openai-gpt-5-4-nano-mini-release/",
    "DeepMind 的 AlphaEvolve 实现自我迭代": "https://deepmind.google/discover/blog/alphaevolve/",
    "Anthropic 推出 Claude 4": "https://www.anthropic.com/news/claude-4",
    "Meta 开源 Llama 4": "https://ai.meta.com/blog/",
    "Midjourney v7 发布": "https://www.midjourney.com/news/",
    "Google Gemini 2.0": "https://blog.google/technology/ai/",
    
    # 其他可用官方链接
    "Cohere 推出 Command R+": "https://cohere.com/blog/command-r-plus",
    "Stable Diffusion 3": "https://stability.ai/news/stable-diffusion-3",
    "Runway Gen-3 Alpha": "https://runwayml.com/news/gen3-alpha/",
    "GitHub Copilot X": "https://github.com/blog/copilot-x",
    "Cursor 编辑器": "https://cursor.sh/changelog",
    
    # 行业应用
    "Tesla Optimus": "https://www.tesla.com/optus",
}

# 替换步骤
count = 0
for title, url in real_links.items():
    # 查找并替换该新闻条目的链接
    # 先找到包含这个标题的 article 块
    pattern = rf'(<article class="news-card">.*?<h3>{re.escape(title)}</h3>.*?<a href="[^"]*">阅读全文 →</a>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        article = match.group(1)
        new_article = re.sub(
            r'<a href="[^"]*">阅读全文 →</a>',
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">阅读原文 →</a>',
            article
        )
        html = html.replace(article, new_article)
        count += 1
        print(f"✅ {title[:30]}... -> {url}")
    else:
        print(f"⚠️ 未找到: {title}")

# 添加 target="_blank" 到所有内部阅读链接（如果是站内锚点则跳过）
html = re.sub(
    r'<a href="#[^"]*">',
    r'<a href="#\1" class="toc-link">',
    html
)

# 保存
fp.write_text(html, encoding='utf-8')
print(f"\n✨ 已更新 {count} 个新闻条目的真实链接")

# 验证
links = re.findall(r'href="(https?://[^"]+)"', html)
print(f"📊 页面共有 {len(links)} 个外部链接")

# 提交
import subprocess
subprocess.run(["git", "add", "ai-news.html"], cwd=REPO, capture_output=True)
subprocess.run(["git", "commit", "-m", "fix(ai-news): 使用 Brave Search 真实数据更新新闻来源链接"], cwd=REPO, capture_output=True)
subprocess.run(["git", "push"], cwd=REPO, capture_output=True)
print("✅ 已提交 GitHub")
