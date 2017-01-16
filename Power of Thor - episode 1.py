# Power of Thor - easy
'''This program allows Thor to reach the light of power by giving it directions'''

import sys
import math


# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thor_x = initial_tx
thor_y = initial_ty


while 1:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move

    # direction the Thor should take
    direction = ""

    if light_y < thor_y and light_x > thor_x:
        # if the Thor locates south and west of the light of power, go down and right will go northeast
        thor_y -= 1
        thor_x += 1
        direction = "NE"

    elif light_y < thor_y and light_x < thor_x:
        # if the Thor locates south and east of the light of power, go up and left will go northwest
        thor_y += 1
        thor_x -= 1
        direction = "NW"

    elif light_y > thor_y and light_x > thor_x:
        # if the Thor locates north and east of the light of power, go down and right will go southeast
        thor_y += 1
        thor_x += 1
        direction = "SE"

    elif light_y > thor_y and light_x < thor_x:
        # if the Thor locates north and west of the light of power, go down and left will go southwest
        thor_y += 1
        thor_x -= 1
        direction = "SW"

    elif light_x < thor_x:
        # if the Thor locates east of the light of power, go left will go west
        thor_x += 1
        direction = "W"

    elif light_x > thor_x:
        # if the Thor locates west of the light of power, go right will go east
        thor_x -= 1
        direction = "E"

    elif light_y < thor_y:
        # if the Thor locates south of the light of power, go up will go north
        thor_y -= 1
        direction = "N"

    elif light_y > thor_y:
        # if the Thor locates north of the light of power, go down will go south
        thor_y += 1
        direction = "S"


    print(direction)
