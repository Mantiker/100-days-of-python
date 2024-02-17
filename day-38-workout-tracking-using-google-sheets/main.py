from datetime import datetime
import dotenv
import os
import requests
import requests.auth

dotenv.load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
SHEETY_URL = os.getenv("SHEETY_URL")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

main_url = "https://trackapi.nutritionix.com/v2"
natural_exercise_endpoint = "natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

body = {
    "query": input("Please provide details about completed exercises: ")
}

response = requests.post(f"{main_url}/{natural_exercise_endpoint}", headers=headers, json=body)
response.raise_for_status()
exercises = response.json()["exercises"]

today = datetime.now()

for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    basic_auth = requests.auth.HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)
    resp = requests.post(SHEETY_URL, auth=basic_auth, json=sheety_data)
    print(resp.text)
    resp.raise_for_status()

