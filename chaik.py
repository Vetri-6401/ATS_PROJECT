import time
import win32api
from win32api import GetSystemMetrics

def get_current_location():
    latitude = None
    longitude = None
    
    try:
        latitude = GetSystemMetrics(12) / 10**6
        longitude = GetSystemMetrics(13) / 10**6
    except Exception as e:
        print(f"Error fetching location: {e}")
    
    return latitude, longitude

while True:
    latitude, longitude = get_current_location()
    if latitude and longitude:
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Location not available.")
    time.sleep(10)  # Adjust the interval as needed


from gps3 import gps3

# Create a GPS object
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()

# Connect to the GPSD
gps_socket.connect()
gps_socket.watch()

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        # Fetching location details
        latitude = data_stream.TPV['lat']
        longitude = data_stream.TPV['lon']
        altitude = data_stream.TPV['alt']
        speed = data_stream.TPV['speed']

        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
        print(f'Altitude: {altitude}')
        print(f'Speed: {speed}')
