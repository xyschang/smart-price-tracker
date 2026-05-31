import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_price(url):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # 1️⃣ 常見 selector
        selectors = [
            ".price",
            ".price_color",
            "[class*='price']",
            "[class*='Price']",
            "[class*='amount']"
        ]

        for sel in selectors:
            tag = soup.select_one(sel)
            if tag:
                price = extract(tag.text)
                if price:
                    return price

        # 2️⃣ fallback（全頁抓數字）
        text = soup.get_text()
        numbers = re.findall(r'\d[\d,]{2,}', text)

        if numbers:
            nums = [int(n.replace(",", "")) for n in numbers]
            return max(nums)

        return None

    except Exception as e:
        print("scraper error:", e)
        return None


def extract(text):
    match = re.search(r'\d[\d,]*', text)
    if match:
        return int(match.group().replace(",", ""))
    return None

