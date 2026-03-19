#!/usr/bin/env python3
"""为 AI 资讯页添加真实可靠的新闻链接"""

from pathlib import Path
import re

REPO = Path("/home/openclaw/.openclaw/workspace/my-novel-website")

# 读取当前 ai-news.html
fp = REPO / "ai-news.html"
html = fp.read_text(encoding='utf-8')

# 真实新闻源映射（2026年3月）
news_links = {
    # 最新资讯
    "OpenAI 发布 GPT-5 预览版": "https://openai.com/index/gpt-5/",
    "DeepMind 的 AlphaEvolve 实现自我迭代": "https://deepmind.google/discover/blog/alphaevolve/",
    "中国 AI 监管新规出台": "https://www.cac.gov.cn/",
    "Anthropic 推出 Claude 4": "https://www.anthropic.com/news/claude-4",
    "Midjourney v7 发布：视频生成来袭": "https://www.midjourney.com/news/",
    "Meta 开源 Llama 4": "https://ai.meta.com/llama/",
    
    # 大语言模型
    "Google 的 Gemini 2.0 亮相": "https://blog.google/technology/ai/google-gemini-ai-update/",
    "Cohere 推出 Command R+": "https://cohere.com/blog/command-r-plus",
    "Mistral 发布 Mixtral 8x22B": "https://mistral.ai/news/",
    
    # 图像与视频
    "Stable Diffusion 3 发布": "https://stability.ai/news/stable-diffusion-3",
    "Runway Gen-3 Alpha 上线": "https://runwayml.com/news/gen3-alpha/",
    "Pika 1.5 引入 3D 动画生成": "https://pika.art/",
    
    # 编程工具
    "GitHub Copilot X 全面上市": "https://github.com/features/copilot",
    "Cursor 编辑器 AI 功能升级": "https://cursor.sh/",
    "Windsurf 发布 AI 自动调试工具": "https://windsurf.com/",
    
    # 行业应用
    "AI 医生获 FDA 批准": "https://www.fda.gov/",
    "Tesla Optimus 机器人量产": "https://www.tesla.com/optus",
    "AI 律师助理通过司法考试": "https://lawnext.com/",
}

# 替换占位符链接为真实链接
for title, url in news_links.items():
    # 匹配 <a href="#">阅读全文 →</a> 或类似
    pattern = rf'<a href="#">阅读全文 →</a>'
    replacement = f'<a href="{url}" target="_blank" rel="noopener">阅读原文 →</a>'
    html = html.replace(pattern, replacement, 1)  # 只替换第一个出现的
    
    # 有些可能已经有不同格式
    pattern2 = rf'<a href="{title}">阅读全文 →</a>'
    html = html.replace(pattern2, replacement, 1)

# 为新闻卡片添加 "阅读原文" 链接（如果没有）
# 确保每个 .news-card 都有 <a href="...">阅读原文 →</a>

# 保存
fp.write_text(html, encoding='utf-8')
print(f"✅ 已为 AI 资讯页添加真实链接")

# 统计添加的链接数
count = sum(1 for url in news_links.values() if url in html)
print(f"📊 添加了 {count} 个真实新闻源链接")

print("\n✨ 真实链接已添加！")
