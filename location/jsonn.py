import subprocess
import re
import json

def get_wifi_info():
    try:
        # Run the netsh command to get wireless network information
        result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], capture_output=True, text=True)
        output = result.stdout

        # Extract network information using regex
        networks = re.findall(r'^\s+SSID\s+\d+\s+:\s+(.*)', output, re.MULTILINE)
        mac_addresses = re.findall(r'^\s+BSSID\s+\d+\s+:\s+([0-9A-Fa-f:]{17})', output, re.MULTILINE)
        signal_strengths = re.findall(r'^\s+Signal\s+:\s+(\d+)%', output, re.MULTILINE)

        wifi_info = []
        for i in range(len(networks)):
            info = {
                'SSID': networks[i],
                'MAC Address': mac_addresses[i] if i < len(mac_addresses) else 'N/A',
                'Signal Strength': signal_strengths[i] if i < len(signal_strengths) else 'N/A'
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
