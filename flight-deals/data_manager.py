import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.environ["MY_SHEETY_ENDPOINT"]

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iata"
                }
            }