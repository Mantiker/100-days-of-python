import datetime as dt
import os
import random
import smtplib
from dotenv import load_dotenv

# -------------------------  get config values from env file  -------------------------

load_dotenv()

SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PROTOCOL = int(os.getenv('SMTP_PROTOCOL'))
SMTP_EMAIL = os.getenv('SMTP_EMAIL')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

print(SMTP_HOST)
print(SMTP_PROTOCOL)
print(SMTP_EMAIL)
print(SMTP_PASSWORD)

# -------------------------  send email  -------------------------

now = dt.datetime.now()
if now.weekday() == 1:
    with open("./quotes.txt", mode="r") as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)

    sender_smtp_username = SMTP_EMAIL
    sender_smtp_password = SMTP_PASSWORD

    to_email = sender_smtp_username

    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PROTOCOL) as connection:
        connection.starttls()
        connection.login(user=sender_smtp_username, password=sender_smtp_password)
        connection.sendmail(
            from_addr=sender_smtp_username,
            to_addrs=sender_smtp_username,
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )

