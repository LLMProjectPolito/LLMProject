import unittest
from unittest.mock import patch
from your_module import rolling_max

class TestRollingMaxFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(rolling_max([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_increasing_sequence(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_decreasing_sequence(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])

    def test_mixed_sequence(self):
        self.assertEqual(rolling_max([5, 2, 8, 1, 4, 3, 2, 6]), [5, 2, 8, 8, 4, 4, 4, 6])

    def test_negative_numbers(self):
        self.assertEqual(rolling_max([-5, -2, -8, -1, -4, -3, -2, -6]), [-5, -2, -8, -8, -4, -4, -4, -6])

    def test_zero(self):
        self.assertEqual(rolling_max([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_edge_cases_with_large_numbers(self):
        self.assertEqual(rolling_max([10**100, 10**100, 10**100]), [10**100, 10**100, 10**100])

    def test_multiple_elements_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_list_with_duplicates(self):
        self.assertEqual(rolling_max([2, 2, 3, 2, 3, 4, 2]), [2, 2, 3, 3, 3, 4, 4])

    def test_list_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -3, -4, -2]), [-1, -1, -1, -1, -1, -1, -1])

    def test_decreasing_list(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_increasing_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()