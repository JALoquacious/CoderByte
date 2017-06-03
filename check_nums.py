#!/usr/bin/env python3

"""
Using the Python language, have the function CheckNums(num1,num2) take both
parameters being passed and return true if num2 is greater than num1, otherwise
return false. If the parameter values are equal to each other then return -1.
"""

def check_nums(num1, num2):
    if num1 == num2: return -1
    elif num1 < num2: return True
    else: return False

import unittest


class CheckNumsTests(unittest.TestCase):
    def test_check_nums(self):
        self.assertEqual(check_nums(3, 122), True)
        self.assertEqual(check_nums(67, 67), -1)
        self.assertEqual(check_nums(45, 39), False)
        self.assertEqual(check_nums(-114, 9834), True)
        
if __name__ == '__main__':
    unittest.main()
