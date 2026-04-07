
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
import math

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
    
def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_number():
    assert specialFilter([15]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([15, 22, 33, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -22, -33]) == 0

def test_mixed_positive_negative():
    assert specialFilter([-15, 22, -33, 45]) == 1

def test_edge_case_single_digit_odd():
    assert specialFilter([11]) == 0

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
    
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([11, 13, 15, 17, 19], 5),
        ([-11, -13, -15, -17, -19], 0),
        ([11, 13, 15, 17, 19, 21], 5),
        ([11, 13, 15, 17, 19, 23], 5),
        ([11, 13, 15, 17, 19, 45], 1),
        ([11, 13, 15, 17, 19, 47], 0),
        ([11, 13, 15, 17, 19, 55], 0),
    ]
)
def test_specialFilter_parametrized(nums, expected):
    assert specialFilter(nums) == expected