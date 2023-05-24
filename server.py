import os
import requests
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

OPENCAGE_API_KEY = os.getenv('OPENCAGE_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

CITY = "enugu"

# LAT = 6.4402
# LON = 7.4943

app = Flask(__name__)


def get_lat_lon():
    url = f'https://api.opencagedata.com/geocode/v1/json?q={CITY}&key={OPENCAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()

    LAT = data['results'][0]['geometry']['lat']
    LON = data['results'][0]['geometry']['lng']
    
    return LAT, LON
    
def current_weather():
    LAT, LON = get_lat_lon()
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={OPENWEATHER_API_KEY}")
    data = response.json()
    return data
   
@app.route('/')
def index():
    data = current_weather()
    return data

