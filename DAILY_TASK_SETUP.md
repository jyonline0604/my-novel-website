# 每日任務設置指南

## 概述

本系統可自動化《科技修真傳》小說的章節生成與發布。每天自動：
1. 根據上一章內容生成新章節
2. 使用相同的HTML格式排版
3. 更新網站首頁
4. 推送到GitHub倉庫（自動觸發GitHub Pages部署）

## 系統要求

- Python 3.6+
- Git
- 網絡連接（用於DeepSeek API和GitHub）

## 安裝步驟

### 1. 設置執行權限
```bash
chmod +x daily_chapter_generator.sh
chmod +x generate_chapter.py
chmod +x generate_chapter_backup.py
```

### 2. 測試運行
```bash
./daily_chapter_generator.sh
```

檢查生成結果：
```bash
tail -n 50 chapter_generation.log
```

### 3. 設置每日定時任務（Cron Job）

#### 方法A：使用crontab（推薦）
```bash
# 編輯crontab
crontab -e

# 添加以下行（每天上午9點運行）
0 9 * * * cd /home/openclaw/.openclaw/workspace/my-novel-website && ./daily_chapter_generator.sh

# 保存並退出
```

#### 方法B：使用systemd定時器（Linux系統）
創建服務文件：
```bash
sudo nano /etc/systemd/system/novel-generator.service
```

內容：
```ini
[Unit]
Description=Novel Chapter Generator
After=network.target

[Service]
Type=oneshot
User=openclaw
WorkingDirectory=/home/openclaw/.openclaw/workspace/my-novel-website
ExecStart=/bin/bash ./daily_chapter_generator.sh
StandardOutput=append:/home/openclaw/.openclaw/workspace/my-novel-website/chapter_generation.log
StandardError=append:/home/openclaw/.openclaw/workspace/my-novel-website/chapter_generation.log

[Install]
WantedBy=multi-user.target
```

創建定時器文件：
```bash
sudo nano /etc/systemd/system/novel-generator.timer
```

內容：
```ini
[Unit]
Description=Daily Novel Chapter Generation

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

啟用定時器：
```bash
sudo systemctl enable novel-generator.timer
sudo systemctl start novel-generator.timer
```

## GitHub配置

### 1. 獲取新的GitHub Personal Access Token

當前Token缺少`workflow`權限，需要新Token：

1. 訪問 https://github.com/settings/tokens
2. 點擊「Generate new token (classic)」
3. 選擇以下權限：
   - `repo`（完整倉庫控制）
   - `workflow`（必須！用於修改GitHub Actions）
4. 生成並複製Token

### 2. 更新Git配置
```bash
cd /home/openclaw/.openclaw/workspace/my-novel-website

# 使用新Token更新remote URL
git remote set-url origin https://新Token@github.com/jyonline0604/my-novel-website.git

# 測試推送
git push origin main
```

## 故障排除

### 1. 章節生成失敗
檢查日誌：
```bash
tail -n 100 chapter_generation.log
```

常見問題：
- **DeepSeek API Key無效**：檢查`auth-profiles.json`中的Key
- **網絡連接問題**：確保可以訪問`api.deepseek.com`
- **Python依賴缺失**：運行`pip3 install requests`

### 2. Git推送失敗
```bash
# 檢查remote配置
git remote -v

# 測試Token有效性
curl -s -H "Authorization: token 你的Token" https://api.github.com/user
```

### 3. 定時任務不運行
```bash
# 檢查cron服務狀態
sudo systemctl status cron

# 檢查cron日誌
sudo grep CRON /var/log/syslog

# 手動測試cron命令
cd /home/openclaw/.openclaw/workspace/my-novel-website && ./daily_chapter_generator.sh
```

## 手動操作

### 強制生成新章節
```bash
cd /home/openclaw/.openclaw/workspace/my-novel-website
python3 generate_chapter.py
```

### 使用備用方案
```bash
cd /home/openclaw/.openclaw/workspace/my-novel-website
python3 generate_chapter_backup.py
```

### 查看所有章節
```bash
ls -la chapter-*.html | tail -10
```

## 監控與維護

### 查看生成歷史
```bash
# 查看日誌
less chapter_generation.log

# 查看Git提交歷史
git log --oneline -20

# 查看GitHub Pages部署狀態
curl -s https://api.github.com/repos/jyonline0604/my-novel-website/pages/builds | jq '.[0]'
```

### 清理舊日誌
```bash
# 保留最近30天的日誌
find . -name "chapter_generation.log" -mtime +30 -delete
```

## 擴展功能

### 1. 添加通知
修改`daily_chapter_generator.sh`，在成功生成後發送通知（Telegram、Email等）。

### 2. 質量檢查
添加章節質量檢查腳本，確保生成的內容符合要求。

### 3. 備份系統
定期備份整個網站倉庫。

## 聯繫與支持

如有問題，請檢查：
1. 日誌文件：`chapter_generation.log`
2. GitHub Actions運行狀態
3. 系統資源使用情況

系統設計為容錯運行，即使AI生成失敗也會使用備用內容，確保每日都有新章節發布。