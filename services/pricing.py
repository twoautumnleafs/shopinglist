import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from utils.units import BASE_PRICES, units
_prices_cache = {}

def get_base_price(product):
    return BASE_PRICES.get(product)

def get_price_from_tesco(product):
    if product in _prices_cache:
        return _prices_cache[product]

    try:
        query = quote(product)
        url = f"https://www.tesco.sk/groceries/en-GB/search?query={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=0.5)
        soup = BeautifulSoup(resp.text, "html.parser")
        price = soup.select_one(".value")
        if not price:
            return None
        price_num = float(price.text.replace("€", "").replace(",", "."))
        _prices_cache[product] = price_num
        return price_num
    except Exception:
        _prices_cache[product] = None
        return None

def calculate_total(prices_real):
    return sum(price for price, _, _ in prices_real.values())

def get_unit(product_name):
    for unit, products in units.items():
        if product_name in products:
            return unit
    return "unit"