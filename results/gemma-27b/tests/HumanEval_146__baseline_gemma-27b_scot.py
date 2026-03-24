
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
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 33, 57, 79, 91]) == 5

def test_mixed_numbers():
    assert specialFilter([15, 2, 33, 4, 57, 6, 79, 8, 91, 10]) == 4

def test_negative_numbers():
    assert specialFilter([-15, -33, -57, -79, -91]) == 5

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_large_numbers():
    assert specialFilter([123456789, 135791111, 987654321]) == 2

def test_edge_case_11():
    assert specialFilter([11]) == 0

def test_edge_case_13():
    assert specialFilter([13]) == 1