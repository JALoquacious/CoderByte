#!/usr/bin/env python3

"""
Using the Python language, have the function CheckNums(num1,num2) take both
parameters being passed and return true if num2 is greater than num1, otherwise
return false. If the parameter values are equal to each other then return -1.
"""

def CheckNums(num1, num2):
    if num1 == num2: return -1
    elif num1 < num2: return True
    else: return False

print(CheckNums(3, 122)) # True
print(CheckNums(67, 67)) # -1
print(CheckNums(45, 39)) # False
