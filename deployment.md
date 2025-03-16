# 真相追蹤器部署說明

## 1. 程式碼準備

### 1.1 檢查本地檔案
- 確保 `index.html` 和 `app.py` 都能正常運行
- 檢查 `requirements.txt` 已包含所有依賴：
  ```
  Flask==2.0.1
  Werkzeug==2.0.1
  Jinja2==3.0.1
  MarkupSafe==2.0.1
  itsdangerous==2.0.1
  click==8.0.1
  ```

### 1.2 上傳到 GitHub
1. 初始化 Git 倉庫：
   ```bash
   git init
   ```

2. 添加檔案到暫存區：
   ```bash
   git add index.html app.py requirements.txt
   ```

3. 提交變更：
   ```bash
   git commit -m "初始提交：真相追蹤器專案"
   ```

4. 在 GitHub 創建新倉庫
   - 前往 https://github.com/new
   - 輸入倉庫名稱（例如：truth-tracker）
   - 選擇公開（Public）
   - 不要初始化 README

5. 推送到 GitHub：
   ```bash
   git remote add origin https://github.com/你的用戶名/truth-tracker.git
   git branch -M main
   git push -u origin main
   ```

## 2. Render 部署

### 2.1 註冊 Render 帳號
1. 前往 https://render.com
2. 點擊「Sign Up」
3. 建議使用 GitHub 帳號登入，方便連接倉庫

### 2.2 創建 Web Service
1. 點擊 Dashboard 中的「New +」→「Web Service」
2. 選擇之前創建的 GitHub 倉庫
3. 填寫基本配置：
   - **名稱**：truth-tracker（或其他名稱）
   - **環境**：Python 3
   - **構建命令**：`pip install -r requirements.txt`
   - **啟動命令**：`python app.py`
   - **計劃**：選擇免費方案（Free）

### 2.3 更新前端 API
1. 修改 `index.html` 中的 API 請求地址：
   - 將所有 `fetch('http://localhost:5000/...')` 改為：
   - `fetch('https://你的應用名稱.onrender.com/...')`

2. 重新提交到 GitHub：
   ```bash
   git add index.html
   git commit -m "更新 API 地址為 Render URL"
   git push
   ```

## 3. 測試與分享

### 3.1 功能測試
1. 等待 Render 部署完成（約 5-10 分鐘）
2. 打開應用 URL：`https://你的應用名稱.onrender.com`
3. 測試以下功能：
   - 時間軸顯示
   - 支持投票系統
   - 真相提交功能

### 3.2 分享應用
1. 複製應用 URL
2. 在 X（Twitter）上分享：
   - 建議附上簡短說明和主要功能介紹
   - 加上相關標籤（例如 #真相追蹤 #專案分享）

## 4. 注意事項

### 4.1 Render 免費方案限制
- 15 分鐘無訪問後會進入休眠狀態
- 首次訪問可能需要等待 30 秒左右喚醒
- 每月有 750 小時免費使用時間

### 4.2 未來優化建議
1. 資料持久化
   - 考慮接入 MongoDB 或 PostgreSQL 資料庫
   - 將用戶提交的真相儲存到資料庫
   - 添加用戶認證系統

2. 性能優化
   - 實現前端緩存機制
   - 優化 API 請求頻率
   - 考慮使用 CDN 加速靜態資源

### 4.3 故障排除
- 如果部署失敗，檢查 Render 日誌
- 確保所有依賴都已列在 requirements.txt
- 檢查 API 請求地址是否正確
- 確認 app.py 中的 host 和 port 配置正確