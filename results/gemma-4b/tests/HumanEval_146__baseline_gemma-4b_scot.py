
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
# We need to create a pytest suite to thoroughly test this function with various inputs, including positive and negative numbers, numbers greater than 10, and numbers that don't meet the criteria.  We should cover edge cases like empty lists and lists with only invalid numbers.

### STEP 2: PLAN
# Test Cases:
# 1. Empty list: []
# 2. List with no valid numbers: [-2, -4, -6]
# 3. List with some valid numbers: [15, -73, 14, -15]
# 4. List with multiple valid numbers: [33, -2, -3, 45, 21, 109]
# 5. List with numbers close to 10: [9, 11, 12]
# 6. List with negative numbers: [-11, -13, -15]
# 7. List with mixed positive and negative numbers: [-15, 15, -25, 25]
# 8. List with numbers containing leading zeros (handled by abs()): [101, -202]

### STEP 3: CODE
def test_empty_list():
    assert specialFilter([]) == 0

def test_no_valid_numbers():
    assert specialFilter([-2, -4, -6]) == 0

def test_some_valid_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_multiple_valid_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_numbers_close_to_10():
    assert specialFilter([9, 11, 12]) == 0

def test_negative_numbers():
    assert specialFilter([-11, -13, -15]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([-15, 15, -25, 25]) == 2

def test_numbers_with_leading_zeros():
    assert specialFilter([101, -202]) == 0

def test_single_valid_number():
    assert specialFilter([11]) == 1

def test_single_invalid_number():
    assert specialFilter([-12]) == 0

def test_large_numbers():
    assert specialFilter([1111111111, 1333333333]) == 2

def test_mixed_valid_and_invalid_large():
    assert specialFilter([1111111111, -2222222222, 1333333333]) == 2