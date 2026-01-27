import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
stock_apikey =os.getenv("STOCK_API_KEY")
news_apikey = os.getenv("NEWS_API_KEY")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_apikey
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
#print(response.json())

stock_data = stock_response.json()
#print(stock_data["Time Series (Daily)"]["2026-01-22"]["4. close"])

closing_prices = [
    float(value["4. close"])
    for (key, value) in stock_data["Time Series (Daily)"].items()
]

yesterday_closing = closing_prices[0]

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_closing = closing_prices[1]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

positive_difference = abs(yesterday_closing - day_before_yesterday_closing)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_difference = (positive_difference / yesterday_closing) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_params = {
    "apiKey": news_apikey,
    "q": COMPANY_NAME,
    "language": "en"
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
#print(response.json())
news_data = news_response.json()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

first_articles = news_data["articles"][:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

first_articles_simple = [
    (article["title"], article["description"])
    for article in first_articles
]

print(first_articles_simple)

#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(account_sid, auth_token)
message = client.messages.create(
    from_="whatsapp:",
    body=f"{STOCK_NAME}: {percentage_difference}%",
    to="whatsapp:"
)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

