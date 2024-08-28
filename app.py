import os
import requests

# Hardcoded database credentials
DATABASE_HOST = "localhost"
DATABASE_USER = "admin"
DATABASE_PASSWORD = "SuperSecretPassword123"

def connect_to_database():
    print(f"Connecting to database at {DATABASE_HOST} with user {DATABASE_USER}")
    # In a real application, this would be where the connection happens
    print("Database connection successful")

# API key for an external service 
API_KEY = "1234567890abcdef"

def fetch_data_from_api():
    url = f"https://api.example.com/data?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data fetched successfully")
    else:
        print("Failed to fetch data")

# Secret token used for  authentication
SECRET_TOKEN = "s3cr3t-t0k3n"

def authenticate():
    print(f"Authenticating with secret token: {SECRET_TOKEN}")
    # Simulate authentication process
    print("Authentication successful")

if __name__ == "__main__":
    connect_to_database()
    fetch_data_from_api()
    authenticate()
