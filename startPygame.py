'''
This is a program for creating the snake game
'''

import pygame as pg
import sys
from pygame.locals import *
import random

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (400, 300)
window = pg.display.set_mode(winSize)
cellSize = 20
# title
pg.display.set_caption('Snake game')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()
# Set start point.
wormCoords = [{'x': 5, 'y': 5},
              {'x': 5, 'y': 4},
              {'x': 5, 'y': 3}]

direction = 'right'



def drawGrid(win, winSize, cellSize, color):
    """
    Draws the grid for the game
    :param win: identifier of the window
    :param winSize: winSize (width,height)
    :param cellSize: size of one cell on the grid
    :param color: the color of the background and grid
    :return: None
    """
    for x in range(0, winSize[0], cellSize):  # draw vertical lines
        pg.draw.line(win, color, (x, 0), (x, winSize[1]))
    for y in range(0, winSize[1], cellSize):  # draw horizontal lines
        pg.draw.line(win, color, (winSize[0], y), (0, y))


def drawWorm(win, wormCoords, cellSize, wormColor):
    '''
    :param win: identifier of the window
    :param wormCoords: the coordinates for the worm
    :param cellSize: size of one cell on the grid
    :param wormColor: the color of the worm's head and body
    :return: None
    '''
    for i, c in enumerate(wormCoords):
        x = c['x'] * cellSize
        y = c['y'] * cellSize
        wormSegmentRect = pg.Rect(x, y, cellSize, cellSize)
        # change color of head
        color = wormColor
        if i is 0:
            color = (0, 0, 0)
        pg.draw.rect(win, color, wormSegmentRect)

def drawFood(window, foodSize, foodColor, x, y):
    """
    Draws the food that snake will eat
    :param window: identifier of the window
    :param foodSize: foodSize (width,height)
    :param foodColor: color of food
    :param x: food's x coordinate
    :param y: food's y coordinate
    """
    foodRect = pg.Rect(x, y, foodSize, foodSize)
    pg.draw.rect(window, foodColor, foodRect)


def randomPlace():
    """
    Generate random coordinate for the food
    :return: x, y coordinates
    """
    x = int(random.randint(0, winSize[0]-1) / cellSize)*cellSize
    y = int(random.randint(0, winSize[1]-1) / cellSize)*cellSize
    return x, y
food_x, food_y = randomPlace()


instructions = True
startGame = True
endGame = True

# upload the start and end screens
start_image = pg.image.load('start_image.jpg')
end_image = pg.image.load('end_image.jpg')

while instructions: # give instructions
    window.fill((0,0,0))
    window.blit(start_image, (0,0))
    pg.display.flip()
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type is keys[pg.K_LEFT]:
            instructions = False
        elif event.type is QUIT:
            pg.quit()
            sys.exit()

while startGame:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    # worm's directions
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and direction is not 'right':
        direction = 'left'
    if keys[pg.K_RIGHT] and direction is not 'left':
        direction = 'right'
    if keys[pg.K_UP] and direction is not 'down':
        direction = 'up'
    if keys[pg.K_DOWN] and direction is not 'up':
        direction = 'down'

    # worm turns when it touches the wall
    if direction is 'up' and wormCoords[0]['y'] == 0:
        direction = 'right'
    if direction is 'down' and wormCoords[0]['y'] == winSize[1] / cellSize - 1:
            direction = 'left'
    if direction is 'left' and wormCoords[0]['x'] == 0:
            direction = 'up'
    if direction is 'right' and wormCoords[0]['x'] == winSize[0] / cellSize - 1:
        direction = 'down'

    if direction is 'up':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] - 1}
    elif direction is 'down':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] + 1}
    elif direction is 'left':
        newHead = {'x': wormCoords[0]['x'] - 1, 'y': wormCoords[0]['y']}
    else:
        newHead = {'x': wormCoords[0]['x'] + 1, 'y': wormCoords[0]['y']}


    wormCoords.insert(0, newHead)

    window.fill((255, 255, 255))
    drawGrid(window, winSize, cellSize, (40, 40, 40))
    drawWorm(window, wormCoords, cellSize, (0, 255, 255))
    drawFood(window, cellSize, (255,255,0), food_x, food_y)

    # if the snake touches the coordinate the food is located, add body
    if newHead['x'] * 20 == food_x or newHead['y'] * 20 == food_y:
        food_x, food_y = randomPlace()
        wormCoords.insert(0, newHead)
    # if not, remove worm's tail segment
    else:
        del wormCoords[-1]
        wormCoords.insert(0, newHead)

    # restrictions
    # can't touch wall
    if newHead['x'] < 0:
        startGame = False
    elif newHead['x'] > winSize[0] / cellSize -1 or newHead['y']>winSize[1]/cellSize-1:
        startGame = False
    # can't touch body
    for i, j in enumerate(wormCoords):
        if i != 0:
            if newHead == j:
                startGame = False

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(5)

while endGame: # game over
    window.fill((0,0,0))
    window.blit(end_image, (0,0))
    pg.display.flip()
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type is keys[pg.K_LEFT]:
            endGame = False
        elif event.type is QUIT:
            pg.quit()
            sys.exit()
