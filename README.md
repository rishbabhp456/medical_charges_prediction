# Medical Insurance Charges Prediction

This is a web application that predicts medical insurance charges based on user-provided data. The application is built using Flask for the backend, serves a pre-trained machine learning model, and includes features for user authentication and data persistence.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Project Flow](#project-flow)

## Features

- **User Authentication**: Secure user registration, login, and password reset functionality.
- **JWT-based Authorization**: API endpoints are secured using JSON Web Tokens.
- **Medical Charges Prediction**: Utilizes a machine learning model to predict insurance costs.
- **Dynamic Frontend**: Dropdown menus are populated dynamically from the backend.
- **Data Logging**: User inputs and corresponding predictions are saved to a MongoDB database.

## Project Structure

```
medical_charges_prediction/
├── artifacts/
│   ├── linear_reg_model.pkl      # Trained machine learning model
│   └── project_data.json         # Data for encoding categorical features
├── src/
│   ├── __init__.py
│   ├── database.py               # MongoDB connection utility
│   └── utils.py                  # Core logic for model loading and prediction
├── templates/
│   ├── forget_password.html
│   ├── login.html
│   ├── prediction.html
│   └── register.html
├── config.py                     # Configuration file for paths, DB, etc.
├── main.py                       # Main Flask application file
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Technology Stack

- **Backend**: Flask
- **ML Model**: Scikit-learn (assumed, via pickle)
- **Database**: MongoDB
- **Authentication**: Flask-JWT-Extended
- **Libraries**: Pandas, NumPy

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd medical_charges_prediction
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Update `config.py` with your MongoDB connection string, database name, and collection names.

## Running the Application

Execute the `main.py` file to start the Flask development server:

```bash
python main.py
```

The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

The application exposes several REST API endpoints for user management and prediction.

| Method | Endpoint                 | Description                                                              |
|--------|--------------------------|--------------------------------------------------------------------------|
| POST   | `/register`              | Registers a new user.                                                    |
| POST   | `/login`                 | Authenticates a user and returns a JWT access token.                     |
| POST   | `/forget_password`       | Allows a user to reset their password.                                   |
| GET    | `/gender_options`        | Returns available options for the 'gender' field.                        |
| GET    | `/smoker_options`        | Returns available options for the 'smoker' field.                        |
| GET    | `/region_options`        | Returns available options for the 'region' field.                        |
| POST   | `/predict_charges`       | (Protected) Accepts user data and returns the predicted insurance charge.|

## Project Flow

1.  **User Registration/Login**: A new user can register. An existing user can log in to receive a JWT token.
2.  **Prediction Page**: After logging in, the user is redirected to the prediction page.
3.  **Input Data**: The user fills out a form with their details (age, BMI, children, gender, smoker status, region).
4.  **Submit for Prediction**: The user submits the form. The frontend sends a POST request with the form data and the JWT token in the header to the `/predict_charges` endpoint.
5.  **Backend Processing**: The Flask backend receives the request, validates the token, processes the input data, and feeds it to the machine learning model.
6.  **Return Prediction**: The model's prediction is returned to the user and displayed on the page.
7.  **Log Data**: The input data and the resulting prediction are stored as a new document in the MongoDB database.