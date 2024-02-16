import os
import dotenv
import requests

dotenv.load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

PIXELA_GRAPH_ID ="graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1"
CREATE_GRAPH_ENDPOINT = f"users/{PIXELA_USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_config = {
    "id": PIXELA_GRAPH_ID,
    "name": "Studying graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu",  # green
}

response = requests.post(url=f"{PIXELA_ENDPOINT}/{CREATE_GRAPH_ENDPOINT}", headers=headers, json=graph_config)
print(response)
print(response.text)