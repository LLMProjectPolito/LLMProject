
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

def test_single_odd_first_last_greater_than_10():
    assert specialFilter([111]) == 1

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([-1, -2, -3]) == 0

def test_mixed_positive_negative():
    assert specialFilter([-15, 15, -21, 21]) == 2

def test_all_odd_first_last():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_some_odd_some_even_first_last():
    assert specialFilter([15, 12, 13, 14, 17]) == 2

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_large_numbers():
    assert specialFilter([111111, 133333, 155555, 177777, 199999]) == 5