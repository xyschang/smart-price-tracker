# Debug Log

## 2026-06-01 Render 部署失敗：gunicorn 找不到

### 問題

Render 部署時出現：

```text
gunicorn: command not found
Exited with status 127
```

### 原因

Render 的 Start Command 使用：

```bash
gunicorn app:app
```

但 `requirements.txt` 裡沒有安裝 `gunicorn`，所以伺服器找不到啟動指令。

### 解法

在 `requirements.txt` 加入：

```txt
gunicorn
```

並新增 `runtime.txt` 指定 Python 版本：

```txt
python-3.12.10
```

### 學到的重點

部署 Flask 專案到 Render 時，本機能跑不代表雲端一定能跑。雲端環境需要明確列出所有套件與啟動方式。
# Smart Price Tracker - Debug Log

## Debug #1 Flask Route 404 Error

### 問題

新增價格歷史 API 後，瀏覽器存取：

```text
/api/history/Test Book
```

出現：

```text
404 Not Found
```

### 原因

Flask 未載入最新程式碼，實際執行的 app.py 與修改中的檔案不一致。

### 解決方式

加入測試 Route：

```python
@app.route("/test")
def test():
    return "test route OK"
```

並確認：

```python
print("正在執行的 app.py：", __file__)
```

確認 Flask 執行的檔案路徑正確。

### 學習成果

* 學會確認 Flask 實際執行檔案
* 學會排查 Route 未生效問題

---

## Debug #2 SQLite 歷史資料查詢

### 問題

價格走勢圖沒有資料。

### 原因

缺少依商品名稱查詢的 SQL。

### 解決方式

新增：

```python
def get_history_by_name(name):
```

並使用：

```sql
SELECT name, price, time
FROM prices
WHERE name = ?
ORDER BY id ASC
```

### 學習成果

* SQLite 條件查詢
* REST API 資料串接

---

## Debug #3 Chart.js 圖表無法顯示

### 問題

圖表區域出現空白。

### 原因

API 回傳資料格式錯誤。

### 解決方式

建立：

```python
@app.route("/api/history/<path:name>")
```

回傳 JSON：

```python
return jsonify(result)
```

### 學習成果

* Flask API 設計
* JSON 資料交換

---

## Debug #4 Git Branch 衝突

### 問題

執行：

```bash
git push -u origin main
```

出現：

```text
rejected (fetch first)
```

### 原因

本機與 GitHub 的 branch 歷史不同。

### 解決方式

重新整理 branch 結構並完成 merge。

### 學習成果

* Git Branch 管理
* Merge 衝突處理

---

## Debug #5 履歷網站更新失敗

### 問題

GitHub Pages 沒有更新。

### 原因

實際修改的是：

```text
.vscode/index.html
```

GitHub Pages 讀取的是：

```text
index.html
```

### 解決方式

刪除重複檔案。

只保留：

```text
resume-website/index.html
```

### 學習成果

* GitHub Pages 部署流程
* 專案目錄管理

---

## Debug #6 Render 部署失敗

### 問題

Render 顯示：

```text
Not Found
```

### 原因

最新 Commit 尚未部署。

### 解決方式

執行：

```bash
git add .
git commit -m "Update"
git push
```

並重新 Deploy。

### 學習成果

* Render 自動部署流程
* GitHub 與 Render 整合

---

## Debug #7 Python SyntaxError

### 問題

出現：

```text
SyntaxError: invalid syntax
```

### 原因

Dictionary 缺少逗號。

錯誤：

```python
"url": data["url"]
"target": data["target"]
```

正確：

```python
"url": data["url"],
"target": data["target"]
```

### 學習成果

* Python Dict 語法
* Debug 技巧

---

## Debug #8 Gmail App Password

### 問題

Email 無法寄送。

### 原因

使用 Gmail 登入密碼而非 App Password。

### 解決方式

開啟 Google 兩步驟驗證。

建立：

```text
App Password
```

並使用：

```env
EMAIL_PASS=xxxxxxxxxxxxxxxx
```

### 學習成果

* SMTP 郵件發送
* 環境變數管理

---

## Debug #9 Email 重複寄送

### 問題

每次重新整理首頁都寄送 Email。

### 原因

達標判斷每次都觸發。

### 解決方式

新增：

```json
"notified": true
```

並加入：

```python
if not p.get("notified", False):
```

### 學習成果

* 狀態管理
* 防重複通知設計

---

## Debug #10 products.json 格式錯誤

### 問題

出現：

```text
JSONDecodeError
```

### 原因

JSON 缺少逗號。

### 解決方式

修正格式：

```json
{
  "target": "60",
  "notified": false
}
```

### 學習成果

* JSON 格式驗證
* 資料序列化概念

---

## Debug #11 多商品圖表切換

### 問題

切換商品後圖表重疊。

### 原因

Chart.js 持續建立新實例。

### 解決方式

加入：

```javascript
if (priceChart) {
    priceChart.destroy();
}
```

### 學習成果

* JavaScript 物件生命週期
* Chart.js 管理技巧

---

## 專案最終技術

* Python
* Flask
* SQLite
* JSON
* Chart.js
* Gmail SMTP
* Git/GitHub
* Render
* Windows Task Scheduler
* REST API
* Web Scraping
