import pygame
import particle_library as pl
import math
import random

# -- definition of congif variables
background_color = (255,255,255)
(width, height) = (1000, 400)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Particle simulator with OOP')

# -- number of particles
num_particles = 100
# -- particle info
min_size = 5
max_size = 10
gravity = (math.pi, 0.01)
# -- list to store particles
set_particles = list()

for i in range(num_particles):
    size = random.randint(min_size, max_size)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    angle = random.uniform(0, 2*math.pi)
    set_particles.append(pl.Particle(x=x, y=y, size=size, angle=angle))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    # -- draw the particles
    for par in set_particles:
        par.add_gravity(gravity=gravity)
        par.experience_drag(drag=0.999)
        par.move()
        par.bounce(height,width)
        par.draw(screen)

    pygame.display.flip()
