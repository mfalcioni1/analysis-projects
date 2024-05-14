import os
from dotenv import load_dotenv, set_key, unset_key
from stravalib import Client

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

# Retrieve client ID and client secret from environment variables
client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')

# Create a Strava client
client = Client()

# Generate the authorization URL
url = client.authorization_url(client_id=client_id, 
                               redirect_uri='http://127.0.0.1:5000/authorization', 
                               scope=['read_all','profile:read_all','activity:read_all'])

# Print the URL for the user to authenticate
print("Go to the following URL to authenticate:")
print(url)

# Prompt the user to enter the access code from the URL
AUTH_CODE = input("Enter the authorization code from the URL: ")

unset_key(env_path, 'STRAVA_AUTH_CODE')
set_key(env_path, 'STRAVA_AUTH_CODE', AUTH_CODE)
print("Authorization code stored successfully.")