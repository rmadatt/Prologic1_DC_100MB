# Prologic1_DC_100MB
Data Collection App
A lightweight Flask web application to collect user data (Name, Age, 5 Interests, 5 Likes, 5 Dislikes, 5 Daily Habits) using a simple form, stored in SQLite. The app is under 100 MB and ready for deployment.
Features

Simple HTML form with validation.
Stores data in a SQLite database (data.db).
Minimal dependencies (Flask, Gunicorn).
Responsive design with inline CSS.

Setup and Deployment
Prerequisites

Python 3.6+
Git
A deployment platform (e.g., Render, Heroku, PythonAnywhere)

Local Setup (Optional)

Clone the repository


Install dependencies


Run the app



Deploy to Render

Create a new Web Service on Render.
Connect this GitHub repository.
Set:
Runtime: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app


Deploy and access the provided URL.

Project Structure
data-collection-app/
├── app.py              # Main Flask application
├── requirements.txt    # Dependencies
└── templates/
    ├── index.html      # Data collection form
    └── thank_you.html  # Submission confirmation

Notes

The SQLite database (data.db) is created automatically on first run.
Ensure the database path is secure in production.
App size (including dependencies) is well under 100 MB.

License
MIT License

