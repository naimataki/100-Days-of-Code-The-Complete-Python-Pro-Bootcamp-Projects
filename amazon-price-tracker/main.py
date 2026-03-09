import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import smtplib

load_dotenv()

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['password']
SMTP_ADDRESS = os.environ['SMTP_ADDRESS']
BUY_PRICE = 100
url = "https://appbrewery.github.io/instant_pot/"

headers= {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en,en-US;q=0.9,en-GB;q=0.8", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0", 
  }

response = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "html.parser")

whole_price = soup.find(name="span" ,class_="a-price-whole").getText()
fraction_price = soup.find(name="span" ,class_="a-price-fraction").getText()
price = float(f"{whole_price}{fraction_price}")
product_title = soup.find(id="productTitle").get_text().strip()

print(price)

if price < BUY_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL, 
                    to_addrs="takioutinaima10@gmail.com", 
                    msg=f"Subject:Amazon Price Alert!\n\n{product_title} now in {price}!\n{url}".encode("utf-8"))