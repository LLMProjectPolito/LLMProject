
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_special_filter_examples():
    """Test the examples provided in the problem description."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_empty():
    """Test with an empty list."""
    assert specialFilter([]) == 0

def test_special_filter_all_below_threshold():
    """Test numbers that are not greater than 10."""
    # 10 is not > 10, negative numbers are not > 10
    assert specialFilter([10, 9, 0, -1, -11, -15, -131]) == 0

def test_special_filter_even_digits():
    """Test numbers > 10 where first or last digits are even."""
    # 21: first digit 2 (even)
    # 12: last digit 2 (even)
    # 22: both even
    # 46: both even
    assert specialFilter([21, 12, 22, 46]) == 0

def test_special_filter_odd_digits_success():
    """Test numbers > 10 where both first and last digits are odd."""
    # 11: 1, 1 (odd, odd)
    # 13: 1, 3 (odd, odd)
    # 31: 3, 1 (odd, odd)
    # 33: 3, 3 (odd, odd)
    # 57: 5, 7 (odd, odd)
    # 99: 9, 9 (odd, odd)
    assert specialFilter([11, 13, 31, 33, 57, 99]) == 6

def test_special_filter_large_numbers():
    """Test larger numbers to ensure first and last digit logic holds."""
    # 101: 1, 1 (odd, odd) -> Yes
    # 3003: 3, 3 (odd, odd) -> Yes
    # 2002: 2, 2 (even, even) -> No
    # 1002: 1, 2 (odd, even) -> No
    # 2001: 2, 1 (even, odd) -> No
    # 55555: 5, 5 (odd, odd) -> Yes
    assert specialFilter([101, 3003, 2002, 1002, 2001, 55555]) == 3

@pytest.mark.parametrize("nums, expected", [
    ([11, 12, 13], 2),          # 11 and 13 match
    ([10, 11, 12], 1),          # Only 11 matches
    ([100, 101, 102], 1),       # Only 101 matches
    ([135, 357, 579], 3),       # All match
    ([235, 352, 252], 0),       # None match
    ([11, 33, 55, 77, 99], 5),  # All match
])
def test_special_filter_parametrized(nums, expected):
    """Parametrized tests for various combinations."""
    assert specialFilter(nums) == expected