#!/usr/bin/env python3
"""
將 LLM 輸出的章節內容轉換為 HTML
支援 markdown 標題 (##, ###) 以及傳統「第X章：」格式
"""

import sys
import re

def convert(content: str) -> str:
    html_lines = []
    in_section = False
    for line_raw in content.split('\n'):
        line = line_raw.strip()
        if not line:
            continue

        # 检测 markdown 二级标题 (## ...) 作为章节
        m_h2 = re.match(r'^(##)\s+(.+)$', line_raw.strip())
        if m_h2:
            title_text = m_h2.group(2).strip()
            if in_section:
                html_lines.append('</div>')
            html_lines.append('<div class="section">')
            html_lines.append(f'<h3 class="section-title">{title_text}</h3>')
            in_section = True
            continue

        # 三级标题 (### ...) 作为节标题
        m_h3 = re.match(r'^(###)\s+(.+)$', line_raw.strip())
        if m_h3:
            sub_title = m_h3.group(2).strip()
            html_lines.append(f'<h4 style="margin-top:1em;margin-bottom:0.5em;">{sub_title}</h4>')
            continue

        # 传统“第X章：...”格式
        if '章：' in line and ('第' in line[:5]):
            if in_section:
                html_lines.append('</div>')
            html_lines.append('<div class="section">')
            html_lines.append(f'<h3 class="section-title">{line}</h3>')
            in_section = True
            continue

        # 普通段落
        html_lines.append(f'<p>{line}</p>')

    if in_section:
        html_lines.append('</div>')

    return '\n'.join(html_lines)

if __name__ == '__main__':
    content = sys.stdin.read()
    html = convert(content)
    print(html)
