#!/usr/bin/env python3

"""
Using the Python language, have the function DashInsert(str) insert dashes ('-')
between each two odd numbers in str. For example: if str is 454793 the output
should be 4547-9-3. Don't count zero as an odd number.
"""

def DashInsert(num):
    n_str = ""
    array = [int(n) for n in str(num)]
    for i in range(len(array)-1):
        if array[i] % 2 != 0 and array[i+1] % 2 != 0:
            n_str += str(array[i]) + "-"
        else: n_str += str(array[i])
    n_str += str(array[-1])
    return n_str

print(DashInsert(99946)) # 9-9-946
print(DashInsert(56730)) # 567-30
print(DashInsert(454793)) # 4547-9-3
