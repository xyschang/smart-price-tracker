# 📊 Smart Price Tracker 商品價格監控系統

> 使用 Flask 開發的商品價格監控平台，支援價格追蹤、歷史紀錄、圖表分析、Email 通知與每日自動檢查。

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Chart.js](https://img.shields.io/badge/Chart.js-Visualization-orange)
![Render](https://img.shields.io/badge/Deploy-Render-purple)

---

## 🔗 Demo

🌐 **線上展示：**  
https://smart-price-tracker-cbke.onrender.com

📁 **GitHub：**  
https://github.com/xyschang/smart-price-tracker

---

## ✨ 專案特色

| 功能 | 說明 |
|---|---|
| 商品管理 | 新增、刪除、多商品追蹤 |
| 價格監控 | 自動擷取商品價格並判斷是否達標 |
| 歷史紀錄 | 使用 SQLite 儲存價格變化 |
| 圖表分析 | 使用 Chart.js 顯示價格走勢 |
| 商品搜尋 | 可快速搜尋指定商品 |
| 表格排序 | 商品名稱、價格、目標價格可排序 |
| Email 通知 | 價格達標時自動寄送 Gmail 通知 |
| 防重複通知 | 已通知商品不會重複寄信 |
| 自動排程 | 使用 Windows Task Scheduler 每日自動檢查 |
| 雲端部署 | 使用 Render 部署 Flask Web App |

---

## 🛠 使用技術

| 類別 | 技術 |
|---|---|
| 後端 | Python、Flask |
| 資料庫 | SQLite |
| 前端 | HTML、CSS、Bootstrap、JavaScript |
| 視覺化 | Chart.js |
| 爬蟲 | Requests、BeautifulSoup |
| 通知 | Gmail SMTP、python-dotenv |
| 版本控制 | Git、GitHub |
| 部署 | Render |
| 自動化 | Windows Task Scheduler |

---

## 📌 已完成功能

- ✅ 商品新增與刪除
- ✅ 多商品價格追蹤
- ✅ 目標價格設定
- ✅ 已達標 / 未達標判斷
- ✅ Gmail Email 通知
- ✅ 防重複通知機制
- ✅ SQLite 歷史價格紀錄
- ✅ Chart.js 價格走勢圖
- ✅ 多商品圖表切換
- ✅ 商品搜尋與排序
- ✅ 價格漲跌顯示
- ✅ Render 雲端部署
- ✅ 每日自動排程檢查

---

## 📂 專案架構

```text
smart-price-tracker/
│
├── app.py                 # Flask 主程式
├── scraper.py             # 商品價格擷取
├── db.py                  # SQLite 資料庫操作
├── notifier.py            # Gmail Email 通知
├── scheduler.py           # 每日排程檢查
├── products.json          # 商品設定資料
├── requirements.txt       # Python 套件
├── runtime.txt            # Render Python 版本
├── DEBUG_LOG.md           # Debug 紀錄
│
├── templates/
│   └── index.html         # 前端頁面
│
└── data/
    └── prices.db          # SQLite 資料庫