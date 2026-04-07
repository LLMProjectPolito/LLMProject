
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
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_some_matching_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 13, 15, 17, 19, 20]) == 5

def test_positive_and_negative():
    assert specialFilter([15, -73, 14, -15, 77, -31]) == 3

def test_single_digit_greater_than_10():
    assert specialFilter([11, 12, 13, 14, 15]) == 3

def test_leading_zeros():
    assert specialFilter([101, 103, 105]) == 3
    assert specialFilter([011, 013, 015]) == 0 # leading zeros are removed when converting to int

def test_edge_cases():
    assert specialFilter([11]) == 1
    assert specialFilter([13]) == 1
    assert specialFilter([15]) == 1
    assert specialFilter([19]) == 1

def test_larger_numbers():
    assert specialFilter([123, 135, 157, 179, 191]) == 5
    assert specialFilter([122, 134, 156, 178, 190]) == 0
    assert specialFilter([1111, 1333, 1555, 1777, 1999]) == 5