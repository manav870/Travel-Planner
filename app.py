from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import os
from datetime import datetime
import requests
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, 
            static_folder='app/static',
            template_folder='app/templates')

app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Weather API configuration
OPENWEATHER_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
WEATHERAPI_KEY = os.getenv('WEATHERAPI_KEY')
WEATHERAPI_BASE_URL = 'http://api.weatherapi.com/v1/current.json'

# Sample data - in a real app, you would use a database
destinations = [
    {
        'id': 1,
        'name': 'Paris',
        'country': 'France',
        'description': 'The City of Light',
        'image': 'paris.jpg',
        'attractions': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
        'suggested_budget': {'min': 1200, 'max': 2000},
        'coordinates': {'lat': 48.8566, 'lon': 2.3522}
    },
    {
        'id': 2,
        'name': 'Tokyo',
        'country': 'Japan',
        'description': 'A blend of traditional and ultramodern',
        'image': 'tokyo.jpg',
        'attractions': ['Tokyo Tower', 'Senso-ji Temple', 'Shibuya Crossing'],
        'suggested_budget': {'min': 1500, 'max': 2500},
        'coordinates': {'lat': 35.6762, 'lon': 139.6503}
    },
    {
        'id': 3,
        'name': 'New York',
        'country': 'USA',
        'description': 'The Big Apple',
        'image': 'newyork.jpg',
        'attractions': ['Statue of Liberty', 'Central Park', 'Empire State Building'],
        'suggested_budget': {'min': 1800, 'max': 3000},
        'coordinates': {'lat': 40.7128, 'lon': -74.0060}
    },
    {
        'id': 4,
        'name': 'Rome',
        'country': 'Italy',
        'description': 'The Eternal City',
        'image': 'rome.jpg',
        'attractions': ['Colosseum', 'Vatican City', 'Trevi Fountain'],
        'suggested_budget': {'min': 1000, 'max': 1800},
        'coordinates': {'lat': 41.9028, 'lon': 12.4964}
    },
    {
        'id': 5,
        'name': 'Bali',
        'country': 'Indonesia',
        'description': 'Island of the Gods',
        'image': 'bali.jpg',
        'attractions': ['Ubud Monkey Forest', 'Tanah Lot Temple', 'Kuta Beach'],
        'suggested_budget': {'min': 800, 'max': 1500},
        'coordinates': {'lat': -8.4095, 'lon': 115.1889}
    },
    {
        'id': 6,
        'name': 'London',
        'country': 'United Kingdom',
        'description': 'The Historic Capital',
        'image': 'london.jpg',
        'attractions': ['Buckingham Palace', 'Big Ben', 'London Eye'],
        'suggested_budget': {'min': 1500, 'max': 2500},
        'coordinates': {'lat': 51.5074, 'lon': -0.1278}
    },
    {
        'id': 7,
        'name': 'Sydney',
        'country': 'Australia',
        'description': 'The Harbour City',
        'image': 'sydney.jpg',
        'attractions': ['Sydney Opera House', 'Bondi Beach', 'Sydney Harbour Bridge'],
        'suggested_budget': {'min': 1600, 'max': 2700},
        'coordinates': {'lat': -33.8688, 'lon': 151.2093}
    }
]

trips = []

@app.route('/')
def home():
    return render_template('index.html', destinations=destinations)

@app.route('/destination/<int:destination_id>')
def destination_detail(destination_id):
    destination = next((d for d in destinations if d['id'] == destination_id), None)
    if destination:
        return render_template('destination.html', destination=destination)
    return redirect(url_for('home'))

@app.route('/plan_trip', methods=['GET', 'POST'])
def plan_trip():
    if request.method == 'POST':
        try:
            # Process the form data
            activities_text = request.form.get('activities', '').strip()
            activities_list = [activity.strip() for activity in activities_text.split(',')] if activities_text else []
            
            # Validate destination
            destination_id = int(request.form.get('destination', 0))
            if not any(d['id'] == destination_id for d in destinations):
                flash('Please select a valid destination.', 'danger')
                return render_template('plan_trip.html', destinations=destinations)
            
            # Validate dates
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            if not start_date or not end_date:
                flash('Please select valid travel dates.', 'danger')
                return render_template('plan_trip.html', destinations=destinations)
            
            # Validate and parse budget
            try:
                budget = float(request.form.get('budget', 0))
                if budget <= 0:
                    flash('Please enter a valid budget amount.', 'danger')
                    return render_template('plan_trip.html', destinations=destinations)
            except ValueError:
                flash('Please enter a valid budget amount.', 'danger')
                return render_template('plan_trip.html', destinations=destinations)
            
            # Create new trip
            new_trip = {
                'id': len(trips) + 1,
                'destination_id': destination_id,
                'start_date': start_date,
                'end_date': end_date,
                'budget': budget,
                'activities': activities_list,
                'created_at': datetime.now()
            }
            trips.append(new_trip)
            flash('Trip planned successfully!', 'success')
            return redirect(url_for('my_trips'))
        except Exception as e:
            flash('An error occurred while planning your trip. Please try again.', 'danger')
            return render_template('plan_trip.html', destinations=destinations)
    
    return render_template('plan_trip.html', destinations=destinations)

