import requests
from datetime import datetime

USERNAME = "naima101"
TOKEN = "12werfghyu9076trd"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Learning Graph",
    "unit": "min",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{graph_endpoint}/{ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "100"
}

update_pixel_endpoint = f"{graph_endpoint}/{ID}/{today.strftime("%Y%m%d")}"
update_pixel_config = {
    "quantity": input("How many minutes did you study today? ")
}

#response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
