"""
Tests for utility functions - تست های توابع کمکی
"""

import unittest
from datetime import datetime
from testpython.utils import greet, format_date, is_even, is_prime, fibonacci


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_greet(self):
        """Test greeting function."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertEqual(greet(""), "Hello, Guest!")
        self.assertEqual(greet(None), "Hello, Guest!")
    
    def test_format_date(self):
        """Test date formatting function."""
        test_date = datetime(2024, 1, 15, 10, 30, 45)
        formatted = format_date(test_date)
        self.assertEqual(formatted, "2024-01-15 10:30:45")
        
        custom_format = format_date(test_date, "%Y/%m/%d")
        self.assertEqual(custom_format, "2024/01/15")
    
    def test_is_even(self):
        """Test even number checker."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-3))
    
    def test_is_prime(self):
        """Test prime number checker."""
        # Prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        
        # Non-prime numbers
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
    
    def test_fibonacci(self):
        """Test Fibonacci sequence generator."""
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
        
        # Verify the sequence properties
        fib_10 = fibonacci(10)
        self.assertEqual(len(fib_10), 10)
        # Check that each element is sum of previous two (after first two)
        for i in range(2, len(fib_10)):
            self.assertEqual(fib_10[i], fib_10[i-1] + fib_10[i-2])


if __name__ == '__main__':
    unittest.main()
