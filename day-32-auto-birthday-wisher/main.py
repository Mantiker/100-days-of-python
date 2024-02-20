import datetime as dt
import pandas
import random

letter_templates = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt",
]

data = pandas.read_csv("./birthdays.csv")
data_dict = data.to_dict(orient="records")
birthdays_dict = {}
for v in data_dict:
    birthdays_dict[(v['month'], v['day'])] = v

now = dt.datetime.now()
today_month = now.month
today_day = now.day

if (today_month, today_day) in birthdays_dict:
    birthday_data = birthdays_dict[(today_month, today_day)]

    with open(random.choice(letter_templates), mode="r") as ltf:
        letter_template = ltf.read()

        letter = letter_template.replace("[NAME]", birthday_data["name"])

        print(letter)

    # TODO: send a mail as in quotes_sender.py - next to this file





##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



