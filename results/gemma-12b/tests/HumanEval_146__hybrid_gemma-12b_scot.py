
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))  # Handle negative numbers
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_valid_numbers(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_even_first_digit(self):
        assert specialFilter([25, 43, 67]) == 0

    def test_even_last_digit(self):
        assert specialFilter([12, 34, 56]) == 0

    def test_valid_numbers(self):
        assert specialFilter([15, 33, 57, 79]) == 4

    def test_mixed_numbers(self):
        assert specialFilter([15, 22, 33, 44, 57, 66, 79]) == 3

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -57, -79]) == 4

    def test_single_valid_number(self):
        assert specialFilter([15]) == 1

    def test_large_numbers(self):
        assert specialFilter([151, 333, 575, 797, 919]) == 5

    def test_numbers_with_zero(self):
        assert specialFilter([105, 303, 507, 709]) == 0

    def test_edge_case_11(self):
        assert specialFilter([11, 13, 15]) == 0

    def test_edge_case_101(self):
        assert specialFilter([101, 111, 121]) == 3

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([015, 033, 057, 079]) == 0