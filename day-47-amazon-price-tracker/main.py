import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# -------------------------  get config values from env file  -------------------------

load_dotenv()

SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PROTOCOL = int(os.getenv('SMTP_PROTOCOL'))
SMTP_EMAIL = os.getenv('SMTP_EMAIL')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

# -------------------------  parse product price  -------------------------

URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
BUY_PRICE = 50

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.select_one("#productTitle").get_text().strip()
price = float(soup.select_one("#corePriceDisplay_desktop_feature_div .aok-offscreen").get_text().strip()[1:])

# -------------------------  send email  -------------------------

if price < BUY_PRICE:
    sender_smtp_username = SMTP_EMAIL
    sender_smtp_password = SMTP_PASSWORD

    to_email = sender_smtp_username

    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PROTOCOL) as connection:
        connection.starttls()
        connection.login(user=sender_smtp_username, password=sender_smtp_password)
        connection.sendmail(
            from_addr=sender_smtp_username,
            to_addrs=sender_smtp_username,
            msg=f"Subject:Amazon Price Alert!\n\n{title} is now ${price}\n{URL}",
        )
