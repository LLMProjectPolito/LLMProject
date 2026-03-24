
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

def test_mixed_positive_and_negative_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_numbers_greater_than_10_odd_ends():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 10

def test_numbers_less_than_10_odd_ends():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_negative_numbers_odd_ends():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_zero_odd_ends():
    assert specialFilter([0]) == 0

def test_large_numbers_odd_ends():
    assert specialFilter([13579]) == 1

def test_large_numbers_with_other_numbers_odd_ends():
    assert specialFilter([13579, 123, 456, 789]) == 1

def test_numbers_with_leading_zeros_odd_ends():
    assert specialFilter([15, 15]) == 1

def test_numbers_with_trailing_zeros_odd_ends():
    assert specialFilter([150, 350]) == 0

def test_numbers_with_mixed_odd_even_digits_odd_ends():
    assert specialFilter([21, 43, 65, 87, 109]) == 1

def test_all_numbers_same_odd_ends():
    assert specialFilter([33, 33, 33, 33]) == 1

def test_edge_case_1_odd_ends():
    assert specialFilter([111, 12, 333, 44, 555]) == 3

def test_edge_case_2_odd_ends():
    assert specialFilter([101, 11, 12, 13, 14, 15]) == 1

def test_large_number_odd_ends():
    assert specialFilter([9999999999]) == 1

def test_numbers_with_only_even_digits():
    assert specialFilter([24, 46, 68, 82]) == 0

def test_duplicates_and_unique_numbers():
    assert specialFilter([15, 15, 21]) == 1

def test_all_negative_numbers_odd_ends():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_no_numbers_meet_criteria_non_empty_list():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_max_integer_odd_ends():
    assert specialFilter([2147483647]) == 1

def test_invalid_input_float():
    with pytest.raises(TypeError):
        specialFilter([15.5])

def test_invalid_input_list():
    with pytest.raises(TypeError):
        specialFilter([[1, 2], 3])

def test_invalid_input_none():
    with pytest.raises(TypeError):
        specialFilter([None])