# Horse-racing Dual - easy
'''This program uses a given number of strengths to identify two closest strengths, and shows their difference'''
import sys
import math

n = int(input()) # number of horses
horses = []
for i in range(n):
    pi = int(input()) # strength of each horse
    horses.append(pi) # store the strength of each horse into a list
horses.sort() # sort the list with horses with similar strengths together
closeStrenth = None
for i in range(n-1):
    difference = int(abs(horses[i] - horses[i+1])) # absolute and find the strength difference
    if closeStrenth is None:
        closeStrenth = difference
    elif difference < closeStrenth:
        closeStrenth = difference

print(closeStrenth) # find horses with similar strength to race
