import pygame
import solarSystemLib as pl
import math
import random



# -- definition of congif variables
background_color = (0,0,0)
(width, height) = (1000, 400)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Particle simulator with OOP')

# -- number of particles
num_particles = 100
# -- particle info
min_mass = 1
max_mass = 5
# gravity = (math.pi, 0.01)
# -- list to store particles
set_particles = list()

for i in range(num_particles):
    mass = min_mass + 0.5 * max_mass * random.random()
    # -- calculate the size
    size = pl.calculateSize(mass)

    x = random.randint(0, width)
    y = random.randint(0, height)
    angle = random.uniform(0, 2*math.pi)
    set_particles.append(pl.Particle(x=x, y=y, size=size, angle=angle, speed=0.0, mass=mass, color=(255,255,255)))


clock = pygame.time.Clock()
running = True
particle_to_remove = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for i, p1 in enumerate(set_particles):
        for p2 in set_particles[i+1:]:
            if p1.attract(p2):
                pl.collide(p1,p2)


        if p1.size > 5:
            # -- yellow for suns
            p1.color = (255, 255, 0)

        if 'collided_with' in pl.__dict__:
            particle_to_remove.append(p1.collide_with)
            p1.size = pl.calculateSize(p1.mass)
            del pl.__dict__['collided_with']
    # -- draw the particles

        p1.experience_drag(drag=0.9)
        p1.move()
        p1.bounce(height,width)
        p1.draw(screen)

    for p in particle_to_remove:
        if p in set_particles:
            set_particles.remove(p)

    #for par in set_particles:
        #par.add_gravity(gravity=gravity)
        #par.experience_drag(drag=0.999)
        #par.move()
        #par.bounce(height,width)
        #par.draw(screen)

    pygame.display.flip()
    clock.tick(5)
