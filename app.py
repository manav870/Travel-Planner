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
        'attractions': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral']
    },
    {
        'id': 2,
        'name': 'Tokyo',
        'country': 'Japan',
        'description': 'A blend of traditional and ultramodern',
        'image': 'tokyo.jpg',
        'attractions': ['Tokyo Tower', 'Senso-ji Temple', 'Shibuya Crossing']
    },
    {
        'id': 3,
        'name': 'New York',
        'country': 'USA',
        'description': 'The Big Apple',
        'image': 'newyork.jpg',
        'attractions': ['Statue of Liberty', 'Central Park', 'Empire State Building']
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
        # Process the form data
        activities_text = request.form.get('activities', '').strip()
        activities_list = [activity.strip() for activity in activities_text.split(',')] if activities_text else []
        
        new_trip = {
            'id': len(trips) + 1,
            'destination_id': int(request.form.get('destination')),
            'start_date': request.form.get('start_date'),
            'end_date': request.form.get('end_date'),
            'budget': float(request.form.get('budget')),
            'activities': activities_list,
            'created_at': datetime.now()
        }
        trips.append(new_trip)
        flash('Trip planned successfully!', 'success')
        return redirect(url_for('my_trips'))
    
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