# import module
import sys
from geopy.geocoders import Nominatim

def start():
 while True:
    geolocator = Nominatim(user_agent="geoapiExercises")
    # get input
    name = input("Name: ")
    fname = name.split()
    place = input("Address: ")
    last_four = input("Last 4 of zip: ")
    location = geolocator.geocode(place)
  
    # locate and format data
    data = location.raw
    loc_data = data['display_name'].split(',')
    #print (loc_data) used to find location of data(line 17)
    mylist = fname[0], fname[1], place, loc_data[-5], loc_data[-3], loc_data[-2]
    fullzip = mylist[5] + '-' + str(last_four)
    final =(*mylist, fullzip)
    output = str(final)
    print (output)
   

start()

