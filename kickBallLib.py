'''
Projectile motion library
'''
import pygame
import random
import math

# -- definition of the config variables
background_color = (255,255,255)
(width, height) = (800, 650)

class Ball():
    '''
    creates a ball object
    '''


    def __init__(self, x, y, size, angle=math.pi/2, speed=0):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 165, 165)
        self.thickness = 5
        self.speed = speed
        self.angle = angle # -- going to the right by default

    def draw(self, screen):
        '''
        draws the ball on the screen
        :return:
        '''
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

    def move(self):
        '''
        move the ball given the angle and speed
        :return: None
        '''
        self.x += self.speed * math.sin(self.angle)
        self.y -= self.speed * math.cos(self.angle)

    def bounce(self, height, width):
        '''
        check for ball approacing the walls and bounce them
        :return: None
        '''
        '''
        if self.x < 280 and self.y < 190:
            self.y = 190

        if self.x > 280 and self.y > 190:
        '''    

        if 50 < self.x < 300:
            self.y = 190
            
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = -self.angle

        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = -self.angle

        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle



    def add_gravity(self, gravity):
        angle, speed = gravity
        self.angle, self.speed = addVectors(self.angle,self.speed, angle, speed)

    def experience_drag(self, drag=0.965):
        self.speed *= drag

def addVectors(angle1, length1, angle2, length2):
    '''return the sum of two vectors'''

    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y,x)
    length = math.hypot(x,y)
    return (angle, length)
