import unittest
from unittest.mock import patch
from typing import List

class TestIntersperseFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_single_element_list_with_delimeter(self):
        self.assertEqual(intersperse([1], 4), [1, 4])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_multiple_element_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 4), [1, 4, 2, 4, 3, 4])

    def test_negative_number_list(self):
        self.assertEqual(intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_list_with_zero(self):
        self.assertEqual(intersperse([0, 1, 2], 4), [0, 4, 1, 4, 2])

    def test_delimeter_value(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_no_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], None), [1, 2, 3])

    def test_negative_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], -4), [1, -4, 2, -4, 3])

    def test_delimeter_is_string(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2, 3], 'a')

    def test_delimeter_is_large(self):
        self.assertEqual(intersperse([1, 2, 3], 1000000), [1, 1000000, 2, 1000000, 3])

    def test_large_list(self):
        self.assertEqual(intersperse([1] * 1000, 4), [1] * 1000 + [4] * 999)

    def test_input_not_list(self):
        with self.assertRaises(TypeError):
            intersperse('123', 4)

    def test_input_list_contains_non_integer(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2.3, 3], 4)

if __name__ == '__main__':
    unittest.main()