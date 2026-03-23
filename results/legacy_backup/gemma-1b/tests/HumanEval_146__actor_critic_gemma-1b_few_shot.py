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
    assert specialFilter([]) == 0

def test_specialFilter_negative():
    assert specialFilter([-15, -23, -35]) == 0
    assert specialFilter([-11, -22, -33]) == 0
    assert specialFilter([-1, 2, 3]) == 1
    assert specialFilter([10, 20, 30]) == 0

def test_specialFilter_single_element():
    assert specialFilter([15]) == 1
    assert specialFilter([-15]) == 0
    assert specialFilter([1]) == 0
    assert specialFilter([11]) == 1
    assert specialFilter([22]) == 1
    assert specialFilter([33]) == 1
    assert specialFilter([44]) == 1
    assert specialFilter([55]) == 1
    assert specialFilter([]) == 0

def test_specialFilter_all_same():
    assert specialFilter([11, 11, 11]) == 3
    assert specialFilter([11, 11, 11, 11]) == 4
    assert specialFilter([11, 11, 11, 11, 11]) == 5
    assert specialFilter([11, 11, 11, 11, 11, 11]) == 6
    assert specialFilter([11, 11, 11, 11, 11, 11, 11]) == 7
    assert specialFilter([11, 11, 11, 11, 11, 11, 11, 11]) == 8
    assert specialFilter([11, 11, 11, 11, 11, 11, 11, 11]) == 9