# Access Strava
One-time set-up

```py
from stravalib import Client
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')

client = Client()

url = client.authorization_url(client_id=client_id, 
                               redirect_uri='http://127.0.0.1:5000/authorization', 
                               scope=['read_all','profile:read_all','activity:read_all'])

print(url)
```