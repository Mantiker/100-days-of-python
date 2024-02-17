import os
import dotenv
import requests

dotenv.load_dotenv()

BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

SHEETY_ENDPOINT = "https://api.sheety.co/67f97c5a9fea0be0f8ba7bbf3efaeec1/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = self.get_rows()

    def get_rows(self):
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        response.raise_for_status()

        return response.json()["prices"]

    def update_row(self, id, item):
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
        body = {
            "price": {
                "id": item["id"],
                "city": item["city"],
                "iataCode": item["iataCode"],
                "lowestPrice": item["lowestPrice"],
            }
        }

        response = requests.put(url=f"{SHEETY_ENDPOINT}/{id}", headers=headers, json=body)
        response.raise_for_status()

        for idx, item in self.destination_data:
            if item["id"] == id:
                self.destination_data[idx] = {
                    "id": item["id"],
                    "city": item["city"],
                    "iataCode": item["iataCode"],
                    "lowestPrice": item["lowestPrice"],
                }
