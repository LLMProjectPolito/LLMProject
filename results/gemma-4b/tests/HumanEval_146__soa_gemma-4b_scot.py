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
# 2. The first and last digits of the absolute value of the element must both be odd.
# The test suite should cover various scenarios including:
# - Empty list
# - List with no elements satisfying the conditions
# - List with some elements satisfying the conditions
# - List with all elements satisfying the conditions
# - List with negative numbers
# - List with zero
# - List with large numbers

### STEP 2: PLAN
# Test functions:
# - test_empty_list: Tests with an empty list.
# - test_no_matches: Tests with a list where no elements satisfy the conditions.
# - test_some_matches: Tests with a list where some elements satisfy the conditions.
# - test_all_matches: Tests with a list where all elements satisfy the conditions.
# - test_negative_numbers: Tests with a list containing negative numbers.
# - test_zero: Tests with a list containing zero.
# - test_large_numbers: Tests with a list containing large numbers.
# - test_mixed_numbers: Tests with a list containing a mix of positive, negative, and zero.

### STEP 3: CODE
def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matches():
    assert specialFilter([-2, -3, -4]) == 0

def test_some_matches():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_all_matches():
    assert specialFilter([33, 45, 109]) == 3

def test_negative_numbers():
    assert specialFilter([-11, -13, -15]) == 0

def test_zero():
    assert specialFilter([0, 10, 11]) == 0

def test_large_numbers():
    assert specialFilter([111111111, 133333333]) == 2

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 109, -111]) == 2