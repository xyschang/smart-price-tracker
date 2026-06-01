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
