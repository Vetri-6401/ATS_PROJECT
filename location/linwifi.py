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
    "macAddress": "f6:9f:c2:21:4d:b1",
    "signalStrength": -43.6
  },
  {
    "macAddress": "f0:9f:c2:21:4e:a6",
    "signalStrength": -74.8
  },
  {
    "macAddress": "f0:9f:c2:21:4d:9f",
    "signalStrength": -77.2
  },
  {
    "macAddress": "06:ab:08:96:50:f2",
    "signalStrength": -60.4
  },
  {
    "macAddress": "f0:9f:c2:21:4d:b1",
    "signalStrength": -43.6
  },
  {
    "macAddress": "fe:9f:c2:21:4d:b1",
    "signalStrength": -43.6
  },
  {
    "macAddress": "fe:9f:c2:21:4e:a6",
    "signalStrength": -77.2
  },
  {
    "macAddress": "fa:9f:c2:21:4d:9f",
    "signalStrength": -79.6
  },
  {
    "macAddress": "fe:9f:c2:21:4d:9f",
    "signalStrength": -79.6
  },
  {
    "macAddress": "04:ab:08:b6:50:f2",
    "signalStrength": -59.2
  },
  {
    "macAddress": "52:91:e3:e1:49:ce",
    "signalStrength": -94.0
  },
  {
    "macAddress": "f0:ed:b8:0a:f8:c9",
    "signalStrength": -79.6
  },
  {
    "macAddress": "fa:9f:c2:21:4d:b1",
    "signalStrength": -46.0
  },
  {
    "macAddress": "f6:9f:c2:21:4e:a6",
    "signalStrength": -77.2
  },
  {
    "macAddress": "24:43:e2:2c:ac:78",
    "signalStrength": -58.0
  },
  {
    "macAddress": "04:18:d6:1d:e0:a0",
    "signalStrength": -76.0
  },
  {
    "macAddress": "0c:73:29:20:46:01",
    "signalStrength": -79.6
  },
  {
    "macAddress": "50:91:e3:e1:49:ce",
    "signalStrength": -94.0
  }
]

# Your Google API key
api_key = ''

# Fetch location
location_data = get_location(api_key, wifi_access_points)
if location_data:
    print("Location Data:", json.dumps(location_data, indent=4))
