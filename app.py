from notifier import send_email
from flask import Flask, render_template, request, jsonify
from scraper import get_price
from db import init_db, save, get_all, get_history_by_name
import json
import os
print("正在執行的 app.py：", __file__)

app = Flask(__name__)

init_db()

PRODUCT_FILE = "products.json"


# =====================
# 工具
# =====================
def load_products():
    if not os.path.exists(PRODUCT_FILE):
        return []
    with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_products(data):
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# =====================
# 首頁
# =====================
@app.route("/")
def index():
    products = load_products()
    results = []

    for p in products:
        print(p)
        price = get_price(p["url"])
        target = int(p.get("target")or 0)

        if price:
            save(p["name"], price)
        if price and target > 0:
            if price <= target and not p.get("notified", False):

                send_email(
                f"{p['name']} 已達標",
                f"""
                商品：{p['name']}
                目前價格：{price}
                目標價格：{target}
                """
                )

                p["notified"] = True
                save_products(products)
                print("已寫入 products.json")

        results.append({
            "name": p["name"],
            "price": price,
            "target": p.get("target", "")
        })

    history = get_all()

    return render_template("index.html",
                           products=results,
                           history=history)


# =====================
# 新增商品
# =====================
@app.route("/add", methods=["POST"])
def add():
    data = request.json
    products = load_products()

    products.append({
        "name": data["name"],
        "url": data["url"],
        "target": data.get("target")or "0",
        "notified": False
    })

    save_products(products)

    return jsonify({"status": "ok"})


# =====================
# 刪除商品（V2新增）
# =====================
@app.route("/delete", methods=["POST"])
def delete():
    name = request.json["name"]
    products = load_products()

    products = [p for p in products if p["name"] != name]
    

    return jsonify({"status": "deleted"})

# =====================
# 價格歷史 API
# =====================
@app.route("/test")
def test():
    return "test route OK"
@app.route("/api/history/<path:name>")
def api_history(name):
    history = get_history_by_name(name)

    result = []

    for h in history:
        result.append({
            "name": h[0],
            "price": h[1],
            "time": h[2]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
