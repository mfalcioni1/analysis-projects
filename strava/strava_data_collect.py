import os
from dotenv import load_dotenv
from stravalib.client import Client
import pandas as pd

# data location
data_path = os.path.join(os.path.dirname(__file__), 'data/running_activities_header.csv')

# Load credentials from .env file
load_dotenv()
ACCESS_TOKEN = os.getenv('STRAVA_ACCESS_TOKEN')

# Initialize Strava client
client = Client()
client.access_token = ACCESS_TOKEN

# Function to fetch all running activities
def fetch_running_activities(client):
    activities = client.get_activities()
    running_activities = []
    for activity in activities:
        if activity.type == 'Run':
            running_activities.append({
                'id': activity.id,
                'name': activity.name,
                'distance': activity.distance.num,
                'moving_time': activity.moving_time.total_seconds(),
                'elapsed_time': activity.elapsed_time.total_seconds(),
                'total_elevation_gain': activity.total_elevation_gain.num,
                'type': activity.type,
                'start_date': activity.start_date,
                'start_date_local': activity.start_date_local,
                'timezone': activity.timezone,
                'utc_offset': activity.utc_offset,
                'location_city': activity.location_city,
                'location_state': activity.location_state,
                'location_country': activity.location_country,
                'achievement_count': activity.achievement_count,
                'kudos_count': activity.kudos_count,
                'comment_count': activity.comment_count,
                'athlete_count': activity.athlete_count,
                'photo_count': activity.photo_count,
                'map': activity.map.summary_polyline,
                'average_speed': activity.average_speed.num,
                'max_speed': activity.max_speed.num,
                'average_cadence': activity.average_cadence,
                'average_temp': activity.average_temp,
                'average_watts': activity.average_watts,
                'weighted_average_watts': activity.weighted_average_watts,
                'kilojoules': activity.kilojoules,
                'device_watts': activity.device_watts,
                'has_heartrate': activity.has_heartrate,
                'average_heartrate': activity.average_heartrate,
                'max_heartrate': activity.max_heartrate,
                'pr_count': activity.pr_count,
                'total_photo_count': activity.total_photo_count,
                'has_kudoed': activity.has_kudoed,
            })
    return pd.DataFrame(running_activities)

# Fetch and store running activities
df = fetch_running_activities(client)
df.to_csv(data_path, index=False)

print("Activities fetched and saved to running_activities_header.csv")
