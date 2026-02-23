# 網站分頁自動更新系統設置指南

## 概述

本系統為《科技修真傳》網站的其他分頁提供每日自動更新功能，包括：
1. **問劍長生**遊戲攻略
2. **聖鬥士星矢：重生2**攻略  
3. **Be A Pro Football**足球攻略
4. **AI資訊**新聞頁面

## 系統架構

### 文件結構
```
my-novel-website/
├── auto-update-scripts/
│   ├── daily_page_updater.sh      # 主更新腳本
│   ├── update_config.json         # 配置檔案
│   ├── update_game_guide.py       # 問劍長生更新
│   ├── update_saint_seiya.py      # 聖鬥士星矢更新
│   ├── update_beapro_football.py  # Be A Pro Football更新
│   └── update_ai_news.py          # AI資訊更新
├── game-guide.html                # 問劍長生攻略
├── saint-seiya-guide.html         # 聖鬥士星矢攻略
├── beapro-football-guide.html     # Be A Pro Football攻略
├── ai-news.html                   # AI資訊頁面
├── auto-update.log                # 更新日誌
└── PAGE_UPDATE_SYSTEM_SETUP.md    # 本文檔
```

### 更新流程
```
每日定時觸發
    ↓
執行 daily_page_updater.sh
    ↓
按順序更新四個頁面
    ↓
更新時間戳和內容
    ↓
提交到GitHub
    ↓
觸發GitHub Pages自動部署
```

## 快速開始

### 1. 設置執行權限
```bash
cd /home/openclaw/.openclaw/workspace/my-novel-website
chmod +x auto-update-scripts/daily_page_updater.sh
chmod +x auto-update-scripts/*.py
```

### 2. 測試更新系統
```bash
# 測試單個頁面更新
python3 auto-update-scripts/update_game_guide.py

# 測試所有頁面更新
./auto-update-scripts/daily_page_updater.sh

# 查看日誌
tail -f auto-update.log
```

### 3. 設置每日定時任務
```bash
crontab -e
```

添加以下行（每天上午10點運行）：
```
0 10 * * * cd /home/openclaw/.openclaw/workspace/my-novel-website && ./auto-update-scripts/daily_page_updater.sh
```

或者為每個頁面設置不同時間：
```
# 問劍長生 - 10:00
0 10 * * * cd /路徑 && python3 auto-update-scripts/update_game_guide.py

# 聖鬥士星矢 - 11:00  
0 11 * * * cd /路徑 && python3 auto-update-scripts/update_saint_seiya.py

# Be A Pro Football - 12:00
0 12 * * * cd /路徑 && python3 auto-update-scripts/update_beapro_football.py

# AI資訊 - 14:00
0 14 * * * cd /路徑 && python3 auto-update-scripts/update_ai_news.py
```

## 配置說明

### update_config.json
```json
{
  "update_schedule": {
    "game_guide": {
      "enabled": true,           # 是否啟用
      "update_time": "10:00",    # 更新時間
      "update_frequency": "daily", # 更新頻率
      "requires_ai": false       # 是否需要AI生成內容
    },
    // ... 其他頁面配置
  },
  "system_settings": {
    "git_enabled": true,         # 是否自動提交到GitHub
    "auto_push": true,           # 是否自動推送
    "test_mode": false           # 測試模式
  }
}
```

### 自定義更新內容

每個頁面更新腳本都包含以下功能：
1. **時間戳更新** - 自動更新「最後更新」時間
2. **內容更新** - 更新攻略摘要、新聞內容
3. **AI增強** - 可選的AI生成內容（需要DeepSeek API）

## 頁面特定設置

### 1. 問劍長生攻略 (`update_game_guide.py`)
- 更新遊戲版本資訊
- 添加每日攻略提示
- 檢查遊戲更新狀態

### 2. 聖鬥士星矢攻略 (`update_saint_seiya.py`)  
- 更新遊戲活動資訊
- 添加戰術建議
- 檢查版本更新

### 3. Be A Pro Football攻略 (`update_beapro_football.py`)
- 更新轉會市場資訊
- 生成戰術分析
- 添加專家建議

