#!/bin/bash
# 每日章節自動生成腳本
# 使用方法: ./daily_chapter_generator.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 日誌文件
LOG_FILE="chapter_generation.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "=== 章節生成開始 ($TIMESTAMP) ===" >> "$LOG_FILE"

# 檢查必要工具
if ! command -v python3 &> /dev/null; then
    echo "錯誤: python3 未安裝" | tee -a "$LOG_FILE"
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "錯誤: git 未安裝" | tee -a "$LOG_FILE"
    exit 1
fi

# 檢查Python依賴
echo "檢查Python依賴..." >> "$LOG_FILE"
python3 -c "import requests" 2>> "$LOG_FILE" || {
    echo "安裝Python依賴: requests" | tee -a "$LOG_FILE"
    pip3 install requests >> "$LOG_FILE" 2>&1 || {
        echo "無法安裝requests庫" | tee -a "$LOG_FILE"
        exit 1
    }
}

# 運行章節生成腳本
echo "運行章節生成腳本..." >> "$LOG_FILE"
python3 generate_chapter.py >> "$LOG_FILE" 2>&1

EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ 章節生成完成" >> "$LOG_FILE"
else
    echo "❌ 章節生成失敗，退出碼: $EXIT_CODE" >> "$LOG_FILE"
    # 嘗試使用備用內容
    echo "嘗試使用備用內容..." >> "$LOG_FILE"
    python3 generate_chapter_backup.py 2>> "$LOG_FILE" || {
        echo "備用方案也失敗" >> "$LOG_FILE"
        exit 1
    }
fi

# 記錄完成時間
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "=== 章節生成結束 ($TIMESTAMP) ===" >> "$LOG_FILE"

# 發送通知（可選）
if command -v curl &> /dev/null; then
    # 這裡可以添加通知邏輯，如發送Telegram通知
    echo "通知功能可在此擴展" >> "$LOG_FILE"
fi

exit 0