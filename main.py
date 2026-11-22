# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def send_email(content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{content}")

letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]
today = dt.datetime.now().date()

#read csv
df = pd.read_csv("birthdays.csv")
data = df.to_dict(orient="records")

#check birthday
for item in data:
    bday = dt.datetime(item["year"], item["month"], item["day"]).date()
    if bday.month == today.month and bday.day == today.day:
        name = item["name"]
        email = item["email"]

        #random letter
        letter = random.choice(letters)

        with open(f"letter_templates\\{letter}", "r") as f:
            content = f.read()
            content = content.replace("[NAME]", name)
        print(content)

        #send email
        send_email(content)
