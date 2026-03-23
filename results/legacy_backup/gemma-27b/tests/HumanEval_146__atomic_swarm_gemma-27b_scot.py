import pytest
import math

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

def test_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

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

def test_negative_numbers():
    assert specialFilter([-15, -73, -14, -15]) == 1

def test_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_all_numbers_less_than_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

def test_numbers_with_even_first_digit():
    assert specialFilter([25, 43, 61, 89]) == 0

def test_numbers_with_even_last_digit():
    assert specialFilter([12, 34, 56, 78]) == 0

def test_numbers_with_both_even_digits():
    assert specialFilter([24, 46, 68, 80]) == 0

def test_single_digit_number_greater_than_10():
    assert specialFilter([11]) == 1

def test_large_number():
    assert specialFilter([123456789]) == 1

def test_number_with_leading_zero():
    assert specialFilter([011]) == 0

def test_number_with_decimal():
    assert specialFilter([15.5]) == 0

def test_number_as_string():
    assert specialFilter(["15"]) == 0

def test_invalid_input_type():
    with pytest.raises(TypeError):
        specialFilter([15, "abc"])