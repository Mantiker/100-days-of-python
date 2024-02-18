import datetime
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
        headers = {
            "apikey": API_KEY,
        }

        today = datetime.datetime.now()
        date_from = today + datetime.timedelta(days=1)
        date_to = today + datetime.timedelta(days=180)

        params = {
            "fly_from": f"airport:{flight_data.departure_airport_code}",
            "fly_to": f"airport:{flight_data.destination_airport_code}",
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "return_from": date_from.strftime("%d/%m/%Y"),
            "return_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "curr": "EUR",
            "max_stopovers": 0,
            "limit": 1,
        }

        resp = requests.get(url=f"{URL}/v2/search", headers=headers, params=params)
        resp.raise_for_status()

        resp_data = resp.json()["data"]

        if len(resp_data) > 0:
            flight_data.price = resp_data[0]["price"]
            flight_data.departure_date = datetime.datetime.fromisoformat(resp_data[0]["local_departure"])
            flight_data.destination_date = datetime.datetime.fromisoformat(resp_data[0]["local_arrival"]) + datetime.timedelta(days=int(resp_data[0]["nightsInDest"]))
