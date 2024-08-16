import subprocess
import re
import time
import platform


def get_wifi_info():
    try:
        wifi_info = []

        if platform.system()=='Windows':
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

            time.sleep(4)
            print(wifi_info)
            return wifi_info

        elif platform.system()=='Linux':
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
            time.sleep(4)
            print(networks)
            return networks
        
       

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
