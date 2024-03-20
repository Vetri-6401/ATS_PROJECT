from geopy.geocoders import Nominatim

def address_details(lat,lon):

    geo_Loc=Nominatim(user_agent="GetLoc")

    Location_name=geo_Loc.reverse(f"{lat},{lon}")

    return Location_name.address