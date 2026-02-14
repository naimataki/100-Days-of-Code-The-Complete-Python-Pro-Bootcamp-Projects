import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

api_key = os.getenv("API_KEY")
app_id = os.getenv("APP_ID")

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

request_body = {
    "query": input("Tell me which exercices you did: ")
}

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

response = requests.post(url=nutrition_endpoint, json=request_body, headers=headers)
#print(response.text)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

auth_headers = {
    "Authorization": os.getenv("AUTH")
}

sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=auth_headers)
print(sheet_response.text)

