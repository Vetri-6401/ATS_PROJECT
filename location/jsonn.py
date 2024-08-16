import subprocess
import re
import time
import platform


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

        else:
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
