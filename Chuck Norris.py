# Chuck Norris - easy
'''This program takes an incoming message as input and displays output message encoded using Chuck Norris’ method'''

import sys
import math

message = input() # message consisting of ASCII characters
binaryMessage = []
output = "" # binary code printed, the encoding message

for i in message:
    # convert the character C into binary code 1000011
    binaryMessage.append("{0:07b}".format(ord(i)))

prior = "" # prior character
times = 0 # how many times the blocks repeats
for character in "".join(binaryMessage):
    if character == prior: # if character is the same
        times += 1 # repeat the blocks

    if character != prior: # if character isn't repeating
        for i in range(times):
            output += "0" # print blocks of 0s

        if times > 0: # more than 1 block
            output += " " # separate by space

        if character == "1": # contains 1 in series
            output += "0 "
        if character == "0": # 0 value in series
            output += "00 "
        times = 1 # print blocks 1 time

    prior = character # last character = character

output += "0" * times # repeat the block how many times the character appears

print(output)
