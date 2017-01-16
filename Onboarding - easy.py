# Onboarding - easy
'''This program shoots the closest enemy ships by comparing distances between the ship and mine.
CodinGame planet is being attacked by slimy insectoid aliens.'''

import sys
import math


while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2


    if dist_1 < dist_2: #compare the distance, if enemy 1 is closer
        print(enemy_1) #shoot enemy 1
    else:
        print(enemy_2) #if enemy 2 is closer, shoot enemy 2
