****Smart Price Tracker 商品價格監控系統****
**專案介紹**

Smart Price Tracker 是一套使用 Python Flask 開發的商品價格監控系統，能夠自動追蹤商品價格、記錄歷史價格、分析價格變動、顯示價格走勢圖，並在商品價格達到目標價格時自動寄送 Email 通知。

本專案從需求分析、系統設計、資料庫規劃、功能開發、除錯、版本控制到雲端部署皆由本人獨立完成。

**線上展示Demo**

https://smart-price-tracker-cbke.onrender.com

**GitHub**

https://github.com/xyschang/smart-price-tracker

**功能特色**

**商品管理**

新增商品
刪除商品
多商品追蹤
商品搜尋
商品排序
設定目標價格
**價格監控**

自動擷取商品價格
即時顯示價格資訊
達標價格判斷
價格變動分析
價格漲跌顯示
**歷史紀錄**

SQLite 儲存價格資料
歷史價格查詢
Chart.js 價格走勢圖
多商品圖表切換
**通知功能**

Gmail SMTP Email 通知
達標價格自動寄送通知
防重複通知機制
**自動化**

Windows 工作排程器
每日自動執行價格檢查
雲端部署
Render 雲端部署
GitHub 自動同步更新
**使用技術**

**後端**

Python
Flask
資料庫
SQLite
前端
HTML
CSS
Bootstrap
JavaScript
Chart.js
**資料擷取**

Requests
BeautifulSoup
**通知系統**

Gmail SMTP
Python Dotenv
**版本控制**

Git
GitHub
雲端平台
Render
**已實作功能**

**基礎系統**

Flask Web Application
SQLite Database
REST API
Bootstrap Dashboard
**商品價格追蹤**

BooksToScrape 商品追蹤
PChome 商品追蹤
多商品管理
價格歷史紀錄
**視覺化分析**

Chart.js 折線圖
多商品圖表切換
價格漲跌分析
商品搜尋與排序
**通知與自動化**

Gmail 自動通知
達標價格提醒
防重複寄送機制
Windows Task Scheduler
**部署與維護**

GitHub 版本控制
Render 雲端部署
環境變數管理
Debug Log 管理
**專案架構**

smart-price-tracker
│

├── app.py
├── scraper.py
├── db.py
├── notifier.py
├── scheduler.py
├── products.json
├── requirements.txt
├── runtime.txt
├── .env
├── DEBUG_LOG.md
│
├── templates
│   └── index.html
│
└── data
    └── prices.db
**開發過程中解決的問題**

Flask Route 與 API 錯誤排查
SQLite 歷史資料查詢設計
Chart.js 圖表資料串接
Git Branch 合併衝突處理
GitHub Pages 更新問題排除
Render 部署錯誤排查
Gmail App Password 設定
JSON 格式錯誤修復
Email 重複通知問題解決
Jinja Template 錯誤修正
多商品圖表切換功能實作
PChome 商品價格擷取實作
NoneType 與資料驗證問題排除

詳細內容請參考：

DEBUG_LOG.md

**專案成果**

透過本專案學習並實作：

Flask Web 開發
REST API 設計
SQLite 資料庫操作
Web Scraping
Chart.js 資料視覺化
SMTP 郵件通知
Git / GitHub 版本控制
Render 雲端部署
Windows 工作排程自動化
問題分析與 Debug 能力
完整專案開發流程
未來規劃
支援 momo 商品追蹤
支援蝦皮商品追蹤
LINE 通知
Telegram Bot 通知
使用者登入系統
Docker 容器化部署
PostgreSQL 資料庫
雲端排程服務
管理者後台
商品分類管理
價格異常分析