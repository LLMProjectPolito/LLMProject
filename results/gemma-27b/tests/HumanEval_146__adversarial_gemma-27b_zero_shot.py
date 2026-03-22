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

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1
    assert specialFilter([-73]) == 1
    assert specialFilter([109]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_negative_numbers():
    assert specialFilter([-15, -33, -55]) == 3
    assert specialFilter([-12, -24, -36]) == 0

def test_mixed_numbers():
    assert specialFilter([15, 22, -33, 44, 55]) == 2
    assert specialFilter([111, 222, 333, 444, 555]) == 3

def test_numbers_less_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0
    assert specialFilter([2, 4, 6, 8]) == 0

def test_large_numbers():
    assert specialFilter([12345, 34567, 56789]) == 3
    assert specialFilter([23456, 45678, 67890]) == 0

def test_edge_cases():
    assert specialFilter([11]) == 1
    assert specialFilter([99]) == 1
    assert specialFilter([10]) == 0
    assert specialFilter([12]) == 0
    assert specialFilter([21]) == 1