import pytest
from math import isgrade

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
        if num > 10 and (num % 10 == 1 or num % 10 == 3 or num % 10 == 5 or num % 10 == 7 or num % 10 == 9):
            count += 1
    return count

def test_specialFilter_example1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_example2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_single_element():
    assert specialFilter([15]) == 1

def test_specialFilter_all_elements_greater_than_10():
    assert specialFilter([10, 20, 30]) == 3

def test_specialFilter_all_elements_less_than_10():
    assert specialFilter([-10, -20, -30]) == 0