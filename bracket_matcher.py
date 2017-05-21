#!/usr/bin/env python3

"""Using the Python language, have the function BracketMatcher(str) take the str
parameter being passed and return 1 if the brackets are correctly matched and
each one is accounted for. Otherwise return 0. For example: if str is "(hello
(world))", then the output should be 1, but if str is "((hello (world))" the
output should be 0 because the brackets do not correctly match up. Only "(" and
")" will be used as brackets. If str contains no brackets return 1. """

def bracket_matcher(string):
    L, R = 0, 0
    for s in string:
        if R and not L:
            return 0
        if s == "(":
            L += 1
        elif s == ")":
            R += 1
    return 1 if L == R else 0


import unittest

class AlphabetSoupTests(unittest.TestCase):
    def test_alphabet_soup(self):
        self.assertEqual(bracket_matcher(")((coder)(byte)"), 0)
        self.assertEqual(bracket_matcher("(c(oder)) b(yte)"), 1)
        self.assertEqual(bracket_matcher("((hello (world))"), 0)
        self.assertEqual(bracket_matcher("((hello)) ((world))"), 1)
        
if __name__ == '__main__':
    unittest.main()
