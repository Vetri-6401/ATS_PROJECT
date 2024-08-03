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

if __name__ == "__main__":
    wifi_info = get_wifi_info()
    if wifi_info:
        print(json.dumps(wifi_info, indent=2))