@app.route('/my_trips')
def my_trips():
    # Enhance trips with destination information
    enhanced_trips = []
    for trip in trips:
        destination = next((d for d in destinations if d['id'] == trip['destination_id']), None)
        if destination:
            trip_copy = trip.copy()
            trip_copy['destination'] = destination
            enhanced_trips.append(trip_copy)
    
    return render_template('my_trips.html', trips=enhanced_trips)

@app.route('/delete_trip/<int:trip_id>', methods=['POST'])
def delete_trip(trip_id):
    # Find the trip with the given ID and remove it
    trip_index = next((index for index, trip in enumerate(trips) if trip['id'] == trip_id), None)
    
    if trip_index is not None:
        trips.pop(trip_index)
        flash('Trip deleted successfully!', 'success')
    else:
        flash('Trip not found.', 'danger')
    
    return redirect(url_for('my_trips'))

@app.route('/api/weather/<int:destination_id>')
def get_weather(destination_id):
    try:
        destination = next((d for d in destinations if d['id'] == destination_id), None)
        if not destination:
            return jsonify({'error': 'Destination not found'}), 404

        # Check if we have a valid API key
        if WEATHERAPI_KEY and WEATHERAPI_KEY != "55e07126c6e64ddca6a105841251804":
            # Try to use the real API
            params = {
                'key': WEATHERAPI_KEY,
                'q': f"{destination['coordinates']['lat']},{destination['coordinates']['lon']}",
                'aqi': 'no'
            }

            response = requests.get(WEATHERAPI_BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
                
                # Format the weather data for WeatherAPI.com response
                weather_info = {
                    'temperature': round(weather_data['current']['temp_c']),
                    'feels_like': round(weather_data['current']['feelslike_c']),
                    'humidity': weather_data['current']['humidity'],
                    'description': weather_data['current']['condition']['text'],
                    'icon': weather_data['current']['condition']['icon'],
                    'wind_speed': round(weather_data['current']['wind_kph'] / 3.6),  # Convert to m/s
                    'city': destination['name'],
                    'country': destination['country']
                }
                return jsonify(weather_info)
        
        # If API key is invalid or API call failed, use mock data
        # Generate realistic mock weather data based on destination
        weather_conditions = [
            {"description": "Sunny", "icon": "https://cdn.weatherapi.com/weather/64x64/day/113.png"},
            {"description": "Partly cloudy", "icon": "https://cdn.weatherapi.com/weather/64x64/day/116.png"},
            {"description": "Cloudy", "icon": "https://cdn.weatherapi.com/weather/64x64/day/119.png"},
            {"description": "Light rain", "icon": "https://cdn.weatherapi.com/weather/64x64/day/296.png"},
            {"description": "Moderate rain", "icon": "https://cdn.weatherapi.com/weather/64x64/day/302.png"}
        ]
        
        # Different destinations have different weather patterns
        condition_index = (destination['id'] - 1) % len(weather_conditions)
        condition = weather_conditions[condition_index]
        
        # Temperature ranges by region (roughly)
        base_temp = 0
        if destination['name'] in ['Paris', 'London', 'Rome']:  # Europe
            base_temp = 15  # Mild
        elif destination['name'] in ['Tokyo', 'Bali']:  # Asia
            base_temp = 24  # Warm
        elif destination['name'] == 'New York':  # North America
            base_temp = 12  # Varied
        elif destination['name'] == 'Sydney':  # Australia
            base_temp = 20  # Warm
            
        # Add some randomness
        temp_variation = random.randint(-3, 3)
        temp = base_temp + temp_variation
        
        # Mock weather info
        weather_info = {
            'temperature': temp,
            'feels_like': temp - 1 if condition['description'] in ['Cloudy', 'Light rain', 'Moderate rain'] else temp + 1,
            'humidity': random.randint(40, 85),
            'description': condition['description'],
            'icon': condition['icon'],
            'wind_speed': random.randint(2, 8),
            'city': destination['name'],
            'country': destination['country']
        }
        
        return jsonify(weather_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 