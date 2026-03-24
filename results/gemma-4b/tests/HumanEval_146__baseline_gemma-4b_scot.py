
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
# 2. The first and last digits of the absolute value of the element must both be odd.
# We need to create a pytest suite to test this function with various inputs, including positive and negative numbers, and edge cases.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with no elements satisfying the conditions.
# 3. List with some elements satisfying the conditions.
# 4. List with all elements satisfying the conditions.
# 5. List with negative numbers.
# 6. List with numbers close to 10.
# 7. List with large numbers.
# 8. List with mixed positive and negative numbers.

# Test functions:
# test_empty_list
# test_no_matching_elements
# test_some_matching_elements
# test_all_matching_elements
# test_negative_numbers
# test_numbers_close_to_10
# test_large_numbers
# test_mixed_numbers

### STEP 3: CODE
def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_elements():
    assert specialFilter([-1, -2, -3]) == 0

def test_some_matching_elements():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_all_matching_elements():
    assert specialFilter([33, 45, 109]) == 3

def test_negative_numbers():
    assert specialFilter([-11, -13, -15]) == 0

def test_numbers_close_to_10():
    assert specialFilter([9, 11, 13]) == 0

def test_large_numbers():
    assert specialFilter([1111111111, 1333333333]) == 2

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 111, -222]) == 2