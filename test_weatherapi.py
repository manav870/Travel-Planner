import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# WeatherAPI configuration
WEATHERAPI_KEY = os.getenv('WEATHERAPI_KEY')
WEATHERAPI_BASE_URL = 'http://api.weatherapi.com/v1/current.json'

print(f"WeatherAPI Key: {WEATHERAPI_KEY}")

# Test coordinates for Paris
lat = 48.8566
lon = 2.3522

params = {
    'key': WEATHERAPI_KEY,
    'q': f"{lat},{lon}",
    'aqi': 'no'
}

try:
    print(f"Making request to {WEATHERAPI_BASE_URL} with params: {params}")
    response = requests.get(WEATHERAPI_BASE_URL, params=params)
    print(f"Response status code: {response.status_code}")
    
    if response.status_code == 200:
        weather_data = response.json()
        print("Weather data received:")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Description: {weather_data['current']['condition']['text']}")
        print(f"Icon URL: {weather_data['current']['condition']['icon']}")
    else:
        print(f"Error response: {response.text}")
except Exception as e:
    print(f"Exception occurred: {str(e)}") 