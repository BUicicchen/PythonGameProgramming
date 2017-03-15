import pygame
import random
import math

# -- definition of the config variables
backgroun_color = (255,255,255)
(width, height) = (1000, 400)

class Particle():
    '''
    creates a particle object
    '''

    num_particles = 0

    def __init__(self, x, y, size, color=(255,255,255), angle=math.pi/2, speed=1, mass=1.0):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.thickness = 0
        self.speed = speed
        self.angle = angle # -- going to the right by default
        self.mass = mass # -- mass of object
        Particle.num_particles += 1

    def attract(self, other):
        '''
            gravitational force
        :param other: another particle to whom we attract
        :return:
        '''
        dx = (self.x-other.x)
        dy = (self.y-other.y)
        distance = ((self.x-other.x)**2 + (self.y-other.y)**2) ** 0.5
        force = 0.2*self.mass * other.mass / (distance ** 2)

        #check for colliding particles
        if distance < self.size + other.size:
            return True

        # -- angle
        angle = math.atan2(dy,dx)
        speed = force
        # -- we use Newton's Law
        self.accelerate(angle - math.pi/2 , force/self.mass)
        other.accelerate(angle + math.pi/2 , force/other.mass)

    def accelerate(self, angle, speed):
        '''
        accelerates the particle by the given angle and speed
        :param angle:
        :param speed:
        :return:
        '''
        self.angle, self.speed = addVectors(self.angle,self.speed, angle, speed)

    def draw(self, screen):
        '''
        draws the particle on the screen
        :return:
        '''
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.x), int(self.y)),
                           int(self.size),
                           self.thickness)

    def move(self):
        '''
        move the particle given the angle and speed
        :return: None
        '''
        self.x += self.speed * math.sin(self.angle)
        self.y -= self.speed * math.cos(self.angle)

    def bounce(self, height, width):
        '''
        check for particles approacing the walls and bounce them
        :return: None
        '''
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

    def experience_drag(self, drag=0.9):
        self.speed *= drag

def addVectors(angle1, length1, angle2, length2):
    '''return the sum of two vectors'''

    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y,x)
    length = math.hypot(x,y)
    return (angle, length)

def collide(p1, p2):
    '''
    combines two colliding particles into one bigger particle
    :param p1:
    :param p2:
    :return:
    '''
    total_mass = p1.mass + p2.mass
    total_size = p1.size + p2.size
    # -- position of the new particle
    p1.x = (p1.x * p1.mass + p2.x * p2.mass) / total_mass
    p1.y = (p1.y * p1.mass + p2.y * p2.mass) / total_mass
    # --
    (angle, speed) = addVectors(p1.angle, p1.speed*p1.mass / total_mass,
                                p2.angle, p2.speed*p2.mass / total_mass)
    p1.speed = speed
    p1.angle = angle
    p1.mass = total_mass
    p1.size = total_size
    p1.collided_with = p2

def calculateSize(mass):
    '''
        calculates the size of the particle given its mass
    :param mass:
    :return:
    '''
    return 0.5 * mass ** (0.5)
