import unittest
from typing import List

class TestIntersperseFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1, 4])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_multiple_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimiter_value(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(intersperse([1, 1, 1], 4), [1, 4, 1, 4, 1])

    def test_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_zero(self):
        self.assertEqual(intersperse([0, 1, 2], 4), [0, 4, 1, 4, 2])

    def test_list_with_duplicate_elements(self):
        self.assertEqual(intersperse([1, 2, 2, 3], 4), [1, 4, 2, 4, 2, 4, 3])

    def test_single_element_input_list(self):
        self.assertEqual(intersperse([42], 4), [42])

    def test_zero_as_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_large_input_list(self):
        numbers = [i for i in range(1000)]
        delimeter = 42
        result = intersperse(numbers, delimeter)
        self.assertEqual(len(result), 2 * len(numbers) - 1)

if __name__ == '__main__':
    unittest.main()