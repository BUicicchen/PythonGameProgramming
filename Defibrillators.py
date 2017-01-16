# Defibrillators - easy
'''This program allows users to find the defibrillator nearest to their location'''

import sys
import math

lon_a = input()
lat_a = input()
n = int(input())
listDefib = []
close = {}

def distanceD(lon_a, lat_a, lon_b, lat_b):
    #turn comma (,) into dot (.) in order to use the data in the program
    lon_a = float(lon_a.replace(',', '.'))
    lat_a = float(lat_a.replace(',', '.'))
    lon_b = float(lon_b.replace(',', '.'))
    lat_b = float(lat_b.replace(',', '.'))

    # formula to calculate x, y, and distance
    x = (lon_b - lon_a) * math.cos((lat_b + lat_a)/2)
    y = (lat_b - lat_a)
    distance = math.sqrt(x**2 + y**2) * 6371
    return distance

for i in range(n):
    defib = input()

    splitDefib = defib.split(';') # fields are separated by a semicolon (;)
    # dictionary for storing fields
    data = {"numDef":float(splitDefib[0]), "name":splitDefib[1], "address":splitDefib[2], "contactPN":splitDefib[3], "lon_a":splitDefib[4], "lat_a":splitDefib[5]}
    listDefib.append(data) # appending dictionary into defibrillators list

minDistance = "" #
if len(listDefib) > 1: # more than 1 defibrillators
    for location in listDefib:
        distance = distanceD(location["lon_a"], location["lat_a"], lon_a, lat_a) # use the function
        if minDistance == "":
            minDistance = distance
            listDefib = location
        elif minDistance > distance:
            minDistance = distance
            listDefib = location


print(listDefib["name"]) # name of closest defibrillator to the user's position
