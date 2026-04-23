
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
        if num > 10 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
            count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([-15, -73, -14, -15]) == 0

def test_all_numbers_greater_than_10_but_not_meeting_condition():
    assert specialFilter([14, 16, 18, 19]) == 0

def test_all_numbers_meeting_condition():
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    
def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([-15, -73, -14, -15]) == 0

def test_large_numbers():
    assert specialFilter([101, 103, 105, 107, 109]) == 5

def test_mixed_positive_negative_large():
    assert specialFilter([101, -103, 105, -107, 109, -111]) == 2
    
def test_zero():
    assert specialFilter([0, 10]) == 0

def test_one():
    assert specialFilter([1, 11]) == 0
    
def test_large_numbers_greater_than_10_with_odd_first_and_last_digit():
    assert specialFilter([101, 103, 105, 107, 109]) == 5

def test_large_numbers_greater_than_10_with_even_first_and_last_digit():
    assert specialFilter([202, 204, 206, 208]) == 0