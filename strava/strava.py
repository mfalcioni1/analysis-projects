from stravalib import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve client ID and client secret from environment variables
client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')

# Create a Strava client
client = Client()

url = client.authorization_url(client_id=client_id, 
                               redirect_uri='http://127.0.0.1:5000/authorization', 
                               scope=['read_all','profile:read_all','activity:read_all'])

print(url)
# Set access token (optional if using OAuth2)
client.access_token = access_token

# Fetch activities
activities = client.get_activities()

# Print activity names and types
for activity in activities:
    print(activity.name, activity.type)
