
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

def test_special_filter_basic_true():
    """Test numbers that clearly meet all criteria (>10, first odd, last odd)."""
    # 11: >10, 1 odd, 1 odd
    # 35: >10, 3 odd, 5 odd
    # 79: >10, 7 odd, 9 odd
    assert specialFilter([11, 35, 79]) == 3

def test_special_filter_basic_false():
    """Test numbers that fail one or more criteria."""
    # 12: last digit even
    # 21: first digit even
    # 22: both digits even
    # 9: not > 10
    # -11: not > 10
    assert specialFilter([12, 21, 22, 9, -11]) == 0

def test_special_filter_empty():
    """Test with an empty list."""
    assert specialFilter([]) == 0

def test_special_filter_boundaries():
    """Test boundary conditions around the value 10."""
    # 10 is not > 10
    # 11 is > 10 and fits odd/odd
    assert specialFilter([10, 11]) == 1

def test_special_filter_large_numbers():
    """Test with larger numbers to ensure first and last digit logic works."""
    # 1001: >10, 1 odd, 1 odd (True)
    # 2001: >10, 2 even, 1 odd (False)
    # 1002: >10, 1 odd, 2 even (False)
    # 3005: >10, 3 odd, 5 odd (True)
    assert specialFilter([1001, 2001, 1002, 3005]) == 2

def test_special_filter_mixed_types():
    """Test a mix of valid and invalid numbers in one list."""
    # Valid: 13, 57, 911
    # Invalid: 10 (too small), 23 (first even), 34 (last even), -15 (too small)
    nums = [13, 10, 23, 57, 34, -15, 911]
    assert specialFilter(nums) == 3