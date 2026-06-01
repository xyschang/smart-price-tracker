import json
from scraper import get_price
from notifier import send_email


PRODUCT_FILE = "products.json"


def load_products():
    with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_products(products):
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


def check_prices():
    products = load_products()

    for p in products:
        price = get_price(p["url"])
        target = int(p.get("target", 0))

        print(f"檢查商品：{p['name']}")
        print(f"目前價格：{price}")
        print(f"目標價格：{target}")

        if price and target > 0:
            if price <= target and not p.get("notified", False):
                send_email(
                    f"{p['name']} 價格已達標",
                    f"""
商品：{p['name']}

目前價格：{price}

目標價格：{target}
"""
                )

                p["notified"] = True
                save_products(products)

                print("已寄出通知並更新 notified")

            else:
                print("尚未達標或已通知過")


if __name__ == "__main__":
    check_prices()