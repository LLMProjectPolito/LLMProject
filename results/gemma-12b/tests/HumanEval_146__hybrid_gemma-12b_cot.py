
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
            num_str = str(abs(num))
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

class TestSpecialFilter:
    def test_empty_list(self):
        assert specialFilter([]) == 0

    def test_no_matching_numbers(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_all_matching_numbers(self):
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_example_1(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_negative_numbers(self):
        assert specialFilter([-11, -33, -55, -77, -99]) == 0

    def test_zero_and_positive(self):
        assert specialFilter([0, 11, 22, 33]) == 1

    def test_large_numbers(self):
        assert specialFilter([111, 3333, 55555, 777777, 9999999]) == 5

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([101, 303, 505, 707, 909]) == 5

    def test_numbers_with_decimal_part(self):
        assert specialFilter([11.1, 33.3, 55.5, 77.7, 99.9]) == 0

    def test_single_digit_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_numbers_greater_than_100(self):
        assert specialFilter([111, 333, 555, 777, 999]) == 5

    def test_mixed_positive_and_negative_greater_than_10(self):
        assert specialFilter([11, -33, 55, -77, 99, 101, -103]) == 4

    def test_single_number(self):
        assert specialFilter([15]) == 0

    def test_single_matching_number(self):
        assert specialFilter([11]) == 1