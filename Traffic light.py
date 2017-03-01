import pygame as pg
import sys
from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('Traffic light')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

off_light = pg.image.load('off_light.png')
red_light = pg.image.load('red_light.png')
yellow_light = pg.image.load('yellow_light.png')
green_light = pg.image.load('green_light.png')

traffic = {'off':off_light,
           'red':red_light,
           'yellow':yellow_light,
           'green':green_light,
           'pos_x':80,
           'pos_y':0}
state = {'state':'off', 'count':0}

while True:
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    window.fill((255,255,255))

    if keys[pg.K_SPACE]:
        state['state'] = 'red' if state['state'] is 'off' else 'off'

    if state['state'] is 'off':
        offState = pg.Rect(traffic['pos_x'], traffic['pos_y'], 50, 50)
        window.blit(traffic['off'], offState)

    elif state['state'] is 'red':
        redState = pg.Rect(traffic['pos_x'], traffic['pos_y'], 50, 50)
        window.blit(traffic['red'], redState)
        state['count'] += 1
        if state['count'] >= 60:
            state['state'] = 'green'
            state['count'] = 0
        else:
            state['state'] = 'red'

    elif state['state'] is 'green':
        greenState = pg.Rect(traffic['pos_x'], traffic['pos_y'], 50, 50)
        window.blit(traffic['green'], greenState)
        state['count'] += 1
        if state['count'] >= 60:
            state['state'] = 'yellow'
            state['count'] = 0
        else:
            state['state'] = 'green'

    elif state['state'] is 'yellow':
        yellowState = pg.Rect(traffic['pos_x'], traffic['pos_y'], 50, 50)
        window.blit(traffic['yellow'], yellowState)
        state['count'] += 1
        if state['count'] >= 10:
            state['state'] = 'red'
            state['count'] = 0
        else:
            state['state'] = 'yellow'        


    pg.display.flip()
    clock.tick(10)
