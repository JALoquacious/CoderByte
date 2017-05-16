#!/usr/bin/env python3

"""Using the Python language, have the function ABCheck(str) take the str
parameter being passed and return the string true if the characters a and b are
separated by exactly 3 places anywhere in the string at least once (ie. "lane
borrowed" would result in true because there is exactly three characters between
a and b). Otherwise return the string false."""

def ABCheck(string):
    string = "".join(string.lower().split())
    for idx,val in enumerate(string):
        #print(idx,":",val) # debug
        if val == "a" and string[idx+3] == "b":
            return True
        elif val == "b" and string[idx+3] == "a":
            return True
    else: return False

print(ABCheck("after badly")) #False
print(ABCheck("Laura sobs")) #True
print(ABCheck("b32a")) #True
