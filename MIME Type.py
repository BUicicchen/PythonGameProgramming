# MIME Type - easy
'''This program that detects the MIME type of a file based on its name'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mimeDic = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimeDic[ext.lower()] = mt # make into lowercase

for i in range(q):
    fname = input()  # One file name per line.
    fnameList = fname.split(".") # split into lines

    if len(fnameList) == 1:
        print("UNKNOWN") # if there is no corresponding MIME type, then display UNKNOWN

    elif len(fnameList) != 1:
        # For each of the Q filenames, display on a line the corresponding MIME type.
        ext = fname[-1]
        print(mimeDic.get(fnameList[-1].lower(), "UNKNOWN"))
