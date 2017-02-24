import pygame as pg
import sys

from pygame.locals import *

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
walk_1 = pg.image.load('down_walk_1.png')
walk_2 = pg.image.load('down_walk_2.png')
walk_3 = pg.image.load('down_walk_3.png')
walk_4 = pg.image.load('down_walk_4.png')
wait = pg.image.load('wait.png')



felix = {
    'pos_y': int(winSize[1]/2),
    'pos_x': int(winSize[0]/2),
    'wait': wait,
    'walk_1': walk_1,
    'walk_2': walk_2,
    'walk_3': walk_3,
    'walk_4': walk_4,
    }

# --dictionary for the state machine
state = {'state':'wait', 'param':{}, 'image':'wait'}

speed = 10
while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()

    window.fill((255, 255, 255))

    if state['state'] is 'wait':
        # -- output
        state['image'] = 'wait'
        # -- transition
        if keys[K_DOWN]:
            state['state'] = 'walk'
            state['param'] = {'time':0}
    elif state['state'] is 'walk':
        # -- output
        t = state['param']['time']
        n = t%4 + 1
        state['image'] = 'walk_' + str(n)
        felix['pos_y'] += speed

        # -- transition
        if keys[K_DOWN]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    felix_rect = pg.Rect(felix['pos_x'], felix['pos_y'], 50, 50)
    image = state['image']
    window.blit(felix[image], felix_rect)
    
    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
