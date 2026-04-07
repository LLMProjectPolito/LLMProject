
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 37, 59]) == 3

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_numbers_less_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_equal_to_10():
    assert specialFilter([10]) == 0

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_large_numbers_with_even_digits():
    assert specialFilter([112, 334, 556, 778, 990]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([15, -37, 14, -59, 71]) == 2

def test_zero():
    assert specialFilter([0]) == 0

def test_decimal_numbers():
    assert specialFilter([15.5, 37.2, 59.8]) == 0

def test_string_input():
    with pytest.raises(TypeError):
        specialFilter(["15", "37"])

def test_none_input():
    with pytest.raises(TypeError):
        specialFilter(None)