
# -------------------------  get config values from env file  -------------------------

# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# SMTP_HOST = os.getenv('SMTP_HOST')
# SMTP_PROTOCOL = os.getenv('SMTP_PROTOCOL')
# SMTP_EMAIL = os.getenv('SMTP_EMAIL')
# SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
#
# print(SMTP_HOST)
# print(SMTP_PROTOCOL)
# print(SMTP_EMAIL)
# print(SMTP_PASSWORD)


# -------------------------  send email  -------------------------

# import smtplib
# sender_smtp_username = SMTP_EMAIL
# sender_smtp_password = SMTP_PASSWORD
#
# to_email = sender_smtp_username
#
# with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PROTOCOL) as connection:
#     connection.starttls()
#     connection.login(user=sender_smtp_username, password=sender_smtp_password)
#     connection.sendmail(from_addr=sender_smtp_username, to_addrs=sender_smtp_username, msg="Subject:Hello\n\nHi there!")


# -------------------------  datetime  -------------------------

import datetime as dt

now = dt.datetime.now()

print(now)
print(now.year)
print(now.minute)

date = dt.datetime(year=2000, month=12, day=23)
print(date)
