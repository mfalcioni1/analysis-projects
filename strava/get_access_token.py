import os
from dotenv import load_dotenv, set_key, unset_key
from stravalib.client import Client
from datetime import datetime

# Load credentials from .env file in the same directory as the script
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv('STRAVA_CLIENT_ID')
CLIENT_SECRET = os.getenv('STRAVA_CLIENT_SECRET')
AUTH_CODE = os.getenv('STRAVA_AUTH_CODE')
ACCESS_TOKEN = os.getenv('STRAVA_ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('STRAVA_REFRESH_TOKEN')
EXPIRES_AT = os.getenv('STRAVA_EXPIRES_AT')

# Check if the current access token has expired
if EXPIRES_AT and datetime.now().timestamp() < float(EXPIRES_AT):
    print("Access token is still valid.")
    exit(0)

# Initialize Strava client
client = Client()

# Remove previous instances of STRAVA_ACCESS_TOKEN, STRAVA_REFRESH_TOKEN, and STRAVA_EXPIRES_AT
unset_key(env_path, 'STRAVA_ACCESS_TOKEN')
unset_key(env_path, 'STRAVA_REFRESH_TOKEN')
unset_key(env_path, 'STRAVA_EXPIRES_AT')

# Exchange access code for an access token
token_response = client.exchange_code_for_token(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                code=AUTH_CODE)

# Extract access token from the response
access_token = token_response['access_token']
refresh_token = token_response['refresh_token']
expires_at = token_response['expires_at']

print(f"Access Token: {access_token}")
print(f"Refresh Token: {refresh_token}")
print(f"Expires At: {expires_at}")

# Store the access token in a secure place
set_key(env_path, 'STRAVA_ACCESS_TOKEN', access_token)
set_key(env_path, 'STRAVA_REFRESH_TOKEN', refresh_token)
set_key(env_path, 'STRAVA_EXPIRES_AT', str(expires_at))
