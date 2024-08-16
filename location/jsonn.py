import subprocess
import re
import time
import platform
import json
import requests

def get_wifi_info():
    try:
        wifi_info = []

        if platform.system() == 'Windows':
            result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], capture_output=True, text=True)
            output = result.stdout

            mac_addresses = re.findall(r'^\s+BSSID\s+\d+\s+:\s+([0-9A-Fa-f:]{17})', output, re.MULTILINE)
            signal_strengths = re.findall(r'^\s+Signal\s+:\s+(\d+)%', output, re.MULTILINE)

            if len(mac_addresses) != len(signal_strengths):
                raise ValueError("Mismatch between MAC addresses and signal strengths count")

            for i in range(len(mac_addresses)):
                signal_strength = -100 + (int(signal_strengths[i]) * 0.6)
                wifi_info.append({
                    'macAddress': mac_addresses[i],
                    'signalStrength': signal_strength
                })

        elif platform.system()=='Linux':
            try:
                result = subprocess.run(['sudo', 'iwlist', 'scan'], capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Error running iwlist command:", e)
                return []

            networks = []
            current_network = {}

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
                    current_network['signalStrength'] = float(signal_match.group(1))

            if current_network:
                networks.append(current_network)
            
            wifi_info = networks
        
        print(wifi_info)
        return wifi_info

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
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

    return response.json()

if __name__ == "__main__":
    api_key = ''
    wifi_info = get_wifi_info()
    if wifi_info:
        print("Scanned Wi-Fi Networks:")
        print(json.dumps(wifi_info, indent=2))

    location_data = get_location(api_key, wifi_info)
    if location_data:
        print("Location Data:")
        print(json.dumps(location_data, indent=2))
