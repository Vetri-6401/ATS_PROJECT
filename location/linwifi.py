import requests
import json

def get_location(api_key, wifi_access_points):
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + api_key
    
    # Prepare the request payload
    payload = {
        "wifiAccessPoints": wifi_access_points
    }
    
    # Send the request to Google Geolocation API
    response = requests.post(url, json=payload)
    
    # Handle the response
    if response.status_code == 200:
        location_data = response.json()
        return location_data
    else:
        print("Error:", response.status_code)
        print(response.text)
        return None

# Example Wi-Fi access points data
wifi_access_points = [
    {
    "macAddress": "",
    "signalStrength": -43.6
  },
  {
    "macAddress": "",
    "signalStrength": -74.8
  }
]

# Your Google API key
api_key = ''

# Fetch location
location_data = get_location(api_key, wifi_access_points)
if location_data:
    print("Location Data:", json.dumps(location_data, indent=4))
