#!/usr/bin/env python3

"""
Using the Python language, have the function ExOh(str) take the str parameter
being passed and return the string true if there is an equal number of x's and
o's, otherwise return the string false. Only these two letters will be entered
in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo"
then the output should return false because there are 6 x's and 5 o's.
"""

def ex_oh(string):
    x_counter = 0
    o_counter = 0
    for s in string.lower():
        if s == "x": x_counter += 1
        elif s == "o": o_counter += 1
        else: pass
    if x_counter == o_counter: return True
    else: return False
    

import unittest

class ExOhTests(unittest.TestCase):
    def test_ex_oh(self):
        self.assertEqual(ex_oh("XXXoxOOOxoOXoXxoXOOooxO"), False)
        self.assertEqual(ex_oh("xxXOoo"), True)
        self.assertEqual(ex_oh("ox"), True)
        self.assertEqual(ex_oh("XXxxOoooO"), False)
        
if __name__ == '__main__':
    unittest.main()
