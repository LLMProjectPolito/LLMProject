
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
    """Test the examples provided in the docstring to ensure basic functionality."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_empty_list():
    """Test that an empty list returns 0."""
    assert specialFilter([]) == 0

def test_special_filter_boundary_ten():
    """
    Test the boundary condition '> 10'. 
    10 should be excluded. 11 should be included (1 is odd, 1 is odd).
    """
    assert specialFilter([10]) == 0
    assert specialFilter([11]) == 1

def test_special_filter_negative_numbers():
    """
    Test that negative numbers are excluded regardless of their digits,
    as they are not greater than 10.
    """
    # -11 has odd first and last digits, but is < 10
    assert specialFilter([-11, -13, -15, -31]) == 0

def test_special_filter_digit_logic():
    """
    Test various combinations of first/last digit parity.
    """
    # First odd, Last even -> Fail
    assert specialFilter([12, 34, 56, 78, 90]) == 0
    # First even, Last odd -> Fail
    assert specialFilter([21, 43, 65, 87, 29]) == 0
    # Both even -> Fail
    assert specialFilter([22, 44, 66, 88]) == 0
    # Both odd -> Pass
    assert specialFilter([11, 13, 31, 33, 55, 77, 99]) == 7

def test_special_filter_large_numbers():
    """Test numbers with multiple digits to ensure first/last logic is robust."""
    # 101: >10, 1 is odd, 1 is odd -> Pass
    # 201: >10, 2 is even -> Fail
    # 102: >10, 2 is even -> Fail
    # 3005: >10, 3 is odd, 5 is odd -> Pass
    assert specialFilter([101, 201, 102, 3005]) == 2

def test_special_filter_single_digits():
    """
    Test that single digit numbers are excluded because they are not > 10,
    even if the digit is odd.
    """
    assert specialFilter([1, 3, 5, 7, 9]) == 0

@pytest.mark.parametrize("nums, expected", [
    ([11, 13, 15], 3),           # All pass
    ([12, 21, 22], 0),           # All fail
    ([11, 10, 9], 1),            # Only one passes
    ([1000000001], 1),           # Very large number, odd start/end
    ([1000000002], 0),           # Very large number, even end
])
def test_special_filter_parametrized(nums, expected):
    """Comprehensive check of various scenarios using parametrization."""
    assert specialFilter(nums) == expected