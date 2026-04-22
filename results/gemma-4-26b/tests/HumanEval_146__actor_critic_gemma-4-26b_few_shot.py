
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

def test_special_filter_boundary_ten():
    """Tests that numbers must be strictly greater than 10."""
    # 10 is not > 10, and even if it were, 0 is even.
    assert specialFilter([10]) == 0

def test_special_filter_negative_numbers():
    """Tests that negative numbers are excluded (since they are < 10)."""
    # Even if the digits are odd, the value must be > 10
    assert specialFilter([-11, -13, -15, -33, -109]) == 0

def test_special_filter_single_digits():
    """Tests that single digit numbers are excluded (since they are < 10)."""
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_special_filter_digit_combinations():
    """Tests various combinations of first and last digits."""
    assert specialFilter([
        11, # Match: >10, 1 is odd, 1 is odd
        12, # Fail: 2 is even
        21, # Fail: 2 is even
        22, # Fail: both even
        33, # Match: >10, 3 is odd, 3 is odd
        45, # Fail: 4 is even
        57, # Match: >10, 5 is odd, 7 is odd
        90, # Fail: 0 is even
    ]) == 3

def test_special_filter_large_numbers():
    """Tests very large numbers to ensure digit extraction works."""
    assert specialFilter([
        1000000001, # Match: >10, 1 is odd, 1 is odd
        3000000007, # Match: >10, 3 is odd, 7 is odd
        2000000001, # Fail: 2 is even
        1000000002, # Fail: 2 is even
    ]) == 2

@pytest.mark.parametrize("input_list, expected_count", [
    ([11, 13, 15, 17, 19], 5),  # All match
    ([20, 22, 24, 26, 28], 0),  # None match (even first digit)
    ([12, 32, 52, 72, 92], 0),  # None match (even last digit)
    ([11, 22, 33, 44, 55], 3),  # Mixed
])
def test_special_filter_parametrized(input_list, expected_count):
    """Parametrized test for multiple scenarios."""
    assert specialFilter(input_list) == expected_count