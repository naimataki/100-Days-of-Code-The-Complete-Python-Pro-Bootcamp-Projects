import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 55.953251,
    "lon": -3.188267,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
        body="It's going to rain today. Remember to bring an umbrella ☔",
        to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
    )

    print(message.status)
