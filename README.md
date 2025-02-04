# Number_Classification_API

## Overview

The Number Classification API is a simple REST API that classifies numbers based on certain criteria. It allows users to send a number as a query parameter and receive a JSON response indicating whether the number is even, odd, prime, or any other classification logic implemented.

## Features

- Classifies numbers as even or odd

- Determines if a number is prime

- Returns a JSON response with classification details

- RESTful API endpoints

- Live Deployment

The API is hosted on Render and can be accessed at:

https://number-classification-api-glt0.onrender.com/api/classify-number?number=<your_number>

## Technologies Used

- Python 3.12

- Django

- Django REST Framework

- Gunicorn (for deployment)

- Render (for hosting)

## Installation & Setup

- Prerequisites

Python 3.12 installed

Virtual environment setup (recommended)

### Steps to Set Up Locally

Clone the repository:

git clone https://github.com/yourusername/Number_Classification_API.git
cd Number_Classification_API

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies: pip install -r requirements.txt

Apply database migrations: python manage.py migrate

Run the local development server: python manage.py runserver

Test the API:

curl http://127.0.0.1:8000/api/classify-number?number=7

## API Endpoints

1. Classify Number

Endpoint:

GET /api/classify-number?number=<number>

### Example Request:

GET /api/classify-number?number=7

### Example Response:

{
    "number": 7,
    "even": false,
    "odd": true,
    "prime": true
}

## Deployment on Render

- Push your code to GitHub

- Create a new web service on Render

- Set the build command:

- pip install -r requirements.txt

- Set the start command:

- gunicorn Number_classification.wsgi:application

- Define PORT as an environment variable (Render automatically assigns one)

- Environment Variables

- DEBUG (set to False in production)

- SECRET_KEY (set a strong secret key)

## Issues & Contributions

Feel free to open issues or pull requests on GitHub.

### If you find a bug, please provide clear steps to reproduce.

## License

This project is licensed under the MIT License.