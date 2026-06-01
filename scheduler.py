import time
from app import load_products
from scraper import get_price
from db import save

def run_scheduler():
    while True:
        print("🔄 更新價格中...")

        products = load_products()

        for p in products:
            price = get_price(p["url"])

            if price:
                save(p["name"], price)
                print(f"✔ {p['name']} = {price}")

        time.sleep(300)  # 5分鐘更新一次

檢查價格

if current_price <= target_price:

    send_mail()