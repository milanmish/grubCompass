import serial
import requests
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
#BAUD = 9600
#PORT = 

def get_nearby_restaurants(lat, lon):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lon}",
        "radius": 2000,
        "type": "restaurant",
        "open_now": True,
        "key": api_key
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])

print(get_nearby_restaurants(44.963735, -93.308424))