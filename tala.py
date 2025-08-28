import requests
from bs4 import BeautifulSoup
import json

site = "https://www.tgju.org/profile/geram18"

response = requests.get(site).content
soup = BeautifulSoup(response, "html.parser")

price = soup.find('span', attrs={'data-col': 'info.last_trade.PDrCotVal'}).text

data = {
    "price": price
}

# ذخیره در فایل json
with open('price.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("price.json")
