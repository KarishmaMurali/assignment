'''unit testing'''
import unittest
from src.radpkg import radian

class Testrngg(unittest.TestCase):
    '''write test cases'''
    def test1_rad(self):
        '''check for zero'''
        self.assertEqual(radian.rad(0), 0)

    def test2_rad(self):
        '''check for positive integers'''
        self.assertEqual(radian.rad(1), 0.017453292519943295)

    def test3_rad(self):
        '''check for negative integers'''
        self.assertEqual(radian.rad(-1), -0.017453292519943295)

    def test4_rad(self):
        '''check for positive float '''
        self.assertAlmostEqual(radian.rad(2.5), 0.04363323129985824)

    def test5_rad(self):
        '''check for negative float'''
        self.assertEqual(radian.rad(-4.5), -0.07853981633974483)

    def test6_rad(self):
        '''check for exception'''
        self.assertEqual(radian.rad("abc"), "Enter a number")

if __name__ == "__main__":
    unittest.main()
