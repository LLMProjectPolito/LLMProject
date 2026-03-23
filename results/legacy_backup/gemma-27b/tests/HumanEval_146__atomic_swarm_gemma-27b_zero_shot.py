import pytest
import math

def test_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_empty_input():
    assert specialFilter([]) == 0

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

def test_empty_array():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_large_numbers():
    assert specialFilter([111, 123, 135, 147, 159]) == 5

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_close_to_boundary():
    assert specialFilter([9, 11, 13, 15, 17, 19]) == 5

def test_string_input():
    with pytest.raises(TypeError):
        specialFilter(["15", "33"])

def test_float_input():
    with pytest.raises(TypeError):
        specialFilter([15.5, 33.2])