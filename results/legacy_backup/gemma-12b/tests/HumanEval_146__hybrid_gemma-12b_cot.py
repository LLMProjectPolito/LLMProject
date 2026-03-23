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

    def test_large_numbers(self):
        assert specialFilter([111, 3333, 55555, 777777, 9999999]) == 5

    def test_numbers_with_zeros(self):
        assert specialFilter([101, 303, 505, 707, 909]) == 0

    def test_numbers_with_leading_zeros(self):
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_single_number(self):
        assert specialFilter([15]) == 0

    def test_single_matching_number(self):
        assert specialFilter([11]) == 0

    def test_numbers_greater_than_10_and_less_than_100(self):
        assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]) == 25

    def test_numbers_with_decimal_part(self):
        assert specialFilter([15.5, 33.3, 55.5, 77.7, 99.9]) == 0

    def test_positive_numbers(self):
        assert specialFilter([15, 33, 57, 79, 91]) == 5

    def test_negative_numbers_2(self):
        assert specialFilter([-15, -33, -57, -79, -91]) == 0

    def test_mixed_positive_and_negative_2(self):
        assert specialFilter([15, -33, 57, -79, 91]) == 0

    def test_numbers_greater_than_10_2(self):
        assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 5

    def test_numbers_less_than_or_equal_to_10_2(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_zero_and_large_numbers(self):
        assert specialFilter([0, 131, 357, 7999, 9111]) == 4

    def test_single_digit_numbers_2(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_numbers_with_leading_zeros_2(self):
        assert specialFilter([15, 33, 57, 79, 91, 101]) == 5

    def test_large_numbers_with_odd_digits_2(self):
        assert specialFilter([13579, 97531, 11111]) == 3

    def test_numbers_with_even_digits_2(self):
        assert specialFilter([24, 46, 68, 82]) == 0

    def test_mixed_cases_2(self):
        assert specialFilter([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 5

    def test_boundary_just_above_10(self):
        assert specialFilter([11]) == 0

    def test_boundary_just_below_10(self):
        assert specialFilter([9]) == 0