#!/usr/bin/env python3

"""Using the Python language, have the function ABCheck(str) take the str
parameter being passed and return the string true if the characters a and b are
separated by exactly 3 places anywhere in the string at least once (ie. "lane
borrowed" would result in true because there is exactly three characters between
a and b). Otherwise return false."""

def ab_check(string):
    if len(string) < 4:
        return False
    string = "".join(string.lower().split())
    for idx in range(len(string)):
        if (string[idx] == "a" and string[idx+3] == "b"
        or  string[idx] == "b" and string[idx+3] == "a"):
            return True
    return False


import unittest

class ABCheckTests(unittest.TestCase):
    def test_ab_check(self):
        self.assertFalse(ab_check("after badly"))
        self.assertFalse(ab_check("ab"))
        self.assertTrue(ab_check("Laura sobs"))
        self.assertTrue(ab_check("b32a"))
        self.assertTrue(ab_check("lane borrowed"))

if __name__ == '__main__':
    unittest.main()
