
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

    def test_positive_numbers(self):
        assert specialFilter([15, 33, 57, 79, 91]) == 5

    def test_negative_numbers(self):
        assert specialFilter([-15, -33, -57, -79, -91]) == 0

    def test_mixed_positive_and_negative(self):
        assert specialFilter([15, -33, 57, -79, 91]) == 0

    def test_numbers_greater_than_10(self):
        assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25]) == 5

    def test_numbers_less_than_or_equal_to_10(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_example_1(self):
        assert specialFilter([15, -73, 14, -15]) == 1

    def test_example_2(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_zero_and_large_numbers(self):
        assert specialFilter([0, 131, 3579, 1000]) == 1

    def test_single_digit_odd_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_large_number_with_even_digits(self):
        assert specialFilter([12345, 55556, 77778]) == 0

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([105, 307, 509]) == 0

    def test_all_numbers_are_same(self):
        assert specialFilter([33, 33, 33, 33]) == 0

    def test_numbers_with_decimal_part(self):
        assert specialFilter([15.5, 33.3, 57.7]) == 0