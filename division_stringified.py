#!/usr/bin/env python3

"""
Using the Python language, have the function DivisionStringified(num1,num2)
take both parameters being passed, divide num1 by num2, and return the result
as a string with properly formatted commas. If an answer is only 3 digits long,
return the number with no commas (ie. 2 / 3 should output "1"). For example: if
num1 is 123456789 and num2 is 10000 the output should be "12,345".
"""

import math

def DivisionStringified(num1,num2):
    quot = math.ceil(num1 / num2)
    if quot < 4:
        return quot
    else:
        array = [x for x in str(quot)]
        for i in range(len(array)-3,0,-3):
            array.insert(i,",")
        n_quot = ''.join(array)
        return n_quot

print(DivisionStringified(123456789, 100)) # "1,234,568"
print(DivisionStringified(5000000000000,2)) # "2,500,000,000,000"
print(DivisionStringified(687413,67)) # "10,260"
print(DivisionStringified(2000,3)) # "667"
