
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

def test_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_number():
    assert specialFilter([15]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_numbers_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 5

def test_numbers_less_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_zero():
    assert specialFilter([0]) == 0

def test_large_numbers():
    assert specialFilter([151, 353, 575, 797, 919]) == 5

def test_numbers_with_leading_zeros():
    assert specialFilter([15, 33, 55, 77, 99]) == 5

def test_numbers_with_trailing_zeros():
    assert specialFilter([150, 330, 550, 770, 990]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109, -11]) == 2

def test_all_numbers_greater_than_10_and_odd_digits():
    assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]) == 25

def test_numbers_with_same_first_and_last_digits():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_numbers_with_different_first_and_last_digits():
    assert specialFilter([13, 15, 17, 19, 31, 35, 37, 39, 51, 53, 57, 59, 71, 73, 75, 79, 91, 93, 95, 97]) == 0

def test_numbers_with_spaces():
    with pytest.raises(ValueError):
        specialFilter(["15", "33", " 55"])

def test_very_large_numbers():
    assert specialFilter([151111111111111111111]) == 0

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_negative_number_with_same_digits():
    assert specialFilter([-11]) == 0

def test_zero_as_input():
    assert specialFilter([0]) == 0

def test_leading_trailing_zeros():
    assert specialFilter([01, 10, 110]) == 0

def test_return_type():
    result = specialFilter([11])
    assert isinstance(result, int)