
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
            if num_str and num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

def test_specialFilter_example1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_example2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_all_match():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_mixed():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111]) == 10

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([11111, 33333, 55555, 77777, 99999]) == 5

def test_specialFilter_zero():
    assert specialFilter([0]) == 0

def test_specialFilter_single_element_match():
    assert specialFilter([15]) == 0

def test_specialFilter_single_element_no_match():
    assert specialFilter([12]) == 0

def test_specialFilter_with_floats():
    assert specialFilter([15.0, 33.5, 55.2]) == 0