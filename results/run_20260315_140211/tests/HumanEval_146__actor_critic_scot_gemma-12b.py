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
    def test_empty_array(self):
        assert specialFilter([]) == 0

    def test_no_matches(self):
        assert specialFilter([2, 4, 6, 8, 10]) == 0

    def test_single_match(self):
        assert specialFilter([15]) == 1

    def test_single_no_match(self):
        assert specialFilter([12]) == 0

    def test_basic_matches(self):
        assert specialFilter([15, 33, 57, 79]) == 4

    def test_mixed_matches(self):
        assert specialFilter([15, 22, 33, 44, 57, 66, 79]) == 3

    def test_greater_than_10_even_digits(self):
        assert specialFilter([12, 34, 56, 78, 90]) == 0

    def test_less_than_equal_10(self):
        assert specialFilter([1, 2, 3, 4, 5, 10]) == 0

    def test_negative_matches(self):
        assert specialFilter([-15, -33, -57, -79]) == 4

    def test_large_numbers(self):
        assert specialFilter([159, 333, 577, 799]) == 4

    def test_mixed_positive_negative(self):
        assert specialFilter([15, -33, 22, -57, 79, -91]) == 4

    def test_single_digit_odd(self):
        assert specialFilter([5]) == 0  # Single digit numbers are not greater than 10

    def test_negative_number(self):
        assert specialFilter([-15]) == 1

    def test_with_zero(self):
        assert specialFilter([0, 15, 33]) == 2

    def test_leading_zeros(self):
        assert specialFilter([15]) == 1  # Using decimal representation

    def test_large_negative_number(self):
        assert specialFilter([-159]) == 1

    def test_single_digit_less_than_10(self):
        assert specialFilter([7]) == 0

    def test_multi_digit_number(self):
        assert specialFilter([135]) == 1