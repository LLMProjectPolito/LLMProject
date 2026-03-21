import unittest
from typing import List

class TestHasCloseElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 1.0))

    def test_single_element_list(self):
        self.assertFalse(has_close_elements([1.0], 1.0))

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 1.0))

    def test_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 2.0))

    def test_negative_threshold(self):
        with self.assertRaises(ValueError):
            has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], -1.0)

    def test_threshold_is_zero(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.0))

    def test_large_threshold(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 10.0))

    def test_real_world_scenario(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_two_elements_not_close(self):
        self.assertFalse(has_close_elements([1.0, 2.0], 0.5))

    def test_two_elements_close(self):
        self.assertTrue(has_close_elements([1.0, 2.0], 0.3))

    def test_duplicate_elements(self):
        self.assertFalse(has_close_elements([1.0, 1.0, 3.0], 0.5))

    def test_threshold_zero(self):
        with self.assertRaises(ValueError):
            has_close_elements([1.0, 2.0], 0.0)

    def test_threshold_negative(self):
        with self.assertRaises(ValueError):
            has_close_elements([1.0, 2.0], -0.5)

    def test_threshold_large(self):
        self.assertFalse(has_close_elements([1.0, 2.0], 100.0))

    def test_threshold_equal_to_difference(self):
        self.assertTrue(has_close_elements([1.0, 2.0], 1.0))

    def test_positive_threshold(self):
        self.assertFalse(has_close_elements([1.0, 2.0], 0.5))

    def test_multiple_elements_not_close(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.1))

    def test_multiple_elements_close(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

if __name__ == '__main__':
    unittest.main()