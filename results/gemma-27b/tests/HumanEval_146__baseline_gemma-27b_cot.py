
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

def test_specialFilter_empty_array():
    assert specialFilter([]) == 0

def test_specialFilter_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_one_special_number():
    assert specialFilter([15, 2, 4, 6, 8]) == 1

def test_specialFilter_multiple_special_numbers():
    assert specialFilter([33, 45, 21, 109]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_large_numbers():
    assert specialFilter([111, 123, 135, 147, 159]) == 5

def test_specialFilter_numbers_close_to_10():
    assert specialFilter([11, 13, 15, 99]) == 3

def test_specialFilter_numbers_just_above_10():
    assert specialFilter([11, 12, 13, 14, 15]) == 2

def test_specialFilter_all_numbers_greater_than_10_but_none_special():
    assert specialFilter([12, 14, 16, 18, 20]) == 0

def test_specialFilter_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_zero():
    assert specialFilter([0]) == 0

def test_specialFilter_negative_and_positive():
    assert specialFilter([-11, 11, -13, 13]) == 2

def test_specialFilter_with_duplicates():
    assert specialFilter([15, 15, 33, 33]) == 2

def test_specialFilter_edge_case_11111():
    assert specialFilter([11111]) == 1