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
    flight_data = FlightData(destination_airport_code=item["iataCode"], destination_city=item["city"])

    flight_search.search(flight_data)

    print(f"{flight_data.destination_city}: €{flight_data.price}")

    if flight_data.price < int(item["lowestPrice"]):
        print(f"Low price alert!Only €{flight_data.price} to fly from {flight_data.departure_city}-{flight_data.departure_airport_code}"
              f" to {flight_data.destination_city}-{flight_data.destination_airport_code},"
              f" from {flight_data.departure_date.strftime('%Y-%m-%d')} to {flight_data.destination_date.strftime('%Y-%m-%d')}")

