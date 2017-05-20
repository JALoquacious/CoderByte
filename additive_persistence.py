"""Using the Python language, have the function AdditivePersistence(num) take
the num parameter being passed which will always be a positive integer and
return its additive persistence which is the number of times you must add the
digits in num until you reach a single digit. For example: if num is 2718 then
your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you
stop at 9."""

def additive_persistence(num):
    counter = 0
    while len(integer_list(num)) > 1:
        num = sum([int(n) for n in str(num)])
        counter += 1
    return counter


import unittest

class AdditivePersistenceTests(unittest.TestCase):
    def test_additive_persistence(self):
        self.assertEqual(additive_persistence(999999999999999999999), 3)
        self.assertEqual(additive_persistence(19), 2)
        self.assertEqual(additive_persistence(2718), 2)
        self.assertEqual(additive_persistence(313), 1)
        self.assertEqual(additive_persistence(4), 0)
        
if __name__ == '__main__':
    unittest.main()
