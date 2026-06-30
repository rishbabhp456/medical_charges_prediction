# Medical Insurance Charges Prediction

This is a web application that predicts medical insurance charges based on user-provided data. The application is built using Flask for the backend, serves a pre-trained machine learning model, and includes features for user authentication and data persistence.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Set and Run](#set-and-run)
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

## Set and Run

1.  **Clone the repository**
    ```bash
    git clone <your-repository-url>
    cd medical_charges_prediction
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the application**
    Update `config.py` with your MongoDB connection string, database name, and collection names.

5.  **Run the application**
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

The application workflow is centered around user authentication and model prediction, with MongoDB integrated at key points:

1.  **User Registration**: A new user provides their details via the `/register` endpoint. The application checks the `users` collection in MongoDB to ensure the user doesn't already exist before inserting a new user document.
2.  **User Login**: An existing user logs in via the `/login` endpoint. The application queries the `users` collection to validate the credentials. Upon success, a JWT access token is generated and sent to the client.
3.  **Prediction Page**: The user navigates to the prediction form. Dynamic dropdowns for `gender`, `smoker`, and `region` are populated by fetching data via dedicated API endpoints.
4.  **Submit for Prediction**: The user fills out the form and submits it. The frontend sends a POST request to the `/predict_charges` endpoint.
5.  **Backend Processing**: The Flask backend receives the data, converts it into the format required by the machine learning model, and generates a prediction.
6.  **Data Logging**: The application logs the user's input data along with the model's prediction by inserting a new document into the `prediction_data` collection in MongoDB. This is useful for monitoring and future model retraining.
7.  **Return Prediction**: The final predicted insurance charge is returned as a JSON response and displayed to the user on the frontend.
# medical_insurance_price_prediction