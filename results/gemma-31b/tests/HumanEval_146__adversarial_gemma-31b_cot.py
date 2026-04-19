
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
    """Test the examples provided in the docstring."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_empty():
    """Test with an empty list."""
    assert specialFilter([]) == 0

def test_special_filter_no_matches():
    """Test cases where no numbers satisfy the conditions."""
    # All <= 10
    assert specialFilter([10, 9, 0, -1, -15]) == 0
    # > 10 but first digit even
    assert specialFilter([21, 43, 65, 87]) == 0
    # > 10 but last digit even
    assert specialFilter([12, 34, 56, 78]) == 0
    # > 10 but both first and last even
    assert specialFilter([22, 44, 66, 88]) == 0

def test_special_filter_all_matches():
    """Test cases where all numbers satisfy the conditions."""
    # Small numbers > 10, both odd
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    # Larger numbers, both odd
    assert specialFilter([31, 33, 35, 37, 39]) == 5
    # Multi-digit numbers, both odd
    assert specialFilter([101, 303, 505, 707, 909]) == 5

def test_special_filter_boundaries():
    """Test boundary conditions around the value 10."""
    assert specialFilter([10]) == 0
    assert specialFilter([11]) == 1
    assert specialFilter([9]) == 0

def test_special_filter_negative_numbers():
    """
    Test that negative numbers are excluded by the '> 10' rule, 
    even if their digits are odd.
    """
    # -11 is not > 10
    assert specialFilter([-11, -13, -15]) == 0
    # Mixed negative and positive
    assert specialFilter([-11, 11]) == 1

def test_special_filter_large_numbers():
    """Test very large numbers to ensure digit extraction is robust."""
    # First digit 1 (odd), last digit 1 (odd), > 10
    assert specialFilter([1000000001]) == 1
    # First digit 2 (even), last digit 1 (odd), > 10
    assert specialFilter([2000000001]) == 0
    # First digit 1 (odd), last digit 2 (even), > 10
    assert specialFilter([1000000002]) == 0

@pytest.mark.parametrize("nums, expected", [
    ([11, 13, 15], 3),
    ([21, 23, 25], 0),
    ([12, 14, 16], 0),
    ([101, 102, 103], 2), # 101 and 103 match
    ([1111, 2222, 3333], 2), # 1111 and 3333 match
])
def test_special_filter_parametrized(nums, expected):
    """Parametrized tests for various combinations."""
    assert specialFilter(nums) == expected