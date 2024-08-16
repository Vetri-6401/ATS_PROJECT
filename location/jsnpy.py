import subprocess
import re
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
                result = subprocess.run(['nmcli', '-f', 'SSID,CHAN,RATE,SIGNAL', 'device', 'wifi', 'list'], capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Error running nmcli command:", e)
                return []

            networks = []
            lines = result.stdout.split('\n')[1:]  # Skip header line
            for line in lines:
                if line.strip():
                    parts = re.split(r'\s{2,}', line.strip())
                    if len(parts) >= 4:
                        ssid = parts[0]
                        signal_strength = float(parts[3])
                        networks.append({
                            'ssid': ssid,
                            'signalStrength': signal_strength
                        })

            wifi_info = networks
        
        print(wifi_info)
        return wifi_info

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
