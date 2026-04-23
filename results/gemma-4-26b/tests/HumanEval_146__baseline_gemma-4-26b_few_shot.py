
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_special_filter_provided_examples():
    """Tests the examples provided in the docstring."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_empty_list():
    """Tests that an empty list returns 0."""
    assert specialFilter([]) == 0

def test_special_filter_threshold_boundary():
    """Tests numbers around the threshold of 10."""
    # 10 is not > 10. 11 is > 10 and both digits are odd.
    assert specialFilter([10, 11]) == 1
    # 9 is odd but not > 10.
    assert specialFilter([9]) == 0

def test_special_filter_negative_numbers():
    """Tests that negative numbers are excluded regardless of digit properties."""
    # -11 has odd digits but is not > 10.
    assert specialFilter([-11, -13, -15]) == 0

def test_special_filter_digit_parity():
    """Tests various combinations of first and last digit parity."""
    assert specialFilter([
        12,  # > 10, first odd, last even -> No
        21,  # > 10, first even, last odd -> No
        22,  # > 10, first even, last even -> No
        13,  # > 10, first odd, last odd -> Yes
        31,  # > 10, first odd, last odd -> Yes
    ]) == 2

def test_special_filter_large_numbers():
    """Tests large numbers to ensure first and last digit logic holds."""
    assert specialFilter([
        1001, # > 10, first 1 (odd), last 1 (odd) -> Yes
        3000, # > 10, first 3 (odd), last 0 (even) -> No
        5007, # > 10, first 5 (odd), last 7 (odd) -> Yes
        8009, # > 10, first 8 (even), last 9 (odd) -> No
        9999  # > 10, first 9 (odd), last 9 (odd) -> Yes
    ]) == 3

def test_special_filter_all_fail():
    """Tests a list where no elements meet the criteria."""
    assert specialFilter([2, 4, 6, 8, 10, 12, 14, 20, 22, 40]) == 0

def test_special_filter_all_pass():
    """Tests a list where all elements meet the criteria."""
    assert specialFilter([11, 13, 31, 33, 55, 71, 99]) == 7