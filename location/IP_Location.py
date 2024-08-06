import subprocess
import re
import json
import requests

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
                'signalStrength': -100 + (int(signal_strengths[i]) * 0.6)
            }
            wifi_info.append(info)

        return wifi_info

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_location(api_key, wifi_access_points=None, ip_address=None):
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + api_key
    
    # Prepare the request payload based on available data
    payload = {}
    if wifi_access_points:
        payload["wifiAccessPoints"] = wifi_access_points
    elif ip_address:
        payload["considerIp"] = "true"  # Use IP address for location
    
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

if __name__ == "__main__":
    api_key = 'YOUR API KEY'
    
    wifi_info = get_wifi_info()
    
    if wifi_info:
        print("Wi-Fi Information:")
        print(json.dumps(wifi_info, indent=2))

        location_data = get_location(api_key, wifi_access_points=wifi_info)
        if location_data:
            print("Latitude:", location_data['location']['lat'])
            print("Longitude:", location_data['location']['lng'])
            print("Accuracy:", location_data['accuracy'])
        else:
            print("Failed to get location data using Wi-Fi.")
            # Optionally, you can add logic to handle IP-based location here
    else:
        print("No Wi-Fi information available. Attempting to use IP-based geolocation.")
        location_data = get_location(api_key, ip_address='true')  # Trigger IP-based location
        if location_data:
            print("Latitude:", location_data['location']['lat'])
            print("Longitude:", location_data['location']['lng'])
            print("Accuracy:", location_data['accuracy'])
        else:
            print("Failed to get location data using IP.")
