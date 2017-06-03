#!/usr/bin/env python3

"""
Using the Python language, have the function ExOh(str) take the str parameter
being passed and return the string true if there is an equal number of x's and
o's, otherwise return the string false. Only these two letters will be entered
in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo"
then the output should return false because there are 6 x's and 5 o's.
"""

def ExOh(string):
    x_counter = 0
    o_counter = 0
    for s in string.lower():
        if s == "x": x_counter += 1
        elif s == "o": o_counter += 1
        else: pass
    if x_counter == o_counter: return True
    else: return False
    
print(ExOh("XXXoxOOOxoOXoXxoXOOooxO")) # False (10x,13o)
print(ExOh("xxXOoo")) # True (3x,3o)
print(ExOh("ox")) # True (1x,1o)
