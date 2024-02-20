import requests
from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://web.archive.org/web/20240121023101/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

parsed_movies = soup.select(".listicleItem_listicle-item__title__BfenH")
movies = []

for item in parsed_movies:
    text_parts = item.get_text().split(sep=") ")

    movies.append({
        "position": int(text_parts[0]),
        "title": text_parts[1],
    })

sorted_movies = sorted(movies, key=lambda x: x["position"])
sorted_strings = [f"{item['position']}) {item['title']}\n" for item in sorted_movies]

with open("./movies.txt", mode="w") as f:
    f.writelines(sorted_strings)
