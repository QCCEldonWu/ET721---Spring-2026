"""
Eldon Wu
lab 9, unit testing
Feb 28, 2026
"""
import unittest
from calculation import * 

def addtwonumbers(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(addtwonumbers(1, 2), 3) 

    def test_subtraction(self):
        self.assertEqual(subtracttwonumbers(6, 4), 2)
        self.assertEqual(subtracttwonumbers(4, 6), -2)
        self.assertEqual(subtracttwonumbers(5), 5)
        self.assertEqual(subtracttwonumbers(), 0)

    def test_multiplication(self):
        self.assertEqual(multiplythreenumbers(1, 2, 3), 6)
        self.assertEqual(multiplythreenumbers(1, -2, -3), 6)
        self.assertEqual(multiplythreenumbers(-1, -2, -3), -6)

    def test_division(self):
        self.assertEqual(dividetwonumbers(6, 3), 2)
        self.assertAlmostEqual(dividetwonumbers(10, 3), 3.3333, places=3)

    def test_divisionbyzero(self):
        self.assertIsNone(dividetwonumbers(10, 0))
        self.assertIsNone(dividetwonumbers(10, "a"))  
        self.assertIsNone(dividetwonumbers("peter", 2)) 

    def test_unexpected_exception(self):
        with self.assertRaises(Exception):
            dividetwonumbers()

if __name__ == "__main__":
    unittest.main()