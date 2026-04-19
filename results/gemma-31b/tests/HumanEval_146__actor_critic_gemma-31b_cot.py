
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_provided_examples():
    """Test the examples provided in the docstring."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_empty_list():
    """Test with an empty list."""
    assert specialFilter([]) == 0

def test_boundary_ten():
    """Test numbers around the threshold of 10."""
    # 10 is not > 10
    assert specialFilter([10]) == 0
    # 11 is > 10, first digit 1 (odd), last digit 1 (odd)
    assert specialFilter([11]) == 1

def test_single_digit_odd():
    """Test positive integers between 1 and 9. 
    They have odd first/last digits but are not > 10, so they should be excluded.
    """
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_negative_numbers():
    """Test that negative numbers are excluded regardless of digits."""
    # -11 is not > 10
    assert specialFilter([-11, -13, -15, -31]) == 0

def test_first_digit_even():
    """Test numbers > 10 where the first digit is even."""
    # 21: first digit 2 (even)
    # 43: first digit 4 (even)
    # 89: first digit 8 (even)
    assert specialFilter([21, 43, 89]) == 0

def test_last_digit_even():
    """Test numbers > 10 where the last digit is even."""
    # 12: last digit 2 (even)
    # 34: last digit 4 (even)
    # 56: last digit 6 (even)
    assert specialFilter([12, 34, 56]) == 0

def test_all_matching():
    """Test a list where all elements satisfy the conditions."""
    # 11, 33, 55, 77, 99, 101, 135, 317, 999
    nums = [11, 33, 55, 77, 99, 101, 135, 317, 999]
    assert specialFilter(nums) == len(nums)

def test_large_numbers():
    """Test very large numbers to ensure digit extraction works."""
    # 1000000001: > 10, first 1 (odd), last 1 (odd)
    # 2000000001: > 10, first 2 (even)
    # 1000000002: > 10, last 2 (even)
    assert specialFilter([1000000001]) == 1
    assert specialFilter([2000000001]) == 0
    assert specialFilter([1000000002]) == 0

@pytest.mark.parametrize("nums, expected", [
    ([11, 13, 15, 17, 19], 5),
    ([21, 23, 25, 27, 29], 0),
    ([31, 32, 33, 34, 35], 3), # 31, 33, 35
    ([10, 11, 12], 1),         # only 11
    ([101, 202, 303], 2),      # 101, 303
])
def test_parametrized_cases(nums, expected):
    """Run a variety of small test cases."""
    assert specialFilter(nums) == expected