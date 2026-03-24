
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
        num_str = str(abs(num))
        if len(num_str) > 0 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
            count += 1
    return count

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_single_positive():
    assert specialFilter([15]) == 1

def test_specialFilter_single_negative():
    assert specialFilter([-73]) == 1

def test_specialFilter_multiple_positive():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple_negative():
    assert specialFilter([-73, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_same():
    assert specialFilter([11, 11, 11, 11]) == 4

def test_specialFilter_all_same_negative():
    assert specialFilter([-11, -11, -11, -11]) == 4

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2