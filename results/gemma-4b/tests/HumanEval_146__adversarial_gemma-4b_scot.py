
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
    assert specialFilter([-11, 13, -15]) == 0

def test_boundary_conditions():
    assert specialFilter([10, 11, 19, 21]) == 0
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_mixed_numbers():
    assert specialFilter([15, 20, 11, 13, 17, 21, 23, 29]) == 5
    assert specialFilter([-15, -20, -11, -13, -17, -21, -23, -29]) == 0

def test_large_numbers():
    assert specialFilter([1111111111, 1333333333]) == 2
    assert specialFilter([9999999999, 1111111111]) == 1