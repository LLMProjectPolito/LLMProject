
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
            if num_str[0] in '13579' and num_str[-1] in '13579':
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
        assert specialFilter([11, 13, 15, 17, 19, 21]) == 5

    def test_numbers_less_than_or_equal_to_10(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2

    def test_zero_and_large_numbers(self):
        assert specialFilter([0, 13579, 98765, 11111]) == 2

    def test_single_digit_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_large_numbers_with_odd_digits(self):
        assert specialFilter([135791, 987653, 111111]) == 2

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([15, 33, 57, 79, 91, 101]) == 5

    def test_all_numbers_same(self):
        assert specialFilter([15, 15, 15, 15, 15]) == 5

    def test_large_list(self):
        nums = [i for i in range(1, 101)]
        assert specialFilter(nums) == 10

    def test_all_matching_numbers(self):
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_example_1(self):
        assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    def test_negative_numbers_2(self):
        assert specialFilter([-11, -33, -55, -77, -99]) == 0

    def test_zero_and_positive_2(self):
        assert specialFilter([0, 11, 22, 33]) == 1

    def test_large_numbers_2(self):
        assert specialFilter([111, 3333, 55555, 777777, 9999999]) == 5

    def test_numbers_with_leading_zeros_2(self):
        assert specialFilter([101, 303, 505, 707, 909]) == 0

    def test_numbers_with_decimal_part(self):
        assert specialFilter([11.1, 33.3, 55.5, 77.7, 99.9]) == 0

    def test_numbers_greater_than_100(self):
        assert specialFilter([111, 333, 555, 777, 999]) == 5

    def test_mixed_positive_and_negative_greater_than_10_2(self):
        assert specialFilter([11, -33, 55, -77, 99, 101, -103]) == 3