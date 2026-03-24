
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
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_valid_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_valid_number():
    assert specialFilter([15]) == 1

def test_multiple_valid_numbers():
    assert specialFilter([15, 33, 77, 11, 22]) == 4

def test_negative_numbers():
    assert specialFilter([-15, -33, -77]) == 3

def test_large_number():
    assert specialFilter([15151515]) == 1

def test_zero():
    assert specialFilter([0]) == 0

def test_mixed_numbers():
    assert specialFilter([5, 15, -33, 77, -11, 22, 109, 110]) == 4

def test_single_digit_number():
    assert specialFilter([11]) == 0

def test_first_digit_even():
    assert specialFilter([25]) == 0

def test_last_digit_even():
    assert specialFilter([12]) == 0