import urllib.request, urllib.parse
import json

'''
    Use a GeoLocation lookup API modelled after the Google API to look up some
    universities and parse the returned data. The program will prompt for a location,
    contact a web service and retrieve JSON for the web service and parse that data,
    and retrieve the first place_id from the JSON. A place ID is a textual identifier
    that uniquely identifies a place as within Google Maps.

    Use this API endpoint that has a static subset of the Google Data:
    http://py4e-data.dr-chuck.net/geojson?
'''

loc = input('Enter location: ')
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
url = serviceurl + urllib.parse.urlencode({'address': loc}) #Covert mapping object to a percent-encoded ASCII text string.
print('Retrieving', url)

connection = urllib.request.urlopen(url)
data = connection.read().decode() #string from utf-8 to unicode
print('Retrieved:', len(data), 'characters')
js = json.loads(data) #deserialize 'data' to a Python object

placeid = js['results'][0]['place_id']
print('Place id', placeid)
