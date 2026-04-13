
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

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

def test_specialFilter_positive():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([11, 22, 33, 44, 55]) == 5
    assert specialFilter([1, 2, 3, 4, 5, 6]) == 0
    assert specialFilter([]) == 0

def test_specialFilter_negative():
    assert specialFilter([-15, -23, -35]) == 0
    assert specialFilter([-1, 2, 3]) == 1
    assert specialFilter([10, -10, 10]) == 2
    assert specialFilter([-10, -20, -30]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

def test_specialFilter_mixed():
    assert specialFilter([15, -73, 14, -15, 21, 109]) == 2
    assert specialFilter([-15, 14, 21, 109]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert specialFilter([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_mixed():
    assert get_max([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_negative_mixed():
    assert get_max([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == -1