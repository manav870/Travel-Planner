@echo off
echo Starting Travel Planner Application...

REM Check if virtual environment exists
if not exist venv (
    echo Virtual environment not found. Please run setup.bat first.
    pause
    exit /b
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the Flask application
echo Starting Flask server...
python app.py

pause 