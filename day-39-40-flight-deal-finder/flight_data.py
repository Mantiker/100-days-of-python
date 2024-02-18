import math

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, destination_airport_code, destination_city):
        self.price = math.inf
        self.currency = "EUR"
        self.departure_airport_code = "WAW"
        self.departure_city = "Warsaw"
        self.departure_date = None
        self.destination_airport_code = destination_airport_code
        self.destination_city = destination_city
        self.destination_date = None
