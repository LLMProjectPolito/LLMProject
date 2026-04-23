
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
            if len(num_str) > 0 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([-1, -2, -3]) == 0

def test_all_numbers_greater_than_10_but_not_meeting_criteria():
    assert specialFilter([11, 13, 15]) == 0

def test_all_numbers_greater_than_10_and_meeting_criteria():
    assert specialFilter([11, 13, 15]) == 3

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([-15, -73, -14, -15]) == 1

def test_zero():
    assert specialFilter([0, 15, -15]) == 1

def test_large_numbers():
    assert specialFilter([1000000001, 1000000003, 1000000005]) == 3

def test_mixed_positive_negative_large():
    assert specialFilter([-1000000001, 1000000003, -1000000005]) == 2

def test_single_number_greater_than_10_meeting_criteria():
    assert specialFilter([15]) == 1

def test_single_number_greater_than_10_not_meeting_criteria():
    assert specialFilter([14]) == 0

def test_single_number_less_than_10():
    assert specialFilter([5]) == 0

def test_large_numbers_with_odd_first_and_last_digit():
    assert specialFilter([1000000001, 1000000003, 1000000005, 1000000007, 1000000009]) == 5