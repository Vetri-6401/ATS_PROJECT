import subprocess
import re
import json
import requests

def scan_networks():
    # Run the `iwlist` command to scan for networks
    result = subprocess.run(['sudo', 'iwlist', 'scan'], capture_output=True, text=True)
    
    networks = []
    current_network = {}
    
    # Use regex to extract MAC address and signal strength
    mac_regex = re.compile(r"Cell\s+\d+ - Address: ([\w:]+)")
    signal_regex = re.compile(r"Signal level=(-?\d+) dBm")
    
    for line in result.stdout.split('\n'):
        mac_match = mac_regex.search(line)
        signal_match = signal_regex.search(line)
        
        if mac_match:
            if current_network:
                networks.append(current_network)
            current_network = {'macAddress': mac_match.group(1)}
        
        if signal_match:
            current_network['signalStrength'] = signal_match.group(1)
    
    if current_network:
        networks.append(current_network)
    
    return networks


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
    wifi_info = scan_networks()
    if wifi_info:
        print(json.dumps(wifi_info, indent=2))

    location_data = get_location(api_key, wifi_info)
    if location_data:
        print("Location Data:", json.dumps(location_data, indent=2))
