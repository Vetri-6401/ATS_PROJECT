import subprocess
import re
import json

def get_wifi_info():
    try:
        # Run the nmcli command to get wireless network information
        result = subprocess.run(['nmcli', '-f', 'BSSID,SIGNAL', 'device', 'wifi', 'list'], capture_output=True, text=True)
        output = result.stdout

        # Extract network information using regex
        wifi_info = []
        lines = output.splitlines()
        for line in lines[1:]:  # Skip header line
            fields = line.split()
            if len(fields) >= 2:
                mac_address = fields[0]
                signal_strength = int(fields[1])

                info = {
                    'macAddress': mac_address,
                    'signalStrength': signal_strength,
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
