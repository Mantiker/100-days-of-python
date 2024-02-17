import os
import dotenv
import requests
from flight_data import FlightData

dotenv.load_dotenv()

API_KEY = os.getenv("TEQUILA_API_KEY")
IATA_CODE_FROM = os.getenv("IATA_CODE_FROM")

URL = "https://api.tequila.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    def get_iata_code(self, city: str):
        headers = {
            "apikey": API_KEY,
        }

        params = {
            "term": city,
            "location_types": "airport",
            "limit": 3,
        }

        response = requests.get(url=f"{URL}/locations/query", headers=headers, params=params)
        response.raise_for_status()

        return response.json()["locations"][0]["id"]

    def search(self, flight_data: FlightData):
        pass