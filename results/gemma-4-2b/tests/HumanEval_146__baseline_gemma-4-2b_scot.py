
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
        if num > 10 and str(abs(num))[0] in '13579' and str(abs(num))[(-1)] in '13579':
            count += 1
    return count

def test_empty_array():
    assert specialFilter([]) == 0

def test_no_numbers_satisfying_condition():
    assert specialFilter([-1, -2, -3, 4, 5]) == 0

def test_positive_numbers_satisfying_condition():
    assert specialFilter([15, 33, 45, 77, 99]) == 5

def test_negative_numbers_satisfying_condition():
    assert specialFilter([-15, -33, -45, -77, -99]) == 5

def test_mixed_numbers_satisfying_condition():
    assert specialFilter([15, -73, 14, -15, 33, -2, 45, 21, 109]) == 2

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9, 2, 4, 6, 8]) == 0

def test_numbers_with_only_one_digit_satisfying_condition():
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15]) == 3

def test_large_numbers():
    assert specialFilter([1000000001, 1000000003, 1000000005, 1000000007, 1000000009]) == 5