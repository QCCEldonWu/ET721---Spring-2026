"""
Eldon Wu
lab 9, unit testing
feb 28 2026
"""
import unittest
from employee import * 

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee("Peter", "Pan", 80000)

    def test_emailemployee(self):
        self.assertEqual(self.employee1.emailemployee, "Peter_Pan@email.com")
        self.employee1.first = "Will"
        self.assertEqual(self.employee1.emailemployee, "Will_Pan@email.com")

    def test_apply_raise(self):
        self.assertEqual(self.employee1.salary, 80000) 
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.salary, 84000)     

if __name__ == "__main__":   
    unittest.main()