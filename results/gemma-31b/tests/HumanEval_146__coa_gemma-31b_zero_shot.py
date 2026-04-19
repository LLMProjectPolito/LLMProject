
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
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_threshold_boundary():
    # 10 is the boundary for > 10 (should be excluded)
    # 11 is the first integer > 10 that satisfies the odd digit condition
    assert specialFilter([10]) == 0
    assert specialFilter([11]) == 1

def test_specialFilter_digit_boundaries():
    # Testing numbers where only one of the two digits is odd
    assert specialFilter([12]) == 0  # First odd, last even
    assert specialFilter([21]) == 0  # First even, last odd

# Focus: Logic Branches
def test_specialFilter_all_conditions_met():
    # 11: >10, 1 odd, 1 odd
    # 35: >10, 3 odd, 5 odd
    # 79: >10, 7 odd, 9 odd
    assert specialFilter([11, 35, 79]) == 3

def test_specialFilter_branch_failures():
    # 10: fails > 10
    # 21: fails first digit odd
    # 12: fails last digit odd
    # -15: fails > 10
    assert specialFilter([10, 21, 12, -15]) == 0

def test_specialFilter_mixed_logic():
    # 13: True
    # 23: False (first digit even)
    # 14: False (last digit even)
    # 9: False (not > 10)
    assert specialFilter([13, 23, 14, 9]) == 1

# Focus: Type Scenarios
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_float_types():
    # 11.1: > 10, first digit 1 (odd), last digit 1 (odd)
    # 13.5: > 10, first digit 1 (odd), last digit 5 (odd)
    # 12.2: > 10, first digit 1 (odd), last digit 2 (even)
    assert specialFilter([11.1, 13.5, 12.2]) == 2

def test_specialFilter_mixed_numeric_types():
    # 11: > 10, first 1 (odd), last 1 (odd)
    # 13.3: > 10, first 1 (odd), last 3 (odd)
    # 14: > 10, first 1 (odd), last 4 (even)
    assert specialFilter([11, 13.3, 14]) == 2