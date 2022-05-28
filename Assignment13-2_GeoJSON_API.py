# Week 6 : Using the GeoJSON API
# Calling a JSON API
#write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py.
#Prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
#Retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place
#as within Google Maps.



import urllib.request, urllib.parse, urllib.error
import json

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
#url= 'http://py4e-data.dr-chuck.net/comments_1414076.json'
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


while True:
    # South Federal University
    address = input('Enter location: ')
    if len(address) < 1:
        print('No address...')
        # Question: continue
        quit()

# Error: Address = peremeter + key: peremeter
    url = serviceurl + urllib.parse.urlencode({'address': address, 'key' : 42})
    print('Retrieving', url)


    # send request and open the the url
    #uh= urllib.request.urlopen(url)
    uh = urllib.request.urlopen(url)


    # read and decode to readable format
    data=uh.read().decode()
    print('Retriving', len(data), 'characters')


    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        break

    print(json.dumps(js, indent = 4))

#Error: print('Count:', len(info)) # only counting list instead od dic
    placeid = js["results"][0]['place_id']
    print ("Place id",placeid)
