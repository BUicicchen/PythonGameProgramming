'''This program displays a line of text in ASCII art in a style you are given as input'''

import sys

l = int(input()) # length of letter
h = int(input()) # height of letter
t = input() # text
data = [] # storing letters of #

for i in range(h):
    data.append(input()) # insert text into list data


output = [] # final list
t = t.lower() # make text into lower case

for letter in t:
    for i in range(h):
        if letter > 'z' or letter < 'a': # outside of range of alphabet
            letter = chr(ord('z') + 1) # order in ASCII code, find the string of the character

        if len(output) <= i:
            output.append('') # append into string
        index = (ord(letter) - ord('a')) * l # get location
        output[i] += data[i][index: index + l] # put into output list

for word in output: # get the word in string
    print(word) # print word
