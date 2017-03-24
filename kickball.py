'''
This program simulates a projectile motion
An elf kicks a ball off the apartment
The ball bounces
'''
import pygame as pg
import math
import sys
from pygame.locals import *
import kickBallLib as kbl
import random

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 650)
(width, height) = (800, 650)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('Projectile motion simulator')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()




# load images
house_original = pg.image.load('house.jpeg')
house = pg.transform.scale(house_original, (350,450))
wait = pg.image.load('wait.jpg')
right1 = pg.image.load('right1.jpg')
right2 = pg.image.load('right2.jpg')
right3 = pg.image.load('right3.jpg')
left1 = pg.image.load('left1.jpg')
left2 = pg.image.load('left2.jpg')
left3 = pg.image.load('left3.jpg')

# ----------- dictionary for the elf -----------
elf = {
    'pos_x': 65,
    'pos_y': 108,
    'wait': wait,
    'right1': right1,
    'right2': right2,
    'right3': right3,
    'left1': left1,
    'left2': left2,
    'left3': left3
    }
elf_speed = 6

#----------- dictionary for the state machine ------------
state = {'state':'wait', 'param':{}, 'image':'wait'}

#------------ set gravity ------------
gravity = (math.pi, 8)
# ball
num_ball = 1
set_ball = list()

#------------ set ball info ------------

size = 15
x = 150
y = 190
angle = math.pi/2
speed = 0
ball= kbl.Ball(x=x, y=y, size=size, angle=angle, speed=speed)



running = True
while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False



    #------------ fills the window with white background color ------------
    window.fill((255, 255, 255))

    #------------- print directions --------------
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pg.font.SysFont("ariel", 35)
    smallfont = pg.font.SysFont("comicsansms", 20)
    # render text
    label = myfont.render("Projectile motion simulator", 3, (0,0,125))
    equation_displacement = smallfont.render("displacement = vi*t + 1/2*a*t^2", 1, (255,0,255))
    equation_finalVelocity = smallfont.render("final velocity = vi + a*t", 1, (255,0,255))
    direction = myfont.render("The elf kicks the ball", 1, (0,0,255))
    


    window.blit(label, (450, 50))
    print(label)
    window.blit(direction, (450, 90))
    print(direction)
    window.blit(equation_displacement, (450, 130))
    print(equation_displacement)
    window.blit(equation_finalVelocity, (450, 150))
    print(equation_finalVelocity)

    
    #-------------- prints the house --------------
    window.blit(house, (10,200))

    #-------------- control the elf's motion --------------
    keys = pg.key.get_pressed()

    if state['state'] is 'wait':
        # -- output
        state['image'] = 'wait'
        # -- transition
        if keys[K_RIGHT]:
            state['state'] = 'right'
            state['param'] = {'time':0}
        # -- transition
        elif keys[K_LEFT]:
            state['state'] = 'left'
            state['param'] = {'time':0}

    # elf walks to the right
    elif state['state'] is 'right':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'right' + str(n)
        if elf['pos_x'] < 240:
            elf['pos_x'] += elf_speed
        # -- transition
        if keys[K_RIGHT]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    # elf walks to the left
    elif state['state'] is 'left':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'left' + str(n)
        if elf['pos_x'] > 75:
            elf['pos_x'] -= elf_speed
        # -- transition
        if keys[K_LEFT]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    # draws elf
    elf_rect = pg.Rect(elf['pos_x'], elf['pos_y'], 50, 50)
    image = state['image']
    window.blit(elf[image], elf_rect)

    #--------------- ball's motion ---------------
    #ball = kbl.Ball(x, y, size, angle, speed)


    #----------- distance of collide -----------
    distance = math.fabs(ball.x - elf['pos_x'])

    if distance < ball.size+42:
        ball.speed = 40
        ball.angle = math.pi/2
        
    ball.add_gravity(gravity=gravity)
    ball.experience_drag(drag=0.91)
    ball.move()
    ball.bounce(height,width)
    ball.draw(window)

    
    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()


    # --- Limit to 60 frames per second
    clock.tick(8)
