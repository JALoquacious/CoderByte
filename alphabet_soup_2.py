#!/usr/bin/env python3

"""Using the Python language, have the function AlphabetSoup(str) take the str
string parameter being passed and return the string with the letters in
alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation
symbols will not be included in the string."""

def AlphabetSoup(string):
    return ''.join(sorted([s for s in string]))

print(AlphabetSoup("coderbyte")) #"bcdeeorty"
print(AlphabetSoup("hooplah")) #"ahhloop"
print(AlphabetSoup("python")) #"hnopty"
