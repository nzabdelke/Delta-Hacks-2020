#from ipstack import GeoLookup
#geo_lookup = GeoLookup("cca0c85e10af1f0255c8cceca6079c74")
#location = geo_lookup.get_location("http://api.ipstack.com/130.113.69.107")
#print(location)
import requests
import json
key = "cca0c85e10af1f0255c8cceca6079c74"
url ="http://api.ipstack.com/130.113.69.107" + "?access_key=" + key
response = requests.get(url).json()
def getLatitude():
	return(response.get("latitude"))

def getLongitude():
	return (response.get("longitude"))






#x = getLatitude()
#y = getLongitude()
#print(x)
#print(y)
#for g,h  in response.items():
	#print(g,h)
