
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
            if len(num_str) > 1:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_numbers_greater_than_10(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_all_numbers_greater_than_10_but_invalid_digits(self):
        assert specialFilter([22, 44, 66, 88]) == 0
        assert specialFilter([12, 21, 23, 32]) == 0

    def test_valid_numbers(self):
        assert specialFilter([15, 33, 57, 79]) == 4

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15, 22, 33, 57, 88]) == 3
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -57, -79]) == 4
        assert specialFilter([-15, 15]) == 2

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([015, 033, 057, 079]) == 4

    def test_single_digit_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_large_numbers(self):
        assert specialFilter([151, 333, 575, 797, 12345]) == 4