import urllib.request, urllib.parse
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    loc = input('Enter location: ')
    if len(loc)<1:break

    parms = dict()
    parms['address'] = loc
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)

    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    print('Retrieved:', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js=None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=====Faliure to Retrive=======')
        print(data)
        continue

    placeid = js['results'][0]['place_id']
    print('Place id', placeid)
