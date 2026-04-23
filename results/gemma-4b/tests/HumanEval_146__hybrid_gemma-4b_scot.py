
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
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if (first_digit % 2 != 0 and last_digit % 2 != 0):
                    count += 1
    return count

### SCoT Steps:

### STEP 1: REASONING
# The function `specialFilter` counts the number of elements in a list `nums` that satisfy two conditions:
# 1. The element must be greater than 10.
# 2. The first and last digits of the absolute value of the element must both be odd (1, 3, 5, 7, or 9).
# We need to test various scenarios including positive and negative numbers, numbers greater than 10, numbers less than or equal to 10, and cases where the first or last digit is not odd.  Edge cases like empty lists and lists with only invalid numbers should also be considered.

### STEP 2: PLAN
# Test functions:
# - test_empty_list: Tests the function with an empty list.
# - test_positive_numbers: Tests with a list of positive numbers.
# - test_negative_numbers: Tests with a list of negative numbers.
# - test_mixed_numbers: Tests with a list containing both positive and negative numbers.
# - test_numbers_less_than_10: Tests with numbers less than or equal to 10.
# - test_all_invalid: Tests with a list containing only numbers that fail both conditions.
# - test_edge_cases: Tests with edge cases like numbers with leading zeros (handled by abs()).
# - test_large_numbers: Tests with large numbers to ensure no overflow issues.

### STEP 3: CODE
def test_empty_list():
    assert specialFilter([]) == 0

def test_positive_numbers():
    assert specialFilter([15, 23, 35, 47, 59]) == 5

def test_negative_numbers():
    assert specialFilter([-15, -23, -35, -47, -59]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -23, 35, -47, 59, -61]) == 3

def test_numbers_less_than_10():
    assert specialFilter([5, 7, 9]) == 0

def test_all_invalid():
    assert specialFilter([-2, -4, -6, -8]) == 0

def test_edge_cases():
    assert specialFilter([11, 13, 15]) == 3
    assert specialFilter([-11, -13, -15]) == 3
    assert specialFilter([101, 103, 105]) == 3
    assert specialFilter([-101, -103, -105]) == 3

def test_large_numbers():
    assert specialFilter([1011, 1033, 1055]) == 3
    assert specialFilter([-1011, -1033, -1055]) == 3