import requests 

#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()
#
#data = response.json()
#
#longitude = data["iss_position"]["longitude"]
#latitude = data["iss_position"]["latitude"]
#
#iss_position = (longitude, latitude)
#
#print(iss_position)

parameters = {
    "lat": 30.33417,
    "lng": -9.49722
}

response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status()