#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test with a regular list."""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        result = max_integer([-2, -5, -1, -8])
	self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test with a list containing mixed positive and negative numbers."""
        result = max_integer([-2, 5, -1, 8])
	self.assertEqual(result, 8)

if __name__ == "__main__":
unittest.main()
