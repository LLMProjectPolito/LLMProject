
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
            num_str = str(abs(num))  # Handle negative numbers
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

"""
This test suite tests the specialFilter function, which counts numbers
greater than 10 with odd first and last digits.
"""

def test_empty_array():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_number():
    assert specialFilter([15]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([33, 45, 57, 11]) == 3

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 22, 37, 51]) == 3

def test_negative_numbers():
    assert specialFilter([-15, -35, -57, -79]) == 0
    assert specialFilter([-15, 15, -35, 35]) == 2

def test_zero_and_positive_numbers():
    assert specialFilter([0, 11, 13, 15, 17, 19, 20]) == 6

def test_large_numbers():
    assert specialFilter([1235, 3457, 5679, 7891]) == 4

def test_numbers_close_to_10():
    assert specialFilter([11, 12, 9, 10, 110, 111]) == 2

def test_numbers_with_leading_zeros():
    assert specialFilter([15, 35, 55, 75, 95]) == 5

def test_numbers_with_zero_as_first_or_last_digit():
    assert specialFilter([105, 307, 510, 709]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([15, -73, 14, -15, 33]) == 2

def test_large_numbers_2():
    assert specialFilter([13579, -97351]) == 2

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_edge_case_11():
    assert specialFilter([11]) == 0