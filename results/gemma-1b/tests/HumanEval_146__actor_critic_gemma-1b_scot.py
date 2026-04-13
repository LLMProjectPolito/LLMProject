
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

def test_empty_array():
    assert specialFilter([]) == 0

def test_single_element_greater_than_10_and_odd():
    assert specialFilter([15]) == 1

def test_single_element_not_greater_than_10_and_odd():
    assert specialFilter([-15]) == 0

def test_multiple_elements_greater_than_10_and_odd():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_multiple_elements_not_greater_than_10_and_odd():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_all_elements_greater_than_10_and_odd():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2

def test_all_elements_not_greater_than_10_and_odd():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 0

def test_negative_numbers():
    assert specialFilter([-15, -73, -14, -15]) == 1

def test_zero():
    assert specialFilter([0]) == 0

def test_large_numbers():
    assert specialFilter([1000000, -1000000]) == 1