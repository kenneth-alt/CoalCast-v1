import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

OPENCAGE_API_KEY = os.getenv('OPENCAGE_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

CITY = "enugu"

# LAT = 6.4402
# LON = 7.4943

app = Flask(__name__)


def get_lat_lon():
    try:
        url = f'https://api.opencagedata.com/geocode/v1/json?q={CITY}&key={OPENCAGE_API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        lat_lon_data = response.json()
        
        LAT = lat_lon_data['results'][0]['geometry']['lat']
        LON = lat_lon_data['results'][0]['geometry']['lng']
        return LAT, LON
    except requests.exceptions.HTTPError as err:
        return f"Error: {err}"

@app.route('/current')    
def current_weather():
    try:
        LAT, LON = get_lat_lon()
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={OPENWEATHER_API_KEY}")
        weather_data = response.json()
        return  weather_data
    except requests.exceptions.HTTPError as err:
        return f"Error: {err}"

@app.route('/forcast')
def forcast():
    try:
        LAT, LON = get_lat_lon()
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={OPENWEATHER_API_KEY}")
        forcast_data = response.json()
        return  forcast_data
    except requests.exceptions.HTTPError as err:
        return f"Error: {err}"
   
@app.route('/')
def index():
    return render_template("index.html")


