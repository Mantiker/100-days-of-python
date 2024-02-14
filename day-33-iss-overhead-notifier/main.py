from datetime import datetime
import requests

MY_LAT = 48.464718
MY_LNG = 35.046185

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "tzid": "Europe/Kyiv",
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = datetime.fromisoformat(data["results"]["sunrise"])
    sunset = datetime.fromisoformat(data["results"]["sunset"])

    time_now = datetime.now()

    if time_now.hour >= sunset.hour or time_now.hour <= sunrise.hour:
        return True # dark

if is_iss_overhead() and is_night():
    print("check iss in the sky")