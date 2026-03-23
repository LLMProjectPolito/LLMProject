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
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def test_specialFilter_basic1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_basic2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_specialFilter_all_match():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_specialFilter_mixed_numbers():
    assert specialFilter([11, -13, 15, -17, 19, 22, -23]) == 4

def test_specialFilter_single_digit_greater_than_10():
    assert specialFilter([11]) == 1
    assert specialFilter([12]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([12345, 13579, 10000, 10001]) == 1

def test_specialFilter_numbers_with_leading_zeros():
    assert specialFilter([011, 013]) == 0 # Leading zeros are not considered odd digits

def test_specialFilter_numbers_close_to_10():
    assert specialFilter([11, 9, 10]) == 1
    assert specialFilter([10, 11, 12]) == 1