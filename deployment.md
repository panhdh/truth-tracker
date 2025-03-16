# Truth Tracker 部署說明文件

## 問題修正

### 1. 修改 app.py
- 添加根路由處理和靜態文件配置：
  ```python
  from flask import Flask, jsonify, send_from_directory
  from flask_cors import CORS

  app = Flask(__name__, static_folder='.', static_url_path='')
  CORS(app)  # 啟用跨域支持

  @app.route('/')
  def index():
      return app.send_static_file('index.html')
  ```

### 2. 確認 requirements.txt
確保包含以下依賴：
```
Flask==2.0.1
flask-cors==3.0.10
Werkzeug==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
itsdangerous==2.0.1
click==8.0.1
```

### 3. 更新 index.html
- 將 API 請求路徑更新為絕對路徑：
  ```javascript
  const apiUrl = 'https://truth-tracker-nle0.onrender.com/search/';
  ```

### 4. 提交更新到 GitHub
```bash
git add .
git commit -m "Fix 404 error"
git push
```

## 重新部署到 Render

1. 訪問 [Render 儀表板](https://dashboard.render.com)
2. 進入對應的 Web Service
3. 等待自動重新部署完成
4. 檢查 Logs 標籤頁，確認無錯誤信息
5. 點擊生成的 URL 進行測試（例如 https://truth-tracker-nle0.onrender.com）

## 測試與分享

1. 功能測試
   - 時間軸顯示：確認事件時間軸正確加載
   - 投票功能：測試支持按鈕是否正常運作
   - 提交真相：測試表單提交功能

2. 分享
   - 將應用 URL 分享到 X（Twitter）

## 注意事項

1. 部署失敗處理
   - 檢查 Render 的 Logs 標籤頁查看錯誤信息
   - 確認所有依賴包都已正確列在 requirements.txt 中
   - 驗證 Python 版本兼容性

2. 靜態資源檢查
   - 確保所有 CSS 和 JavaScript 文件存在於倉庫中
   - 檢查文件權限是否正確

3. 安全性考慮
   - 避免在代碼中暴露敏感信息
   - 使用環境變量存儲配置信息
   - 確保 CORS 設置適當