#!/usr/bin/env python3

"""
Using the Python language, have the function LetterChanges(string) take
the string parameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
(a, e, i, o, u) and finally return this modified string.
"""

test_str = "hello*3"

def LetterChanges(o_str):
    n_str = ""
    dct = {}
    abc = "abcdefghijklmnopqrstuvwxyza"
    vowels = "aeiou"

    for char in o_str:
        if char in abc and char in vowels:
            n_str += abc[abc.index(char)+1].upper()
        elif char in abc:
           n_str += abc[abc.index(char)+1]
        else:
            n_str += char
    return n_str

print(LetterChanges(test_str))
