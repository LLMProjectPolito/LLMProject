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

# STEP 1: REASONING
# The function `specialFilter` counts numbers in a list that meet specific criteria:
# 1. The number must be greater than 10.
# 2. The first and last digits of the number (when considered as a string) must be odd (1, 3, 5, 7, or 9).
# The function handles both positive and negative numbers by taking the absolute value when converting to a string.
# Edge cases to consider:
# - Empty list
# - List with no numbers greater than 10
# - Numbers with only one digit (should not be counted as they are not > 10)
# - Negative numbers
# - Numbers with leading zeros (should be handled correctly by abs() and string conversion)

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Test with an empty list.
# - test_no_numbers_greater_than_10: Test with a list where all numbers are <= 10.
# - test_all_numbers_meet_criteria: Test with a list where all numbers meet the criteria.
# - test_some_numbers_meet_criteria: Test with a list where some numbers meet the criteria.
# - test_negative_numbers: Test with a list containing negative numbers.
# - test_single_digit_numbers: Test with a list containing single-digit numbers.
# - test_mixed_numbers: Test with a mix of positive, negative, and single-digit numbers.
# - test_numbers_with_leading_zeros: Test with numbers that might have leading zeros after abs().

# STEP 3: CODE
def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_all_numbers_meet_criteria():
    assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39]) == 10

def test_some_numbers_meet_criteria():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0
    assert specialFilter([-11, 15, -13, 17]) == 1
    assert specialFilter([-31, -33, -35]) == 0

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_mixed_numbers():
    assert specialFilter([11, 2, -15, 8, 33, -7, 109]) == 2

def test_numbers_with_leading_zeros():
    assert specialFilter([101, 103, 105]) == 0
    assert specialFilter([111, 131, 151]) == 3