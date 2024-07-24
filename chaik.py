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
