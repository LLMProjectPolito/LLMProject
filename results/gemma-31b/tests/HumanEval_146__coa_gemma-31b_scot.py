
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
def test_specialFilter_boundary_threshold():
    # 10 is the boundary; 11 is the first possible valid integer
    assert specialFilter([10, 11]) == 1

def test_specialFilter_empty_list():
    # Boundary case: empty input array
    assert specialFilter([]) == 0

def test_specialFilter_below_threshold():
    # Boundary case: values just below 10 and negative values
    assert specialFilter([9, -11, -15]) == 0

# Focus: Logic Branches
def test_specialFilter_logic_branches_boundary():
    # Tests the > 10 condition: boundary 10, negative numbers, and numbers < 10
    assert specialFilter([10, 11, -11, 9, 13]) == 2

def test_specialFilter_logic_branches_digits():
    # Tests digit parity: first digit even, last digit even, both even, and both odd
    assert specialFilter([21, 12, 22, 11, 33]) == 2

def test_specialFilter_logic_branches_mixed():
    # Tests a mix of all failure paths: not > 10, first digit even, last digit even
    assert specialFilter([15, 25, 14, 5, 77]) == 2

# Focus: Type Scenarios
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_floats():
    # 11.1: > 10, first digit 1 (odd), last digit 1 (odd)
    # 13.3: > 10, first digit 1 (odd), last digit 3 (odd)
    assert specialFilter([11.1, 13.3]) == 2

def test_specialFilter_mixed_numeric():
    # 11 (int), 13.5 (float), 15 (int)
    assert specialFilter([11, 13.5, 15]) == 3