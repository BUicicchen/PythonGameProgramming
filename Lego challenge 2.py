'''This program categorize legos into beams and bricks by plotting them length by weight
on a graph and calculate the distance each lego is to the "standard" lego coordinate.'''


# library for scientific computations
import numpy as np
#library for graphs
import matplotlib.pyplot as plt
#%matplotlib inline

# read tetx file
legos = np.loadtxt("/Users/icicchen/Desktop/PythonGameProgramming/Homework/Quarter1/Legos2.txt",delimiter=',')

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



# find the distance on the graph of the points, check closer to which center

beam = 0
brick = 0

for x, y in legos:
    range_positive_x = 0.5
    range_negative_x = -0.5
    range_positive_y = 0.5
    range_negative_y = -0.5



    if x <= range_positive_x and x >= range_negative_x and y <= range_positive_y and y >= range_negative_y:
        beam += 1
        plt.scatter(x,y,color='red')

    else:
        brick += 1
        plt.scatter(x,y,color='blue')


print("Number of beams: ", beam)
print("Number of bricks: ", brick)
