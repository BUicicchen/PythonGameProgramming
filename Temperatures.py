# Temperatures - easy
'''This program prints the temperature closest to 0 among input data'''

import sys
import math

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526


tempsList = temps.split() #split the list to get individual values

# display 0 (zero) if no temperatures are provided
if len(tempsList) == 0:
    print(0)

negative = []

# get the values of i if i is positive
# positive integer has to be considered closest to zero, so negative value minus a small number
for i in tempsList:
    negative.append(int(i) if int(i) > 0 else int(i)-0.1)

# use absolute value to find the amount away from 0
absValues =  [abs(i) for i in negative]

# closest temperature is the minimum number after absolute valuing
minTemperature = min(absValues)

# lowest index in list
ind = absValues.index(minTemperature)

print(tempsList[ind])
