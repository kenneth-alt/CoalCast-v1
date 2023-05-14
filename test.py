import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENCAGE_API_KEY = os.getenv('OPENCAGE_API_KEY')
CITY = 'calgary'

url = f'https://api.opencagedata.com/geocode/v1/json?q={CITY}&key={OPENCAGE_API_KEY}'
response = requests.get(url)
data = response.json()


lat = data['results'][0]['geometry']['lat']
lng = data['results'][0]['geometry']['lng']

print(response.status_code)
print(lat, lng)
