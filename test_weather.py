import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenWeatherMap API configuration
WEATHER_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
WEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

print(f"API Key: {WEATHER_API_KEY}")

# Test coordinates for Paris
lat = 48.8566
lon = 2.3522

params = {
    'lat': lat,
    'lon': lon,
    'appid': WEATHER_API_KEY,
    'units': 'metric'
}

try:
    print(f"Making request to {WEATHER_BASE_URL} with params: {params}")
    response = requests.get(WEATHER_BASE_URL, params=params)
    print(f"Response status code: {response.status_code}")
    
    if response.status_code == 200:
        weather_data = response.json()
        print("Weather data received:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Icon: {weather_data['weather'][0]['icon']}")
    else:
        print(f"Error response: {response.text}")
except Exception as e:
    print(f"Exception occurred: {str(e)}") 