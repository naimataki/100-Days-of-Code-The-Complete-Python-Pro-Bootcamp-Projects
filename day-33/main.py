import requests 
from datetime import datetime
import smtplib
import time

MY_LAT = 30.33417
MY_LONG = -9.49722
MY_EMAIL = "naimatakiouti24@gmail.com"
MY_PASSWORD = "zdw f oomn wsl l zamz"

def am_i_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    #iss_position = (longitude, latitude)
    #print(iss_position)
    return (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5)

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #print(sunrise)
    #print(sunset)

    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour <= sunrise

#print(time_now.hour)

while True:
    time.sleep(60)
    if am_i_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs="takioutinaima10@gmail.com", 
                                msg=f"Subject:Look up!\n\nDon't miss the ISS! It's right above you!")

