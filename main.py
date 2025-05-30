import requests
import random
import os
from gpiozero import Button
from signal import pause
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

button = Button(17, pull_up=True, bounce_time=0.1)

def getCurrentLocation():
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    payload = {"considerIp": True}
    headers = {"Content-Type": "application/json"}

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

def findGrub():
    lat, lon = getCurrentLocation()
    if lat is None or lon is None:
        print("Could not get location, try again.")
        return

    nearbyGrub = getNearbyRestaurants(lat, lon)

    if not nearbyGrub:
        print("No restaurants found nearby!")
        return

    randomGrub = random.choice(nearbyGrub)
    location = randomGrub["geometry"]["location"]
    grubLat = location["lat"]
    grubLon = location["lng"]
    name = randomGrub.get("name", "Unknown")
    address = randomGrub.get("vicinity", "No address")
    print(f"Random nearby restaurant: {name} at {address} ({grubLat}, {grubLon})")

button.when_pressed = findGrub

print("Waiting for button press...")
pause()