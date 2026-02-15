import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["AMADEUS_API_KEY"]
API_SECRET = os.environ["AMADEUS_API_SECRET"]

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = API_KEY
        self._api_secret = API_SECRET
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        params = {
            "keyword": city_name
        }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities")
        #code = "TESTING"
        #return code
    
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': API_SECRET
        }
        response = requests.post(
                                url="https://test.api.amadeus.com/v1/security/oauth2/token", 
                                headers=header, 
                                data=body)
        data = response.json()
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return data["access_token"]