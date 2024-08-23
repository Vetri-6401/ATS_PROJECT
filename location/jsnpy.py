import subprocess
import json

def scan_wifi():
    try:
        # Run nmcli command to scan for networks
        result = subprocess.check_output(['nmcli', '-f', 'SSID,BSSID,SIGNAL', 'device', 'wifi', 'list'], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print("Error running nmcli:", e.output)
        return []

    # Parse the output to extract network details
    networks = []
    lines = result.strip().split('\n')[1:]  # Skip the header line
    
    for line in lines:
        parts = line.split()
        if len(parts) >= 3:
            ssid = ' '.join(parts[:-2])
            mac_address = parts[-2]
            signal_strength = (-int(parts[-1]))  # Signal strength is already in dBm
            networks.append({
                'macAddress': mac_address,
                'signalStrength': signal_strength
            })
    
    return networks
import requests
def get_location(api_key, wifi_access_points):
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + api_key
    payload = {"wifiAccessPoints": wifi_access_points}
    

    response = requests.post(url, json=payload)
    if response.status_code==200:
        location_data=response.json()
        return location_data
    else:
        print(response.status_code)
        print(response.text)
        return None
if __name__ == "__main__":
    api_key = 'YOUR API KEY'
    wifi_info = scan_wifi()
    if wifi_info:
        print("Scanned Wi-Fi Networks:")
       

    location_data = get_location(api_key, wifi_info)
    if location_data:
        print("Location Data:")
        print(json.dumps(location_data, indent=2))
