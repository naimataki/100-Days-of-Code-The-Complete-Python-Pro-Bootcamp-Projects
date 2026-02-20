import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices_endpoint = os.environ["PRICES_SHEET_ENDPOINT"]
        self.users_endpoint = os.environ["USERS_SHEET_ENDPOINT"]
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint)
        #print(response.text)
        data = response.json()
        #print(data)
        self.destination_data = data['prices']
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.user_data = data['users']
        return self.user_data