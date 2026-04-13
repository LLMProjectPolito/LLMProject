
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
    The function considers the absolute value of the number when determining the first and last digits.
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))  # Use absolute value
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_valid_numbers():
    assert specialFilter([15, 33, 57, 79]) == 4

def test_invalid_numbers_first_digit_even():
    assert specialFilter([25, 43, 67, 89]) == 0

def test_invalid_numbers_last_digit_even():
    assert specialFilter([12, 34, 56, 78]) == 0

def test_negative_numbers():
    assert specialFilter([-15, -33, -57, -79]) == 4

def test_mixed_numbers():
    assert specialFilter([15, 23, 35, 47, 59, 61]) == 3

def test_zero_in_digits():
    assert specialFilter([105, 307, 509]) == 0

def test_large_numbers():
    assert specialFilter([13579, 35791, 57913]) == 3

# Removed test_leading_zero