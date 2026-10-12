"""This module is used to learn about unit testing"""
import unittest
from my_module import square, double, add

class TestSquare(unittest.TestCase):
    """This class is used to test the 'square' function"""

    def test1(self):
        """ first test"""
        self.assertEqual(square(2), 4)  # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.


class TestDouble(unittest.TestCase):
    """This class is used to test the 'double' function"""

    def test1(self):
        """ first test"""
        self.assertEqual(double(2), 4)  # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2)  # test when -3.1 is given as input the output is -6.2
        self.assertEqual(double(0), 0)  # test when 0 is given as input the output is 0.


class TestAdd(unittest.TestCase):
    """This class is used to test the 'add' function"""

    def test1(self):
        """ first test"""
        self.assertEqual(add(2, 2), 4)  # test when 2 is given as input the output is 4.
        self.assertEqual(add(-3.1, 2), -5.1)  # test when -3.1 is given as input the output is -6.2
        self.assertEqual(add(0, 2), 2)  # test when 0 is given as input the output is 0.


unittest.main()
