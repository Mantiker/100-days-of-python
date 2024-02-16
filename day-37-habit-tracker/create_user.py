import os
import dotenv
import requests

dotenv.load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

PIXELA_ENDPOINT = "https://pixe.la/v1"
CREATE_USER_ENDPOINT = "users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=f"{PIXELA_ENDPOINT}/{CREATE_USER_ENDPOINT}", json=user_params)
print(response)
print(response.text)