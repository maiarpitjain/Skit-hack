import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDHZvKpFeTiCAw5DSMh40S5ulmQscyCGto')

# Geocoding an address
geocode_result = gmaps.geocode('pratap nagar, jaipur, india')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("pratap nagar, jaipur",
                                     "tonk,india",
                                     mode="transit",
                                     departure_time=now)

print(directions_result)