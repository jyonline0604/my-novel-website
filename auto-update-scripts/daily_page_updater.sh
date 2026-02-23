#!/bin/bash
# 網站分頁每日自動更新主腳本
# 負責更新：問劍長生、聖鬥士星矢重生2、Be A Pro Football、AI資訊

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

# 日誌文件
LOG_FILE="auto-update.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "=== 網站分頁自動更新開始 ($TIMESTAMP) ===" >> "$LOG_FILE"

# 檢查必要工具
echo "檢查必要工具..." >> "$LOG_FILE"
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

# 創建今日更新標記
TODAY=$(date '+%Y年%m月%d日')
TODAY_ISO=$(date '+%Y-%m-%d')

# 1. 更新問劍長生攻略
echo "更新問劍長生攻略..." >> "$LOG_FILE"
python3 auto-update-scripts/update_game_guide.py >> "$LOG_FILE" 2>&1
GAME_GUIDE_EXIT=$?

# 2. 更新聖鬥士星矢重生2攻略
echo "更新聖鬥士星矢重生2攻略..." >> "$LOG_FILE"
python3 auto-update-scripts/update_saint_seiya.py >> "$LOG_FILE" 2>&1
SAINT_SEIYA_EXIT=$?

# 3. 更新Be A Pro Football攻略
echo "更新Be A Pro Football攻略..." >> "$LOG_FILE"
python3 auto-update-scripts/update_beapro_football.py >> "$LOG_FILE" 2>&1
BEAPRO_FOOTBALL_EXIT=$?

# 4. 更新AI資訊
echo "更新AI資訊..." >> "$LOG_FILE"
python3 auto-update-scripts/update_ai_news.py >> "$LOG_FILE" 2>&1
AI_NEWS_EXIT=$?

# 檢查所有更新結果
SUCCESS_COUNT=0
FAIL_COUNT=0

if [ $GAME_GUIDE_EXIT -eq 0 ]; then
    SUCCESS_COUNT=$((SUCCESS_COUNT+1))
    echo "✅ 問劍長生攻略更新成功" >> "$LOG_FILE"
else
    FAIL_COUNT=$((FAIL_COUNT+1))
    echo "❌ 問劍長生攻略更新失敗" >> "$LOG_FILE"
fi

if [ $SAINT_SEIYA_EXIT -eq 0 ]; then
    SUCCESS_COUNT=$((SUCCESS_COUNT+1))
    echo "✅ 聖鬥士星矢攻略更新成功" >> "$LOG_FILE"
else
    FAIL_COUNT=$((FAIL_COUNT+1))
    echo "❌ 聖鬥士星矢攻略更新失敗" >> "$LOG_FILE"
fi

if [ $BEAPRO_FOOTBALL_EXIT -eq 0 ]; then
    SUCCESS_COUNT=$((SUCCESS_COUNT+1))
    echo "✅ Be A Pro Football攻略更新成功" >> "$LOG_FILE"
else
    FAIL_COUNT=$((FAIL_COUNT+1))
    echo "❌ Be A Pro Football攻略更新失敗" >> "$LOG_FILE"
fi

if [ $AI_NEWS_EXIT -eq 0 ]; then
    SUCCESS_COUNT=$((SUCCESS_COUNT+1))
    echo "✅ AI資訊更新成功" >> "$LOG_FILE"
else
    FAIL_COUNT=$((FAIL_COUNT+1))
    echo "❌ AI資訊更新失敗" >> "$LOG_FILE"
fi

# 如果有成功更新，提交到GitHub
if [ $SUCCESS_COUNT -gt 0 ]; then
    echo "提交更新到GitHub..." >> "$LOG_FILE"
    
    # 添加已修改的文件
    git add game-guide.html saint-seiya-guide.html beapro-football-guide.html ai-news.html 2>> "$LOG_FILE"
    
    # 提交
    COMMIT_MSG="更新網站分頁內容 ($TODAY)"
    if [ $FAIL_COUNT -gt 0 ]; then
        COMMIT_MSG="$COMMIT_MSG (部分更新失敗)"
    fi
    
    git commit -m "$COMMIT_MSG" >> "$LOG_FILE" 2>&1 || {
        echo "⚠️  Git提交失敗（可能沒有變更）" >> "$LOG_FILE"
    }
    
    # 推送
    git push origin main >> "$LOG_FILE" 2>&1 || {
        echo "❌  Git推送失敗" >> "$LOG_FILE"
        FAIL_COUNT=$((FAIL_COUNT+1))
    }
fi

# 記錄完成時間
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "=== 網站分頁自動更新結束 ($TIMESTAMP) ===" >> "$LOG_FILE"
echo "成功: $SUCCESS_COUNT, 失敗: $FAIL_COUNT" >> "$LOG_FILE"

# 發送簡要狀態報告
echo "📊 網站分頁更新報告 ($TIMESTAMP)" >> "$LOG_FILE"
echo "✅ 成功更新: $SUCCESS_COUNT 個頁面" >> "$LOG_FILE"
echo "❌ 失敗更新: $FAIL_COUNT 個頁面" >> "$LOG_FILE"

# 如果有失敗的更新，記錄詳細信息
if [ $FAIL_COUNT -gt 0 ]; then
    echo "詳細錯誤請查看日誌: $LOG_FILE" >> "$LOG_FILE"
fi

exit 0