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
wait = pg.image.load('wait.jpg')
forward1 = pg.image.load('forward1.jpg')
forward2 = pg.image.load('forward2.jpg')
forward3 = pg.image.load('forward3.jpg')
right1 = pg.image.load('right1.jpg')
right2 = pg.image.load('right2.jpg')
right3 = pg.image.load('right3.jpg')
left1 = pg.image.load('left1.jpg')
left2 = pg.image.load('left2.jpg')
left3 = pg.image.load('left3.jpg')
back1 = pg.image.load('back1.jpg')
back2 = pg.image.load('back2.jpg')
back3 = pg.image.load('back3.jpg')


elf = {
    'pos_y': int(winSize[1]/2),
    'pos_x': int(winSize[0]/2),
    'wait': wait,
    'forward1': forward1,
    'forward2': forward2,
    'forward3': forward3,
    'right1': right1,
    'right2': right2,
    'right3': right3,
    'left1': left1,
    'left2': left2,
    'left3': left3,
    'back1': back1,
    'back2': back2,
    'back3': back3,

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
            state['state'] = 'forward'
            state['param'] = {'time':0}
        if keys[K_RIGHT]:
            state['state'] = 'right'
            state['param'] = {'time':0}            
        if keys[K_LEFT]:
            state['state'] = 'left'
            state['param'] = {'time':0}  
        if keys[K_UP]:
            state['state'] = 'back'
            state['param'] = {'time':0}  

    elif state['state'] is 'forward':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'forward' + str(n)
        elf['pos_y'] += speed

        # -- transition
        if keys[K_DOWN]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'right':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'right' + str(n)
        elf['pos_x'] += speed

        # -- transition
        if keys[K_RIGHT]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'left':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'left' + str(n)
        elf['pos_x'] -= speed

        # -- transition
        if keys[K_LEFT]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'back':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'back' + str(n)
        elf['pos_y'] -= speed

        # -- transition
        if keys[K_UP]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elf_rect = pg.Rect(elf['pos_x'], elf['pos_y'], 50, 50)
    image = state['image']
    window.blit(elf[image], elf_rect)
    
    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
