import os
import dotenv
import requests
from datetime import datetime

dotenv.load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

PIXELA_GRAPH_ID ="graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1"
POST_DATA_GRAPH_ENDPOINT = f"users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

today = datetime.now()

graph_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "45",
}

response = requests.post(url=f"{PIXELA_ENDPOINT}/{POST_DATA_GRAPH_ENDPOINT}", headers=headers, json=graph_data)
print(response)
print(response.text)