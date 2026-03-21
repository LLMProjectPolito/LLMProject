import math
from typing import List, Tuple
import unittest

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_of_numbers = 0
    product_of_numbers = 1

    # Handle edge case of empty list
    if not numbers:
        return 0, 1

    # Handle edge case of single element list
    if len(numbers) == 1:
        return numbers[0], numbers[0]

    # Iterate over the list to calculate sum and product
    for num in numbers:
        sum_of_numbers += num
        product_of_numbers *= num

    # Handle zero in the list to avoid math domain error
    if 0 in numbers:
        # If zero is present, product is zero
        product_of_numbers = 0
        # But sum remains the same
        sum_of_numbers = sum(numbers)

    return sum_of_numbers, product_of_numbers

class TestSumProductFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_element_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_multiple_element_list_with_zero(self):
        self.assertEqual(sum_product([1, 2, 3, 0]), (6, 0))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, -24))

    def test_duplicates(self):
        self.assertEqual(sum_product([1, 2, 2, 3, 3, 3]), (12, 36))

    def test_list_with_zero(self):
        self.assertEqual(sum_product([1, 0, 3]), (4, 0))

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_product([1, -2, 3]), (2, -6))

    def test_list_with_large_numbers(self):
        self.assertEqual(sum_product([1000, 2000, 3000]), (6000, 6000000000))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_product("123")

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sum_product([1, 2, 'a'])

    def test_list_with_one_element(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_list_with_negative_numbers_and_zero(self):
        self.assertEqual(sum_product([-1, 0, -3]), (0, 0))

    def test_large_input_list(self):
        large_list = [i for i in range(1000)]
        result = sum_product(large_list)
        self.assertEqual(result[0], 499500)
        self.assertEqual(result[1], 0)

if __name__ == '__main__':
    unittest.main()