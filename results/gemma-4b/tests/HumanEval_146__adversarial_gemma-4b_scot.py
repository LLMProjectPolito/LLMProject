
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


def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([-1, -2, -3]) == 0

def test_some_matching_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-11, -13, -15]) == 0
    assert specialFilter([-15, -35, -75]) == 3

def test_boundary_cases():
    assert specialFilter([10, 11, 12]) == 0
    assert specialFilter([11, 13, 15]) == 3

def test_mixed_numbers():
    assert specialFilter([11, 13, 15, 12, 14]) == 3
    assert specialFilter([15, 21, 33, 45, 57, 69, 71, 83, 95]) == 9

def test_large_numbers():
    assert specialFilter([101, 131, 151, 171, 191]) == 5
    assert specialFilter([999, 889, 779, 669, 559]) == 5