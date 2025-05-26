import serial
import requests
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
baud = 9600
port = serial.Serial('/dev/ttyUSB0', baud, timeout=1)

def getCurrentLocation():
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    payload = {
        "considerIp": True
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        lat = data["location"]["lat"]
        lon = data["location"]["lng"]
        accuracy = data["accuracy"]
        print(f"Location: ({lat}, {lon}) with ±{accuracy} meters accuracy")
        return lat, lon
    
    else:
        print("Failed to get location:", response.status_code, response.text)
        return None, None

def getNearbyRestaurants(lat, lon):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lon}",
        "radius": 2000,
        "type": "restaurant",
        "open_now": True,
        "key": api_key
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])

lat, lon = getCurrentLocation()

nearbyGrub = getNearbyRestaurants(lat, lon)

randomGrub = random.choice(nearbyGrub)

location = randomGrub["geometry"]["location"]
grubLat = location["lat"]
grubLon = location["lng"]

# now I need to find a way to send this to the ESP32

message = f"{grubLat},{grubLon}\n"
port.write(message.encode())