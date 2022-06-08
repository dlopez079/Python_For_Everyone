# Inport urllib request, parse and error
import urllib.request, urllib.parse, urllib.error

# Import the JSON library
import json

# Import the SSL library for certs.
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create a continuous loop so input is always requested.
while True:

    # Grab address from input user.
    address = input('Enter location: ')

    # If they don't put anything, the program will stopped. 
    if len(address) < 1: break

    # Save parameters into a dictionary list.
    parms = dict()

    # Enter address into parms list.
    parms['address'] = address
    
    # If the api key exist, add key to params dictionary
    if api_key is not False: parms['key'] = api_key

    # Parse, encode and add to service URL
    url = serviceurl + urllib.parse.urlencode(parms)

    # Confirm that the URL is working with a print.
    print('Retrieving', url)

    # Gather JSON URL 
    uh = urllib.request.urlopen(url, context=ctx)

    # Read and Decode the information on the site.
    data = uh.read().decode()

    # Print the length of data and the characters.
    print('Retrieved', len(data), 'characters')

    # Check if data can load via json, If not create a new positive
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # The command below displays the data in viewable format.
    # print(json.dumps(js, indent=4))

    # Navigate through the JSON and grab position for place id.
    place_id = js['results'][0]['place_id']

    # Print out place ID.
    print('Place id:', place_id)