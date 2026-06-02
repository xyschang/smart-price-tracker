import requests
from bs4 import BeautifulSoup
import re


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_price(url):
    if "books.toscrape.com" in url:
        return get_books_price(url)

    if "24h.pchome.com.tw" in url:
        return get_pchome_price(url)

    print("目前不支援這個網站")
    return None


def get_books_price(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")

        tag = soup.select_one(".price_color")

        if tag:
            return extract_price(tag.text)

        return None

    except Exception as e:
        print("books scraper error:", e)
        return None


def get_pchome_price(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text()

        m = re.search(r'\$([\d,]+)', text)

        if m:
            return int(m.group(1).replace(",", ""))
        return None

    except Exception as e:
        print("pchome scraper error:", e)
        return None


def extract_price(text):
    match = re.search(r'\d[\d,]*', text)

    if match:
        return int(match.group().replace(",", ""))

    return None