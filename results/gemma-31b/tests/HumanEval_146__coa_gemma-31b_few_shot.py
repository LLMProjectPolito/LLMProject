
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
import math


# Focus: Boundary Values
def test_specialFilter_threshold_boundaries():
    # 10 is not > 10; 11 is > 10 and both digits are odd
    assert specialFilter([10, 11]) == 1
    # 9 is not > 10; -11 is not > 10
    assert specialFilter([9, -11]) == 0

def test_specialFilter_digit_boundaries():
    # 12: first odd, last even; 21: first even, last odd; 22: both even; 11: both odd
    assert specialFilter([12, 21, 22, 11]) == 1

def test_specialFilter_empty_input():
    assert specialFilter([]) == 0

# Focus: Logic Branches
import pytest

def test_special_filter_logic_branches():
    # Branch 1: num <= 10 (should be ignored regardless of digits)
    # Branch 2: num > 10, first digit even, last digit odd
    # Branch 3: num > 10, first digit odd, last digit even
    # Branch 4: num > 10, first digit even, last digit even
    # Branch 5: num > 10, first digit odd, last digit odd (should be counted)
    assert specialFilter([10, 9, 21, 12, 22, 11]) == 1

def test_special_filter_multi_digit_odd_branches():
    # Testing numbers > 10 with multiple digits to ensure first/last digit logic
    # 109: first=1 (odd), last=9 (odd) -> Yes
    # 302: first=3 (odd), last=2 (even) -> No
    # 401: first=4 (even), last=1 (odd) -> No
    # 505: first=5 (odd), last=5 (odd) -> Yes
    assert specialFilter([109, 302, 401, 505]) == 2

def test_special_filter_negative_and_boundary():
    # Negative numbers are <= 10, so they should fail the first condition immediately
    # 11 is the smallest positive integer that could potentially satisfy all conditions
    assert specialFilter([-11, -15, 11, 10]) == 1

# Focus: Type Scenarios
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_float_types():
    # Testing how the function handles float types (e.g., 11.0 ends in '0', which is even)
    assert specialFilter([11.0, 13.0, 15.5]) == 0

def test_specialFilter_mixed_numeric_types():
    # Testing a mix of integers and floats
    assert specialFilter([11, 13.0, 15]) == 2