from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from datetime import datetime

app = Flask(__name__, 
            static_folder='app/static',
            template_folder='app/templates')

app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Sample data - in a real app, you would use a database
destinations = [
    {
        'id': 1,
        'name': 'Paris',
        'country': 'France',
        'description': 'The City of Light',
        'image': 'paris.jpg',
        'attractions': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
        'suggested_budget': {'min': 1200, 'max': 2000}
    },
    {
        'id': 2,
        'name': 'Tokyo',
        'country': 'Japan',
        'description': 'A blend of traditional and ultramodern',
        'image': 'tokyo.jpg',
        'attractions': ['Tokyo Tower', 'Senso-ji Temple', 'Shibuya Crossing'],
        'suggested_budget': {'min': 1500, 'max': 2500}
    },
    {
        'id': 3,
        'name': 'New York',
        'country': 'USA',
        'description': 'The Big Apple',
        'image': 'newyork.jpg',
        'attractions': ['Statue of Liberty', 'Central Park', 'Empire State Building'],
        'suggested_budget': {'min': 1800, 'max': 3000}
    },
    {
        'id': 4,
        'name': 'Rome',
        'country': 'Italy',
        'description': 'The Eternal City',
        'image': 'rome.jpg',
        'attractions': ['Colosseum', 'Vatican City', 'Trevi Fountain'],
        'suggested_budget': {'min': 1000, 'max': 1800}
    },
    {
        'id': 5,
        'name': 'Bali',
        'country': 'Indonesia',
        'description': 'Island of the Gods',
        'image': 'bali.jpg',
        'attractions': ['Ubud Monkey Forest', 'Tanah Lot Temple', 'Kuta Beach'],
        'suggested_budget': {'min': 800, 'max': 1500}
    },
    {
        'id': 6,
        'name': 'London',
        'country': 'United Kingdom',
        'description': 'The Historic Capital',
        'image': 'london.jpg',
        'attractions': ['Buckingham Palace', 'Big Ben', 'London Eye'],
        'suggested_budget': {'min': 1500, 'max': 2500}
    },
    {
        'id': 7,
        'name': 'Sydney',
        'country': 'Australia',
        'description': 'The Harbour City',
        'image': 'sydney.jpg',
        'attractions': ['Sydney Opera House', 'Bondi Beach', 'Sydney Harbour Bridge'],
        'suggested_budget': {'min': 1600, 'max': 2700}
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

if __name__ == '__main__':
    app.run(debug=True) 