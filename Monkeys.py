'''
We have two monkeys, a and b, the parameters a_smile and b_smile indicate if each is smiling.
This program prints "We are in trouble" if they are both smiling or if neither of them is smiling, while in other conditions, we are fine.

'''
import sys
#reading arguments from the terminal
a_smile = sys.argv[1]
b_smile = sys.argv[2]

a_smile = input("Is monkey a smiling? (Yes/No) ")
if a_smile == "Yes":
    True
if a_smile == "No":
    False

b_smile = input("Is monkey b smiling? (Yes/No) ")
if b_smile == "Yes":
    True
if b_smile == "No":
    False

if a_smile == "Yes" and b_smile == "Yes" or a_smile == "No" and b_smile == "No":
    print("We are in trouble.")

if a_smile == "Yes" and b_smile == "No" or a_smile == "No" and b_smile == "Yes":
    print("We are fine.")
