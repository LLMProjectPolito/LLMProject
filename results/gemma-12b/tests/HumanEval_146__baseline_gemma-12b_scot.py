
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

# STEP 1: REASONING
# The function `specialFilter` needs to be tested thoroughly. We need to cover various scenarios, including:
# 1. Empty input list.
# 2. List with no numbers greater than 10.
# 3. List with numbers greater than 10, but none with odd first and last digits.
# 4. List with numbers greater than 10 and some with odd first and last digits.
# 5. List with negative numbers.
# 6. List with zero.
# 7. List with single element.
# 8. List with multiple elements satisfying the condition.
# 9. Edge cases with numbers like 11, 33, 55, 77, 99.
# 10. Numbers with leading zeros (although the problem doesn't explicitly mention it, it's good to consider).

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Test with an empty list.
# - test_no_numbers_greater_than_10: Test with numbers <= 10.
# - test_no_odd_digits: Test with numbers > 10 but no odd first/last digits.
# - test_mixed_numbers: Test with a mix of numbers, some satisfying the condition.
# - test_negative_numbers: Test with negative numbers.
# - test_single_element: Test with a single element.
# - test_multiple_matches: Test with multiple elements satisfying the condition.
# - test_edge_cases: Test with numbers like 11, 33, 55, 77, 99.
# - test_zero: Test with zero.

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
        assert specialFilter([1, 2, 3, 4, 5, 10]) == 0

    def test_no_odd_digits(self):
        assert specialFilter([22, 44, 66, 88, 10, 12]) == 0

    def test_mixed_numbers(self):
        assert specialFilter([15, -73, 14, -15, 22, 33, 45, 21, 109]) == 4

    def test_negative_numbers(self):
        assert specialFilter([-15, -73, -14, -15]) == 2

    def test_single_element(self):
        assert specialFilter([15]) == 1
        assert specialFilter([12]) == 0

    def test_multiple_matches(self):
        assert specialFilter([15, 35, 55, 75, 95]) == 5

    def test_edge_cases(self):
        assert specialFilter([11, 33, 55, 77, 99]) == 5

    def test_zero(self):
        assert specialFilter([0, 15, 33]) == 1

    def test_leading_zeros(self):
        assert specialFilter([15, 35, 015, 035]) == 4