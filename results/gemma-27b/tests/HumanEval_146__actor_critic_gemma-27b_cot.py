
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

# A "special" number is defined as a number greater than 10 where the first and last digits are odd (1, 3, 5, 7, or 9).
# Negative numbers are not considered "special" even if their absolute value is.

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_more_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -37, -59, -71, -93]) == 0

def test_negative_numbers_with_even_first_digit():
    assert specialFilter([-23]) == 0

def test_zero():
    assert specialFilter([0]) == 0

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_large_numbers_mixed():
    assert specialFilter([111, 222, 333, 444, 555]) == 3

def test_edge_case_11():
    assert specialFilter([11]) == 0

def test_edge_case_99():
    assert specialFilter([99]) == 1

def test_edge_case_101():
    assert specialFilter([101]) == 0

def test_edge_case_131():
    assert specialFilter([131]) == 1

def test_leading_zeros():
    assert specialFilter([15, 07, 09]) == 1

def test_leading_zeros_mixed():
    assert specialFilter([011, 013, 015]) == 0

def test_invalid_input_string():
    with pytest.raises(TypeError):
        specialFilter(['015'])

def test_invalid_input_mixed():
    with pytest.raises(TypeError):
        specialFilter([15, '23', 37])

def test_invalid_input_none():
    with pytest.raises(TypeError):
        specialFilter([15, None, 37])

def test_large_number_special():
    assert specialFilter([123456789]) == 1

def test_large_number_not_special():
    assert specialFilter([123456788]) == 0

def test_negative_special_absolute():
    assert specialFilter([-15]) == 0