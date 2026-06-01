# Smart Price Tracker 商品價格監控系統

## 專案介紹

Smart Price Tracker 是一套使用 Python Flask 開發的商品價格監控系統，能夠自動追蹤商品價格、記錄歷史價格、顯示價格走勢圖，並在商品價格達到目標價格時自動寄送 Email 通知。

本專案從需求分析、系統設計、資料庫規劃、功能開發、除錯到雲端部署皆由本人獨立完成。

---

## 線上展示

Demo：

https://smart-price-tracker-cbke.onrender.com

GitHub：

https://github.com/xyschang/smart-price-tracker

---

## 功能特色

### 商品管理

* 新增商品
* 刪除商品
* 設定目標價格

### 價格監控

* 自動擷取商品價格
* 即時顯示價格資訊
* 達標價格判斷

### 歷史紀錄

* SQLite 儲存價格資料
* 歷史價格查詢
* Chart.js 價格走勢圖

### 通知功能

* Gmail SMTP Email 通知
* 達標價格自動寄送通知
* 防止重複寄送機制

### 自動化

* Windows 工作排程器
* 每日自動執行價格檢查

### 雲端部署

* Render 雲端部署
* GitHub 自動同步更新

---

## 使用技術

### 後端

* Python
* Flask

### 資料庫

* SQLite

### 前端

* HTML
* CSS
* Bootstrap
* JavaScript
* Chart.js

### 資料處理

* Requests
* BeautifulSoup

### 通知系統

* Gmail SMTP
* Python Dotenv

### 版本控制

* Git
* GitHub

### 雲端平台

* Render

---

## 專案架構

```text
smart-price-tracker
│
├── app.py                 Flask 主程式
├── scraper.py             商品價格擷取
├── db.py                  SQLite 操作
├── notifier.py            Email 通知
├── scheduler.py           排程檢查
├── products.json          商品設定
├── requirements.txt
├── runtime.txt
├── DEBUG_LOG.md
│
├── templates
│   └── index.html
│
└── data
    └── prices.db
```

---

## 開發過程中解決的問題

* Flask API 404 錯誤排除
* SQLite 歷史資料查詢設計
* Chart.js 圖表資料串接
* Git Branch 合併衝突處理
* GitHub Pages 更新異常排除
* Render 部署問題排查
* Gmail App Password 設定
* JSON 格式錯誤修復
* Email 重複通知問題解決
* 多商品圖表切換功能實作

詳細內容請參考：

DEBUG_LOG.md

---

## 專案成果

透過本專案學習並實作：

* Flask Web 開發
* REST API 設計
* SQLite 資料庫操作
* Web Scraping
* Chart.js 資料視覺化
* SMTP 郵件通知
* Git/GitHub 版本控制
* Render 雲端部署
* Windows 工作排程自動化
* 專案除錯與維護能力

---

## 未來規劃

* 支援 PChome 商品追蹤
* 支援 momo 商品追蹤
* 支援蝦皮商品追蹤
* LINE Notify 通知
* Telegram Bot 通知
* 使用者登入系統
* Docker 容器化部署
* PostgreSQL 資料庫
* 雲端排程服務
