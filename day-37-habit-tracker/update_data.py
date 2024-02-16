import os
import dotenv
import requests
from datetime import datetime

dotenv.load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

PIXELA_GRAPH_ID ="graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1"
DATA_GRAPH_ENDPOINT = f"users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

date = datetime.now().strftime("%Y%m%d")

graph_data = {
    "quantity": "50",
}

response = requests.put(url=f"{PIXELA_ENDPOINT}/{DATA_GRAPH_ENDPOINT}/{date}", headers=headers, json=graph_data)
print(response)
print(response.text)