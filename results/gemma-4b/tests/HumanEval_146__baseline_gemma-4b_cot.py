
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

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_matching_number():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matching_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([1111111111, 1333333333]) == 2

def test_specialFilter_numbers_with_zero():
    assert specialFilter([101, 102, 103]) == 0

def test_specialFilter_single_digit_numbers():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_numbers_with_negative_first_digit():
    assert specialFilter([-15, 15]) == 1

def test_specialFilter_numbers_with_negative_last_digit():
    assert specialFilter([15, -15]) == 1

def test_specialFilter_numbers_with_both_negative_digits():
    assert specialFilter([-15, -13]) == 0

def test_specialFilter_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 1

def test_specialFilter_mixed_positive_and_negative_numbers():
    assert specialFilter([-15, 15, -33, 33]) == 2