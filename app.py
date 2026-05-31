from flask import Flask, render_template, request, jsonify
from scraper import get_price
from db import init_db, save, get_all
import json
import os

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
        price = get_price(p["url"])

        if price:
            save(p["name"], price)

        results.append({
            "name": p["name"],
            "price": price
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
        "url": data["url"]
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

    save_products(products)

    return jsonify({"status": "deleted"})


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/api/history/<name>")
def history(name):
    data = get_all()
    result = [d for d in data if d[1] == name]
    return jsonify(result)