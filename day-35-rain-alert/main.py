import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_ID = os.getenv('OPEN_WEATHER_API_ID')
CITY = os.getenv('CITY')

# params = {
#     "q": CITY,
#     "appid": OPEN_WEATHER_API_ID,
# }
#
# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=params)
# response.raise_for_status()
#
# print(response.json())

# hourly forcast
params = {
    "q": CITY,
    "appid": OPEN_WEATHER_API_ID,
    "cnt": 4,
    "units": "metric",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

weather_data = response.json()
will_rain = False
print(response.text)

for weather_points in weather_data["list"]:
    for w in weather_points["weather"]:
        if int(w["id"]) < 700:
            will_rain = True

if will_rain:
    print("Bring an umbrella")
    # send sms or mail as in previous tasks