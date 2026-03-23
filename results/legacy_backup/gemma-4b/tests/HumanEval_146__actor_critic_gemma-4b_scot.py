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
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `specialFilter` counts the number of elements in a list `nums` that satisfy two conditions:
# 1. The element must be greater than 10.
# 2. The first and last digits of the absolute value of the element must both be odd (1, 3, 5, 7, or 9).
# Edge cases to consider:
# - Empty list
# - List with only negative numbers
# - List with only numbers less than or equal to 10
# - List with mixed positive and negative numbers
# - Numbers with leading zeros (handled by taking absolute value)
# - Single-digit numbers (handled by the length check)

# STEP 2: PLAN - List test functions names and scenarios.
# test_specialFilter_empty_list
# test_specialFilter_positive_numbers
# test_specialFilter_negative_numbers
# test_specialFilter_mixed_numbers
# test_specialFilter_numbers_less_than_10
# test_specialFilter_edge_cases_first_last_digit
# test_specialFilter_zero_and_negative_zero

# STEP 3: CODE - Write the high-quality pytest suite.
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_positive_numbers():
    assert specialFilter([15, 25, 35, 45]) == 4

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -25, -35, -45]) == 4

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -25, 35, -45, 12, -13]) == 2

def test_specialFilter_numbers_less_than_10():
    assert specialFilter([5, 7, 9]) == 0

def test_specialFilter_edge_cases_first_last_digit():
    assert specialFilter([11, 33, 55, 77, 99]) == 5
    assert specialFilter([12, 34, 56, 78, 90]) == 0
    assert specialFilter([111, 333, 555, 777, 999]) == 5
    assert specialFilter([123, 345, 567, 789, 901]) == 0

def test_specialFilter_zero_and_negative_zero():
    assert specialFilter([0, -0]) == 0
    assert specialFilter([-11, -33]) == 0
    assert specialFilter([11, 33]) == 2

def test_specialFilter_leading_zero():
    assert specialFilter([-015]) == 1