
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

# STEP 1: REASONING
# The function `specialFilter` filters a list of numbers based on two conditions:
# 1. The number must be greater than 10.
# 2. Both the first and last digits of the number must be odd.
# The function returns the count of numbers that satisfy both conditions.
# We need to test various scenarios, including:
# - Empty list
# - List with no numbers greater than 10
# - List with numbers greater than 10 but not satisfying the odd digit condition
# - List with numbers greater than 10 and satisfying the odd digit condition
# - List with negative numbers
# - List with mixed positive and negative numbers
# - List with single-digit numbers
# - List with numbers having leading zeros (should be handled correctly)

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Test with an empty list.
# - test_no_numbers_greater_than_10: Test with a list where no number is greater than 10.
# - test_numbers_greater_than_10_odd_digits_fail: Test with numbers greater than 10 but failing the odd digit condition.
# - test_numbers_greater_than_10_odd_digits_pass: Test with numbers greater than 10 and satisfying the odd digit condition.
# - test_negative_numbers: Test with negative numbers.
# - test_mixed_numbers: Test with a mix of positive and negative numbers.
# - test_single_digit_numbers: Test with single-digit numbers.
# - test_leading_zeros: Test with numbers having leading zeros.
# - test_edge_cases: Test with edge cases like 11, 33, 55, 77, 99.

# STEP 3: CODE
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

    def test_no_numbers_greater_than_10(self):
        assert specialFilter([1, 2, 3, 4, 5]) == 0

    def test_numbers_greater_than_10_odd_digits_fail(self):
        assert specialFilter([12, 24, 36, 48, 50]) == 0

    def test_numbers_greater_than_10_odd_digits_pass(self):
        assert specialFilter([15, 37, 59, 71, 93]) == 5

    def test_negative_numbers(self):
        assert specialFilter([-15, -37, -59, -71, -93]) == 0

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2

    def test_single_digit_numbers(self):
        assert specialFilter([1, 3, 5, 7, 9]) == 0

    def test_leading_zeros(self):
        assert specialFilter([015, 037, 059]) == 0

    def test_edge_cases(self):
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_large_numbers(self):
        assert specialFilter([151, 373, 595, 717, 939]) == 5

    def test_mixed_positive_negative(self):
        assert specialFilter([15, -37, 22, 59, -71, 93, -11]) == 3