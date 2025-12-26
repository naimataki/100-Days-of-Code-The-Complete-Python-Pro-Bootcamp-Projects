import smtplib
#
my_email = "naimatakiouti24@gmail.com"
password = "zdw f oomn wsl l zamz"
#
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(
#        from_addr=my_email, 
#        to_addrs="takioutinaima10@gmail.com", 
#        msg="Subject:Hello\n\nThis is the body of my email.")
##connection.close()

import datetime as dt
import random
#
#now = dt.datetime.now() #actual time rn
#year = now.year
#print(type(year))
#print(now) #type: datetime object
#if year == 2025:
#    print("We host the Afcon in Morocco")
#month = now.month
#day_of_week = now.weekday()
#print(day_of_week)
#
#birthday = dt.datetime(year=2001, month=3, day=23, hour=6)
#print(birthday)

now = dt.datetime.now()

day_of_week = now.weekday()

if day_of_week == 4:
    with open("Birthday Wisher/quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        print(quote.strip())
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="takioutinaima10@gmail.com", 
                msg=f"Subject:Monday Motivation\n\n{quote.strip()}"
                )


