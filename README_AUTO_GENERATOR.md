# 科技修真傳 - 自動章節生成系統

## 系統已完成設置

### ✅ 已完成功能

1. **自動章節生成**
   - `generate_chapter.py` - 主生成腳本，使用DeepSeek AI API
   - `generate_chapter_backup.py` - 備用生成腳本
   - 自動讀取最新章節，保持情節連貫
   - 使用相同的HTML格式和排版

2. **網站更新**
   - 自動更新首頁章節列表
   - 保持一致的設計風格
   - 添加發布日期標記

3. **GitHub集成**
   - 自動提交到GitHub倉庫
   - 觸發GitHub Pages自動部署
   - 網站地址：https://kofhk.com

4. **每日任務系統**
   - `daily_chapter_generator.sh` - 自動化腳本
   - 完整錯誤處理和日誌記錄
   - 容錯設計（主AI失敗時使用備用內容）

### ⚠️ 需要完成的配置

#### 1. 獲取新的GitHub Token
當前Token缺少`workflow`權限，無法修改GitHub Actions工作流程。

**解決方案：**
1. 訪問 https://github.com/settings/tokens
2. 生成新Token，勾選`repo`和`workflow`權限
3. 更新git配置：
   ```bash
   git remote set-url origin https://新Token@github.com/jyonline0604/my-novel-website.git
   ```

#### 2. 設置每日定時任務
選擇以下任一方法：

**方法A：Cron Job**
```bash
crontab -e
# 添加：0 9 * * * cd /路徑/my-novel-website && ./daily_chapter_generator.sh
```

**方法B：Systemd Timer**
```bash
sudo systemctl enable novel-generator.timer
sudo systemctl start novel-generator.timer
```

詳細設置見 `DAILY_TASK_SETUP.md`

#### 3. 測試DeepSeek API
當前API Key已配置，但需要測試連接：
```bash
python3 -c "
import requests
import json
from pathlib import Path

# 讀取API Key
auth_file = Path('/home/openclaw/.openclaw/agents/main/agent/auth-profiles.json')
with open(auth_file, 'r') as f:
    data = json.load(f)

api_key = data['profiles']['deepseek:default']['key']

# 測試API
response = requests.post(
    'https://api.deepseek.com/chat/completions',
    headers={'Authorization': f'Bearer {api_key}'},
    json={
        'model': 'deepseek-chat',
        'messages': [{'role': 'user', 'content': 'Hello'}],
        'max_tokens': 10
    },
    timeout=10
)
print(f'API測試: {response.status_code}')
"
```

### 🚀 快速開始

1. **設置執行權限**
   ```bash
   chmod +x daily_chapter_generator.sh generate_chapter.py generate_chapter_backup.py
   ```

2. **測試運行**
   ```bash
   ./daily_chapter_generator.sh
   tail -n 50 chapter_generation.log
   ```

3. **設置定時任務**
   ```bash
   # 編輯crontab
   crontab -e
   # 添加：0 9 * * * cd /home/openclaw/.openclaw/workspace/my-novel-website && ./daily_chapter_generator.sh
   ```

4. **監控運行狀態**
   ```bash
   # 查看日誌
   tail -f chapter_generation.log
   
   # 查看章節文件
   ls -la chapter-*.html | tail -5
   
   # 檢查網站更新
   curl -s https://kofhk.com | grep -o '第[^<]*章' | head -5
   ```

### 🔧 文件說明

- `generate_chapter.py` - 主AI生成腳本
- `generate_chapter_backup.py` - 備用生成腳本
- `daily_chapter_generator.sh` - 自動化執行腳本
- `DAILY_TASK_SETUP.md` - 詳細設置指南
- `chapter_generation.log` - 運行日誌（運行後生成）
- `chapter-*.html` - 章節文件
- `.github/workflows/deploy.yml` - GitHub Actions工作流程（需要workflow權限）

### 📊 預期效果

**每天自動完成：**
1. 讀取最新章節內容
2. 使用AI生成新章節（或使用備用內容）
3. 創建符合模板的HTML文件
4. 更新網站首頁
5. 提交到GitHub並觸發部署
6. 記錄運行日誌

**網站更新流程：**
```
本地生成 → Git提交 → GitHub推送 → Pages部署 → kofhk.com更新
```

### 🐛 故障排除

**問題1：Git推送失敗**
```bash
# 檢查remote設置
git remote -v

# 測試Token
curl -s -H "Authorization: token YOUR_TOKEN" https://api.github.com/user | grep login
```

**問題2：AI生成失敗**
```bash
# 檢查DeepSeek API Key
grep -A2 'deepseek:default' /home/openclaw/.openclaw/agents/main/agent/auth-profiles.json

# 測試網絡連接
curl -s https://api.deepseek.com/health --connect-timeout 5
```

**問題3：定時任務不運行**
```bash
# 檢查cron服務
sudo systemctl status cron

# 手動測試
cd /home/openclaw/.openclaw/workspace/my-novel-website
./daily_chapter_generator.sh
```

### 📈 擴展建議

1. **添加質量檢查** - 生成後檢查章節長度和內容質量
2. **添加通知** - 成功生成後發送Telegram/Email通知
3. **定期備份** - 自動備份整個網站
4. **流量監控** - 使用Google Analytics追蹤讀者
5. **讀者互動** - 收集讀者反饋調整生成方向

### 📞 支持

- 檢查日誌：`chapter_generation.log`
- GitHub Issues：https://github.com/jyonline0604/my-novel-website/issues
- 系統狀態：`systemctl status cron` 和 `git status`

---

**系統設計理念：**
- 容錯優先：即使AI失敗，也有備用內容
- 自動化優先：最小化手動干預
- 一致性優先：保持原有風格和格式
- 透明優先：完整日誌記錄所有操作

現在你的小說可以每天自動更新一章了！🎉