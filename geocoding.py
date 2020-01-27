from geopy.geocoders import Nominatim
from geo import getLatitude, getLongitude 
def findAddress():
	geolocator = Nominatim(user_agent="specify_your_app_name_here")
	line = str(getLatitude()) + "," +  str(getLongitude())
	location = geolocator.reverse(line)
	return(location.address)
	
	

	#results = Geocoder.reverse_geocode(lat, long)
	#return(results.street_address + ", " +results.city + ", " + results.country) 