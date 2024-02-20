import os
import dotenv
from bs4 import BeautifulSoup
import requests

dotenv.load_dotenv()

BILLBOARD_HOT_100_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_USERNAME = os.getenv("SPOTIPY_USERNAME")

input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(url=f"{BILLBOARD_HOT_100_URL}/{input_date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_elements = soup.select("li.o-chart-results-list__item h3#title-of-a-story")

song_list = [item.get_text().strip() for item in song_elements]

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIPY_USERNAME,
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = input_date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Done")
