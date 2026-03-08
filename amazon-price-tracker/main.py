import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import smtplib

load_dotenv()

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['password']
SMTP_ADDRESS = os.environ['SMTP_ADDRESS']

response = requests.get("https://appbrewery.github.io/instant_pot/")
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "html.parser")

whole_price = soup.find(name="span" ,class_="a-price-whole").getText()
fraction_price = soup.find(name="span" ,class_="a-price-fraction").getText()
price = float(f"{whole_price}{fraction_price}")

print(price)

with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL, 
                to_addrs="takioutinaima10@gmail.com", 
                msg=f"Subject:Amazon Price Alert!\n\nInstant Pot Duo Plus 9-in-1 Electric Pressure Cooker"
                )