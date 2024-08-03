import requests
import json

def get_location_info(lat, lon, api_key):
    # Construct the URL with parameters
    url = f'https://api.olamaps.io/places/v1/reverse-geocode?latlng={lat},{lon}&api_key={api_key}'
    
    # Make the GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract and print the location information
        # Modify according to the actual structure of the response
        address = data.get('results', [])[0] if 'results' in data else {}
        formatted_address = address.get('formatted_address', 'Address not found')
        
        return formatted_address
    else:
        # Handle errors
        return f"Error: {response.status_code}, {response.text}"

# Example usage
latitude = 13.0628743
longitude = 80.1692679
api_key = ''  # Replace 'XXX' with your actual API key

location_info = get_location_info(latitude, longitude, api_key)
print("Location Info:", location_info)
