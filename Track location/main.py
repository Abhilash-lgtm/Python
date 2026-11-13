import phonenumbers
import opencage
import folium

from myphone import number

from phonenumbers import geocoder

parsed_number = phonenumbers.parse(number)
location = geocoder.description_for_number(parsed_number, "en")
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
key = 'd9d2b769cac84bf9a41534ca8cf53f71'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)   
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
"""
mymap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(mymap)

mymap.save("mylocation.html")"""