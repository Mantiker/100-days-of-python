#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
flight_search = FlightSearch()

for item in data_manager.destination_data:
    if item["iataCode"] == "":
        item["iataCode"] = flight_search.get_iata_code(item["city"])
        data_manager.update_row(item["id"], item)

pprint(data_manager.destination_data, width=120)

for item in data_manager.destination_data:
    flight_data = FlightData()
    flight_data.destination_city = item["city"]
    flight_data.destination_airport_code = item["iataCode"]

    data = flight_search.search(flight_data)

    flight_data.price = 0

