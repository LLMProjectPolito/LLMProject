import unittest
from typing import List

class TestHasCloseElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_single_element_list(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_duplicate_elements_list(self):
        self.assertFalse(has_close_elements([1.0, 1.0, 1.0], 0.5))

    def test_elements_greater_than_threshold(self):
        self.assertFalse(has_close_elements([1.0, 10.0], 0.5))

    def test_elements_equal_to_threshold(self):
        self.assertFalse(has_close_elements([1.0, 1.5], 0.5))

    def test_elements_less_than_threshold(self):
        self.assertTrue(has_close_elements([1.0, 1.3], 0.5))

    def test_threshold_zero(self):
        self.assertFalse(has_close_elements([1.0, 2.0], 0))

    def test_threshold_large(self):
        self.assertTrue(has_close_elements([1.0, 2.0], 1e6))

    def test_happy_path(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_numbers_close_together(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_numbers_far_apart(self):
        self.assertFalse(has_close_elements([1.0, 10.0, 100.0], 5.0))

    def test_threshold_greater_than_max_difference(self):
        self.assertFalse(has_close_elements([1.0, 10.0, 100.0], 100.0))

    def test_duplicate_numbers(self):
        self.assertFalse(has_close_elements([1.0, 1.0, 3.0], 0.5))

    def test_threshold_negative(self):
        with self.assertRaises(ValueError):
            has_close_elements([1.0, 2.0], -0.5)

    def test_large_threshold(self):
        self.assertFalse(has_close_elements([1.0, 2.0], 10.0))

    def test_non_float_numbers(self):
        with self.assertRaises(TypeError):
            has_close_elements([1, 2.0, 3.0], 0.5)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            has_close_elements('hello', 0.5)

    def test_negative_numbers(self):
        self.assertTrue(has_close_elements([-1.0, -2.0, -3.0], 0.5))

    def test_decimal_numbers(self):
        self.assertTrue(has_close_elements([1.0, 2.3, 3.0, 4.0, 5.0, 2.0], 0.3))

if __name__ == '__main__':
    unittest.main()