
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
            num_str = str(abs(num))  # Handle negative numbers
            if num_str and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_positive_numbers():
    assert specialFilter([15, 33, 55, 77, 99]) == 5

def test_negative_numbers():
    assert specialFilter([-15, -33, -55, -77, -99]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_mixed_numbers_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_edge_case_10():
    assert specialFilter([10]) == 0

def test_edge_case_11():
    assert specialFilter([11]) == 1

def test_single_negative_odd():
    assert specialFilter([-11]) == 0

def test_single_negative_even():
    assert specialFilter([-12]) == 0