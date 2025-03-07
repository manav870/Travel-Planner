# Personalized Travel Planner

A web application for planning and organizing trips, built with Python and Flask.

## Features

- Browse popular travel destinations
- View detailed information about destinations
- Plan trips with customized itineraries
- Set travel dates and budgets
- Track planned activities
- View all your planned trips

## Technologies Used

- **Backend**: Python with Flask framework
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Bootstrap 5
- **Database**: Currently using in-memory storage (can be extended to use SQLite, MySQL, etc.)

## Project Structure

```
Travel Planner/
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── app/                    # Application package
│   ├── static/             # Static files
│   │   ├── css/            # CSS files
│   │   ├── js/             # JavaScript files
│   │   └── images/         # Image files
│   ├── templates/          # HTML templates
│   └── models/             # Data models
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd travel-planner
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Future Enhancements

- User authentication and profiles
- Database integration for persistent storage
- Weather API integration for destination forecasts
- Map integration for visualizing destinations
- Accommodation and flight booking recommendations
- Social sharing features
- Mobile app version

## College Project Information

This project was created as part of a college assignment to demonstrate web application development skills using Python.

## License

This project is for educational purposes only. 