### 4. AI資訊頁面 (`update_ai_news.py`)
- 獲取最新AI新聞
- 生成技術分析
- 添加趨勢預測

## 高級功能

### AI內容生成
要啟用AI生成內容，需要：
1. 有效的DeepSeek API Key
2. 在腳本中啟用AI功能
3. 設置適當的提示詞

示例配置：
```python
# 在更新腳本中啟用AI
def generate_ai_content(prompt):
    # 使用DeepSeek API生成內容
    # 需要設置 DEEPSEEK_API_KEY 環境變數
    pass
```

### 新聞源配置
AI資訊頁面可以配置多個新聞源：
```json
"news_sources": [
  "TechCrunch AI",
  "MIT Technology Review", 
  "AI Research Papers",
  "Industry News"
]
```

## 監控與維護

### 查看日誌
```bash
# 實時查看日誌
tail -f auto-update.log

# 查看最近更新
grep "✅" auto-update.log | tail -20

# 查看錯誤
grep "❌" auto-update.log
```

### 檢查更新狀態
```bash
# 檢查文件修改時間
ls -la game-guide.html saint-seiya-guide.html beapro-football-guide.html ai-news.html

# 檢查Git提交記錄
git log --oneline -10 --grep="更新網站分頁"

# 檢查GitHub Actions狀態
open https://github.com/jyonline0604/my-novel-website/actions
```

### 備份與恢復
系統支持自動備份：
```bash
# 手動備份
cp game-guide.html game-guide.html.backup.$(date +%Y%m%d)

# 恢復備份
cp game-guide.html.backup.20260223 game-guide.html
```

## 故障排除

### 常見問題

#### 問題1：Python依賴缺失
```bash
# 安裝必要依賴
pip3 install requests
```

#### 問題2：權限問題
```bash
# 設置執行權限
chmod +x auto-update-scripts/*.py
chmod +x auto-update-scripts/daily_page_updater.sh
```

#### 問題3：Git推送失敗
```bash
# 檢查Git配置
git remote -v
git status

# 檢查Token權限
curl -s -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

#### 問題4：內容更新不正確
1. 檢查日誌文件 `auto-update.log`
2. 驗證HTML結構是否改變
3. 檢查正則表達式匹配

### 測試模式
啟用測試模式避免實際修改：
```json
"system_settings": {
  "test_mode": true
}
```

## 擴展功能

### 添加新頁面
1. 創建新的更新腳本 `update_new_page.py`
2. 添加到 `update_config.json`
3. 更新 `daily_page_updater.sh`

### 通知系統
可以擴展添加通知功能：
- Telegram通知更新結果
- Email報告
- Discord Webhook

### 數據分析
添加訪問統計：
- Google Analytics整合
- 自定義訪問追蹤
- 熱門內容分析

## 性能優化

### 定時優化
- 錯開更新時間避免服務器負載
- 設置重試機制
- 實現增量更新

### 緩存策略
- 緩存API響應
- 實現本地新聞存儲
- 優化HTML生成

## 安全考慮

### API Key保護
- 使用環境變數儲存敏感資訊
- 不在代碼中硬編碼API Key
- 定期輪換Token

### 內容審核
- 驗證AI生成內容
- 過濾不當內容
- 實現人工審核流程

### 訪問控制
- 限制更新腳本權限
- 實現日誌審計
- 設置失敗警報

## 聯繫與支持

如有問題，請檢查：
1. 日誌文件：`auto-update.log`
2. GitHub Issues：https://github.com/jyonline0604/my-novel-website/issues
3. 系統狀態：`crontab -l` 和 `git status`

---

## 更新歷史

### v1.0 (2026-02-23)
- 初始版本發布
- 支持四個頁面自動更新
- 基本時間戳和內容更新
- GitHub自動提交功能

### 計劃功能
- AI內容生成增強
- 多新聞源支持
- 通知系統
- 數據分析儀表板

---

**系統設計理念：**
- 模塊化：每個頁面獨立更新
- 可擴展：易於添加新頁面
- 容錯性：失敗時不影響其他頁面
- 透明性：完整日誌記錄

現在你的網站所有分頁都可以每天自動更新了！🎉