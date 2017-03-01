import pygame as pg
import sys
from pygame.locals import *
import random

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('Random Circle Motions')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

numOfCircles = 10
circle = {'x':100,
          'y':100,
          'color':(0,0,0),
          'radius':10,
          'thickness':1}

def newCircle():
    x = int(random.randint(0, winSize[0]-1))
    y = int(random.randint(0, winSize[1]-1))
    radius = int(random.randint(1, 50))
    thickness = 1
    circle['x'] = x
    circle['y'] = y
    circle['radius'] = radius
    circle['thickness'] = thickness
    return circle

def drawCircle(window, circle):
    x = circle['x']
    y = circle['y']
    color = circle['color']
    radius = circle['radius']
    thickness = circle['thickness']
    pg.draw.circle(window, (0,0,0), (x,y), radius, thickness)

'''
def randomPlace():
    x = int(random.randint(0, winSize[0]-1)
    y = int(random.randint(0, winSize[1]-1)
    return x, y
circle_x, circle_y = randomPlace()
'''
while True:
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
            
    window.fill((255, 255, 255))
    for i in range(10):
        newCircle()
        drawCircle(window, circle)

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(5)
