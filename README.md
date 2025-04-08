# Travel Planner

A modern web application for planning and organizing your travel adventures. Built with Flask and Bootstrap, this application helps users discover destinations, plan itineraries, and track their trips.

## Features

### 1. Destination Discovery
- Browse popular travel destinations
- View detailed information about each destination
- Access top attractions and points of interest
- Get travel tips and recommendations
- View real-time weather information
- Interactive maps and location details

### 2. Trip Planning
- Create personalized travel itineraries
- Add attractions to your trip plan
- Track suggested budgets
- View transportation options
- Save and manage multiple trips

### 3. User Experience
- Modern, responsive design
- Interactive UI elements
- Real-time weather updates
- Location-based information
- Mobile-friendly interface

## Technology Stack

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: Database ORM
- **Jinja2**: Template engine
- **RESTful API**: For weather and location data

### Frontend
- **Bootstrap 5**: Responsive design framework
- **JavaScript**: Interactive features
- **CSS3**: Modern styling and animations
- **Font Awesome**: Icons and visual elements

### APIs
- Weather API for real-time weather data
- Google Maps API for location services

## Project Structure

```
Travel-Planner/
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │       └── destinations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── destination.html
│   │   ├── attractions.html
│   │   ├── all_destinations.html
│   │   └── plan_trip.html
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Key Components

### 1. Destination Management
- Detailed destination pages with:
  - Header images
  - Location information
  - Weather widget
  - Attractions list
  - Travel tips
  - Transportation details

### 2. Weather Integration
- Real-time weather updates
- Temperature, humidity, and wind speed
- Weather icons and descriptions
- Automatic refresh every 30 minutes

### 3. Location Services
- Interactive maps
- Coordinates display
- Continent information
- Google Maps integration

### 4. UI Components
- Modern card-based design
- Glassmorphism effects
- Hover animations
- Responsive layouts
- Interactive elements

## Installation

### Windows (Easy Setup)

1. Run the Setup File:
   - Double-click on `setup.bat`
   - This will create a virtual environment and install all required dependencies
   - Wait until you see "Setup completed successfully!"

2. Run the Application:
   - Double-click on `run_app.bat`
   - This will start the Flask server
   - The application will be accessible at http://127.0.0.1:5000

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Travel-Planner.git
cd Travel-Planner
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# On Linux/Mac:
export FLASK_APP=app
export FLASK_ENV=development

# On Windows (Command Prompt):
set FLASK_APP=app
set FLASK_ENV=development

# On Windows (PowerShell):
$env:FLASK_APP="app"
$env:FLASK_ENV="development"
```

5. Run the application:
```bash
python app.py  # or "flask run"
```

## Configuration

1. Create a `.env` file with the following variables:
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your_secret_key
WEATHER_API_KEY=your_weather_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

2. Update the database configuration in `app/__init__.py`

## Usage

1. Access the application at `http://localhost:5000`
2. Browse destinations
3. View destination details
4. Plan your trips
5. Track your itineraries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weather data provided by [WeatherAPI]
- Maps integration powered by Google Maps
- Icons by Font Awesome
- Design inspiration from modern travel websites 

## Troubleshooting

- **Python Not Found**: Ensure Python is installed and added to the PATH
- **Module Not Found Errors**: Make sure setup.bat ran successfully or requirements are installed
- **Port Already in Use**: Close any other applications using port 5000, or modify app.py to use a different port 