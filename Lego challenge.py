'''This program categorize legos into beams and bricks by plotting them length by weight
on a graph and calculate the distance each lego is to the "standard" lego coordinate.'''


# library for scientific computations
import numpy as np
#library for graphs
import matplotlib.pyplot as plt
#%matplotlib inline

# read tetx file
legos = np.loadtxt("/Users/icicchen/Desktop/PythonGameProgramming/Homework/Quarter 1/Legos.txt",delimiter=',')

# show the number of elements in legos
len(legos)

# show the dimensions of legos (# of rows, # columns)
np.shape(legos)

# show every pair of points
for x, y in legos:
    print(x,y)

# print each pair of points in a scatter plot
for x, y in legos:
    plt.scatter(x,y,color='gray')

plt.show()

def distance(beam_x1, brick_x1, x, beam_y1, brick_y1, y):
    return np.sqrt((x - beam_x1)**2 + (y - beam_y1)**2), np.sqrt((x - brick_x1)**2 + (y - brick_y1)**2)


# find the distance on the graph of the points, check closer to which center

beam = 0
brick = 0
for x, y in legos:
    beam_x1 = 7
    beam_y1 = 4
    brick_x1 = 3
    brick_y1 = 5

    db, dbr = distance(beam_x1, brick_x1, x, beam_y1, brick_y1, y)

    # distance_beam_x = x - beam_x1
    # distance_beam_y = y - beam_y1
    #
    # distance_brick_x = x - brick_x1
    # distance_brick_y = y - brick_y1
    #
    # distance_beam = (beam_x1, x, beam_y1, y)
    # distance_brick = (brick_x1, x, brick_y1, y)
    #
    #

    if db> dbr:
        beam += 1
        plt.scatter(x,y,color='red')

    else:
        brick += 1
        plt.scatter(x,y,color='blue')


print(beam)
print(brick)
