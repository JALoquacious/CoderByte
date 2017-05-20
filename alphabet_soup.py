#!/usr/bin/env python3

"""Using the Python language, have the function AlphabetSoup(str) take the str
string parameter being passed and return the string with the letters in
alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation
symbols will not be included in the string."""

def alphabet_soup(string):
    result = ""
    array = [s for s in string]
    length = len(array)
    while length > 0:
        #print(array, result) #debug
        result += min(array)
        array.remove(min(array))
        length -= 1
    return result

import unittest

class AlphabetSoupTests(unittest.TestCase):
    def test_alphabet_soup(self):
        self.assertEqual(alphabet_soup("coderbyte"), "bcdeeorty")
        self.assertEqual(alphabet_soup("hooplah"), "ahhloop")
        self.assertEqual(alphabet_soup("python"), "hnopty")
        self.assertEqual(alphabet_soup("alphabet"), "aabehlpt")
        self.assertEqual(alphabet_soup("supercalifragilistic"), "aaccefgiiiillprrsstu")
        
if __name__ == '__main__':
    unittest.main()
