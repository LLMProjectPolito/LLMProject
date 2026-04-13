
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

def is_odd_digit(digit):
    return digit in '13579'

def special_filter_criteria(num):
    num_str = str(abs(num))
    return len(num_str) > 0 and is_odd_digit(num_str[0]) and is_odd_digit(num_str[-1])

@pytest.mark.parametrize("nums, expected", [
    ([], 0),
    ([1, 2, 3, 4, 5], 0),
    ([15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([15, -73, 14, -15], 1),
    ([13579], 1),
    ([13579, 123, 456, 789], 1),
    ([15, 015], 1),  # Handles leading zeros as intended
    ([150, 350], 0),
    ([105], 0), # Zero handling test
    ([-15, -33], 1), # Negative number edge case
    ([111, 333, 555, 777, 999], 0),
    ([101, 303, 505, 707, 909], 0),
])
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected

def test_is_odd_digit():
    assert is_odd_digit('7') == True
    assert is_odd_digit('0') == False
    assert is_odd_digit('2') == False
    assert is_odd_digit('9') == True

def test_floating_point_input():
    assert specialFilter([15.99999]) == 1

def test_mixed_data_types():
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 33])

def test_none_input():
    with pytest.raises(TypeError):
        specialFilter(None)

def test_duplicates():
    assert specialFilter([15, 15, 33, 33]) == 2

def test_invalid_input():
    with pytest.raises(TypeError):
        specialFilter([15, 15.5, 33])