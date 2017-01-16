# The Descent - easy
'''This program shoots and destroys the highest mountain on the path as your starship descends'''

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# insertion sort is a function that sorts the elements according to value
def insertionSort(items):
    index = list(range(len(items))) # items = list "mountain_h", get the len, range, and list
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] > items[j-1]:
            # fire on the highest mountain by outputting its index
            items[j], items[j-1] = items[j-1], items[j]
            index[j], index[j-1] = index[j-1], index[j]
            j -= 1 # shoot the next highest
    return items, index


while 1:
    mountain_h = [] # list of mountain height
    for i in range(8): # 8 mountains, height of each one
        mountain_h.append(int(input()))  # add elements into the list mountain_h

    mountain_h, index = insertionSort(items = mountain_h)

    print(index[0]) # shoot the first element, which is the highest mountain
