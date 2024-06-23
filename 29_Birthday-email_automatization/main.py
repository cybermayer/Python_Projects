from datetime import datetime
import pandas
import random
import smtplib

# Constants for email credentials
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# Get the current date and extract the month and day
today = datetime.now()
today_tuple = (today.month, today.day)

# Read the birthdays CSV file into a DataFrame
data = pandas.read_csv("birthdays.csv")

# Create a dictionary with keys as (month, day) tuples and values as the corresponding row data
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today's date matches any birthday in the dictionary
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple] 
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"  
    with open(file_path) as letter_file:
        contents = letter_file.read() 
        contents = contents.replace("[NAME]", birthday_person["name"]) 

    # Send the email using SMTP
    with smtplib.SMTP("smtp.mail.google.com") as connection:
        connection.starttls()  
        connection.login(MY_EMAIL, MY_PASSWORD)  
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{contents}"  
        )
