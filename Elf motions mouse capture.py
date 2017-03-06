import pygame as pg
import sys
from pygame.locals import *
import math

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('walking machine')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# load images
wait = pg.image.load('wait.jpg')

# --dictionary for the state machine
state = {'state':'wait', 'param':{}, 'image':'wait'}

speed = 10
angle = math.pi/2

def elf(x=int(winSize[0]/2), y=int(winSize[1]/2), wait=pg.image.load('wait.jpg'),speed=0, angle=math.pi/2):
    return {'x': x, 'y': y, 'wait': wait, 'speed': speed, 'angle': angle}

def move(elf):
    angle = elf['angle']
    speed = elf['speed']
    elf['x'] += math.sin(angle) * speed
    elf['y'] -= math.cos(angle) * speed
    return elf

                 
elf = elf(x=int(winSize[0]/2), y=int(winSize[1]/2), wait=pg.image.load('wait.jpg'))

mouse_click = False

while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
        # --- Here the mouse x and y position is captured when the mouse left button is pressed
        elif event.type == pg.MOUSEBUTTONDOWN:
            # --- here the mouse's position is read
            (mouseX, mouseY) = pg.mouse.get_pos()
            mouse_click = True
        elif event.type == pg.MOUSEBUTTONUP:
            # --- if the button is released then clear flab
            mouse_click = False
            
    window.fill((255, 255, 255))

    if mouse_click:
        # --- Get the mouse position and move particle in that direction
        dx = mouseX - (elf['x'] + 10)
        dy = mouseY - (elf['y'] - 25)
        # --- dx, dy is where the particle should move to
        elf['angle'] = 0.5*math.pi + math.atan2(dy, dx)
        # --- constant speed
        elf['speed'] = 2.0

    elf = move(elf)
    elf_rect = pg.Rect(elf['x'], elf['y'], 50, 50)
    image = state['image']
    window.blit(elf[image], elf_rect)


    if elf['x'] > winSize[0]-75:
        elf['angle'] = -(0.5*math.pi + math.atan2(dy, dx))
    elif elf['x'] < 0-20:
        elf['angle'] = -(0.5*math.pi + math.atan2(dy, dx))
    elif elf['y'] < 0-10:
        elf['angle'] = math.pi-(0.5*math.pi + math.atan2(dy, dx))
    elif elf['y'] > winSize[1]-143:
        elf['angle'] = math.pi-(0.5*math.pi + math.atan2(dy, dx))

        
        


    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(40)
