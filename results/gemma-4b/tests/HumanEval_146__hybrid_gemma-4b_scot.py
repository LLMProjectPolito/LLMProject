
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
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

### SCoT Steps:

### STEP 1: REASONING
# The function `specialFilter` counts the number of elements in a list `nums` that satisfy two conditions:
# 1. The element must be greater than 10.
# 2. The first and last digits of the absolute value of the element must both be odd (1, 3, 5, 7, or 9).
# We need to test various scenarios including positive and negative numbers, numbers greater than 10, numbers less than or equal to 10, and cases where the first or last digit is not odd.
# We should also consider edge cases like empty lists and lists with only one element.

### STEP 2: PLAN
# Test functions:
# - test_empty_list: Tests the function with an empty list.
# - test_positive_numbers: Tests the function with a list of positive numbers.
# - test_negative_numbers: Tests the function with a list of negative numbers.
# - test_mixed_numbers: Tests the function with a list of mixed positive and negative numbers.
# - test_numbers_less_than_10: Tests the function with numbers less than 10.
# - test_first_last_digit_odd: Tests the function with numbers where both first and last digits are odd.
# - test_first_last_digit_even: Tests the function with numbers where either the first or last digit is even.
# - test_single_element_positive: Tests the function with a list containing a single positive number.
# - test_single_element_negative: Tests the function with a list containing a single negative number.
# - test_edge_cases: Tests with edge cases like numbers with leading zeros when converted to string.

### STEP 3: CODE
def test_empty_list():
    assert specialFilter([]) == 0

def test_positive_numbers():
    assert specialFilter([15, 21, 33, 45, 23, 57]) == 4

def test_negative_numbers():
    assert specialFilter([-15, -21, -33, -45, -23, -57]) == 4

def test_mixed_numbers():
    assert specialFilter([15, -21, 33, -45, 23, -57]) == 3

def test_numbers_less_than_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

def test_first_last_digit_odd():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_first_last_digit_even():
    assert specialFilter([21, 43, 65, 87, 109]) == 0

def test_single_element_positive():
    assert specialFilter([15]) == 1

def test_single_element_negative():
    assert specialFilter([-15]) == 1

def test_edge_cases():
    assert specialFilter([-111, 111]) == 0
    assert specialFilter([-11, 11]) == 0
    assert specialFilter([-1111, 1111]) == 0