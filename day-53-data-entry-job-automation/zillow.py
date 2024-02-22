import requests
from bs4 import BeautifulSoup

def get_rent_list(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    rent_list = []
    bs = BeautifulSoup(response.text, "html.parser")
    cards = bs.select(selector=".property-card-data")

    for element in cards:
        a_elem = element.find(name="a")
        price_elem = element.find(name="span", attrs={"data-test": "property-card-price"})

        rent_list.append({
            "address": a_elem.get_text(separator=" ", strip=True),
            "price": clear_price(price_elem.get_text()),
            "url": a_elem.get("href"),
        })

    return rent_list

def clear_price(raw_price: str) -> int:
    price = "".join(raw_price.split(" ")[0].removesuffix("/mo").removesuffix("+").removeprefix("$").split(","))

    return int(price)
