#!/usr/bin/env python3

"""
Using the Python language, have the function ArithGeo(arr) take the array of
numbers stored in arr and return the string "Arithmetic" if the sequence follows
an arithmetic pattern or return "Geometric" if it follows a geometric pattern.
If the sequence doesn't follow either pattern return -1. An arithmetic sequence
is one where the difference between each of the numbers is consistent, where as
in a geometric sequence, each term after the first is multiplied by some
constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric
example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will
not be entered, and no array will contain all the same elements.
"""

def arith_geo(array):
    difference = abs(array[1] - array[0])
    ratio = array[1] / array[0]
    if abs(array[-1] - array[-2]) == difference:
        return "Arithmetic"
    elif array[-1] / array[-2] == ratio:
        return "Geometric"
    else: return -1


import unittest

class AlphabetSoupTests(unittest.TestCase):
    def test_alphabet_soup(self):
        self.assertEqual(arith_geo([-9,-13,-17,-21]), "Arithmetic")
        self.assertEqual(arith_geo([2,9,15,33]), -1)
        self.assertEqual(arith_geo([2,4,8,16,32,64]), "Geometric")
        self.assertEqual(arith_geo([1,1,1,1,1,1,1]), "Arithmetic")
        #(either geometric or arithmatic would be correct)
        
if __name__ == '__main__':
    unittest.main()
