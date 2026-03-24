
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

    def test_numbers_less_than_10(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_numbers_equal_to_10(self):
        assert specialFilter([10, 30, 50, 70, 90]) == 0

    def test_numbers_greater_than_10(self):
        assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39]) == 10

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2

    def test_single_digit_odd_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_large_numbers(self):
        assert specialFilter([151, 353, 575, 797, 919]) == 5

    def test_zero_in_number(self):
        assert specialFilter([105, 307, 509]) == 0

    def test_all_numbers_same(self):
        assert specialFilter([33, 33, 33, 33]) == 0

    def test_edge_case_1(self):
        assert specialFilter([11]) == 0

    def test_edge_case_2(self):
        assert specialFilter([12]) == 0