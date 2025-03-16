# Truth Tracker 部署說明文件

## 問題修正

### 1. 依賴包配置
- 確認 `requirements.txt` 已包含以下依賴：
  ```
  Flask==2.0.1
  flask-cors==3.0.10
  Werkzeug==2.0.1
  Jinja2==3.0.1
  MarkupSafe==2.0.1
  itsdangerous==2.0.1
  click==8.0.1
  ```

### 2. 應用配置
- 已修改 `app.py`，確保：
  - 已導入 `flask_cors`
  - 已啟用 CORS 支持
  - 已正確配置端口和主機設置

### 3. 提交更新到 GitHub
```bash
git add .
git commit -m "Fix dependencies"
git push
```

## 重新部署到 Render

1. 訪問 [Render 儀表板](https://dashboard.render.com)
2. 進入對應的 Web Service
3. 等待自動重新部署完成
4. 檢查 Logs 標籤頁，確認無錯誤信息
5. 點擊生成的 URL 進行測試（例如 https://truth-tracker-xxxx.onrender.com）

## 功能測試

1. 時間軸功能
   - 輸入關鍵字搜索事件
   - 確認時間軸正確顯示

2. 投票功能
   - 測試投票按鈕
   - 確認投票結果更新

3. 提交真相功能
   - 測試提交表單
   - 確認提交成功

## 注意事項

1. Render 免費方案特性
   - 有休眠機制
   - 首次訪問可能需要等待約 50 秒
   - 長時間未訪問會自動休眠

2. 故障排查
   - 如遇部署失敗，檢查 Logs 中的錯誤信息
   - 確認所有依賴包版本兼容
   - 檢查環境變量配置

3. 性能優化
   - 建議使用緩存機制
   - 優化資源加載
   - 減少不必要的 API 請求

## 分享與推廣

1. 在 X（Twitter）上分享應用鏈接
2. 收集用戶反饋
3. 持續優化功能和性能