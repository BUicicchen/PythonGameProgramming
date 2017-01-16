# Mars Lander (episode 1) - easy
'''This program allows the "Mars Lander" shuttle to land safely'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while 1:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(j) for j in input().split()]

    x = 2500 # constant x at 2500m
    h_speed = 0 # no change in horizontal direction, or speed
    rotate = 0 # no rotation

    if y <= 100:
        if v_speed <= -32:
            print("0 4") # thrust power 0~4 wirhin verticle speed, within height

    if y > 100:
        if v_speed <= -32:
            print("0 4") # thrust power 0~4 wirhin verticle speed, above height
        else:
            print("0 3") # thrust power 0~3
