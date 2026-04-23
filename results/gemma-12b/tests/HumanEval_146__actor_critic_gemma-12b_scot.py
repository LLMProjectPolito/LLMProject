
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
from your_module import specialFilter  # Replace your_module

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 5, 10]) == 0

def test_positive_numbers_valid():
    assert specialFilter([15, 33, 57, 79, 91]) == 5

def test_positive_numbers_mixed():
    assert specialFilter([15, 73, 14, 15, 33, 2, 3, 45, 21, 109, 11]) == 4

def test_single_element_list_valid():
    assert specialFilter([15]) == 0

def test_single_element_list_invalid():
    assert specialFilter([12]) == 0

def test_single_valid_number():
    assert specialFilter([15]) == 0

def test_zero():
    assert specialFilter([0, 15, 33]) == 2

def test_floats():
    with pytest.raises(TypeError):
        specialFilter([15.5, 33.1, 57.9])

def test_invalid_first_digit():
    assert specialFilter([25, 43, 67, 89]) == 0
    assert specialFilter([05, 23, 47, 69]) == 0

def test_invalid_last_digit():
    assert specialFilter([12, 34, 56, 78]) == 0
    assert specialFilter([10, 32, 54, 76]) == 0

def test_negative_numbers_mixed():
    assert specialFilter([-15, 13, 57, -79, 91]) == 2
    assert specialFilter([-15, -33, -57, -79]) == 0
    assert specialFilter([-15, 13, -57, 79, -91]) == 2

def test_large_numbers():
    assert specialFilter([151, 333, 575, 797, 919]) == 5
    assert specialFilter([12345, 34567, 56789, 78912, 90123]) == 0
    assert specialFilter([101, 303, 505, 707, 909]) == 5

# The specialFilter function counts numbers greater than 10 where both the
# first and last digits are odd (1, 3, 5, 7, or 9).