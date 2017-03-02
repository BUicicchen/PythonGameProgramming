import pygame as pg
import sys
from pygame.locals import *
import random
import math

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

def circle(x=10,y=10, size=15, color=(0,0,255), thickness=2, speed=0, angle=math.pi/2):
    return {'x':x,'y':y,'color':color,'size':size,'thickness':thickness,'speed':speed, 'angle':angle}

def newCircle(numOfCircles=10):
    circles = []
    for i in range(numOfCircles):
        x = random.randint(0, winSize[0]-1)
        y = random.randint(0, winSize[1]-1)
        size = int(random.randint(5, 60))
        speed = random.random()
        angle = random.uniform(0,math.pi*2)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        circles.append(circle(x=x,y=y,size=size,speed=speed, angle=angle, color=color))
    return circles

def drawCircle(window, circle):
    x = circle['x']
    y = circle['y']
    color = circle['color']
    size = circle['size']
    thickness = circle['thickness']
    pg.draw.circle(window, color, (int(x),int(y)), size, thickness)

def add_vectors(vector1, vector2):
    '''
    function to add two vectors
    :param: vector1: tuple (angle,mag)
    :param: vector2: tuple (angle,mag)
    return: vector: tuple angle,mag
    '''
    angle1, mag1 = vector1
    angle2, mag2 = vector2
    x=math.sin(angle1)*mag1+math.sin(angle2)*mag2
    x=math.cos(angle1)*mag1+math.cos(angle2)*mag2
    mag = math.hypot(x,y)
    angle = 0.5*math.pi - math.atan2(y,x)
    return angle, mag

def move(circle):
    angle = circle['angle']
    speed = circle['speed']
    circle['x'] += math.sin(angle) * speed
    circle['y'] -= math.cos(angle) * speed
    return circle

def bounce(circle):
    x = circle['x']
    y = circle['y']
    size = circle['size']
    angle = circle['angle']
    width = winSize[0]
    height = winSize[1]

    if x > width - size:
        x = 2*(width-size)-x
        angle = -angle
    elif x < size:
        x = 2*size-x
        angle = -angle
    if y > height-size:
        y = 2*(height-size)-y
        angle = math.pi - angle
    elif y<size:
        y = 2*size - y
        angle = math.pi - angle

    circle['x'] = x
    circle['y'] = y
    circle['angle'] = angle
    return circle
    
'''
def randomPlace():
    x = int(random.randint(0, winSize[0]-1)
    y = int(random.randint(0, winSize[1]-1)
    return x, y
circle_x, circle_y = randomPlace()
'''

Circles = newCircle(numOfCircles=10)

while True:
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    window.fill((255, 255, 255))

    # --- for each circle
    for i in range(len(Circles)):
        p = bounce(move(Circles[i]))
        drawCircle(window,p)
        # --- update the circles after moving
        Circles[i] = p


    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(50)
