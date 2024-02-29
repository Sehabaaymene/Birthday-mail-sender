from datetime import datetime
import pandas
import smtplib
import random

# Your information.
MY_EMAIL = "Putyouremail@example.com"
PASSWORD = "yourpassword"

# To get today's month and day.
today = datetime.now()
today_tuple = (today.month, today.day)

# Reading the csv file and converting it to a dictionary.
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# Checking if someone's birthday today.
if today_tuple in birthday_dict:

    # Get hold of the birthday person dict.
    birthday_person = birthday_dict[today_tuple]

    # Going through the letters and choosing one randomly.
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # Going through the letter chosen and putting the birthday person name using replace().
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Steps to take to send an automated email.
    # "smtp.gmail.com" works only with gmail accounts, every other social has its own smtp login type.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject HAPPY BIRTHDAY\n\n{contents}"
                            )
