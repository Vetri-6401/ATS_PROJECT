import subprocess
import re
import json
import time

def get_wifi_info():
    try:
        # Run the netsh command to get wireless network information
        result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], capture_output=True, text=True)
        output = result.stdout

        # Extract network information using regex
        mac_addresses = re.findall(r'^\s+BSSID\s+\d+\s+:\s+([0-9A-Fa-f:]{17})', output, re.MULTILINE)
        signal_strengths = re.findall(r'^\s+Signal\s+:\s+(\d+)%', output, re.MULTILINE)

        wifi_info = []

        for i in range(len(mac_addresses)):
            info = {
                'macAddress': mac_addresses[i],
                'signalStrength': -100+(int(signal_strengths[i])*0.6)
            }
            wifi_info.append(info)

        return wifi_info

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

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
# wifi_access_points = [
#     {
#     "macAddress": macaddress,
#     "signalStrength": -43.6
#   },
# ]
# Your Google API key


# Fetch location

if __name__ == "__main__":
    api_key = 'YOUR API KEY'
    wifi_info = get_wifi_info()
    if wifi_info:
        print(json.dumps(wifi_info, indent=2))

    location_data = get_location(api_key, wifi_info)
    if location_data:
        print("Location Data:", json.dumps(location_data, indent=2))
