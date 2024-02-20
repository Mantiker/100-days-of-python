import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

votes = [int(score.get_text().split()[0]) for score in soup.select("span.score")]

combined_news = soup.select("tr.athing span.titleline")
news = []
for idx, c_news in enumerate(combined_news):
    new_item = c_news.find(name="a")
    if new_item.get("href").startswith("http"):
        news.append({
            "title": new_item.get_text(),
            "link": new_item.get("href"),
            "score": votes[idx]
        })


sorted_news = sorted(news, key=lambda x: x["score"], reverse=True)

for idx, item in enumerate(sorted_news):
    print(item["title"])
    print(item["link"])
    print(item["score"])
