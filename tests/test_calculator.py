"""
Tests for Calculator class - تست های کلاس ماشین حساب
"""

import unittest
from testpython.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
    
    def test_get_result(self):
        """Test getting last result."""
        self.calc.add(5, 5)
        self.assertEqual(self.calc.get_result(), 10)
        self.calc.multiply(2, 3)
        self.assertEqual(self.calc.get_result(), 6)


if __name__ == '__main__':
    unittest.main()
