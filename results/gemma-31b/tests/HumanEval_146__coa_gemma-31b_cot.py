
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
def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_thresholds():
    # 10 is the boundary for > 10; 11 is the smallest number that can satisfy all conditions
    assert specialFilter([10, 11]) == 1

def test_specialFilter_digit_edges():
    # Testing numbers > 10 where only one of the boundary digits is odd or both are even
    assert specialFilter([12, 21, 22, 11]) == 1

# Focus: Logic Branches
import pytest

def test_specialFilter_logic_branches_boundary_and_parity():
    # Tests the > 10 boundary and the odd/even digit combinations
    # 11: >10, first odd, last odd (Pass)
    # 10: not >10 (Fail)
    # 21: >10, first even, last odd (Fail)
    # 12: >10, first odd, last even (Fail)
    # 22: >10, first even, last even (Fail)
    assert specialFilter([11, 10, 21, 12, 22]) == 1

def test_specialFilter_logic_branches_negative_and_small():
    # Tests numbers that might have odd digits but fail the > 10 condition
    # -11: not >10 (Fail)
    # -15: not >10 (Fail)
    # 9: not >10 (Fail)
    # 7: not >10 (Fail)
    assert specialFilter([-11, -15, 9, 7]) == 0

def test_specialFilter_logic_branches_multi_digit_success():
    # Tests various multi-digit numbers that satisfy all conditions
    # 13: >10, 1 odd, 3 odd (Pass)
    # 35: >10, 3 odd, 5 odd (Pass)
    # 109: >10, 1 odd, 9 odd (Pass)
    # 777: >10, 7 odd, 7 odd (Pass)
    assert specialFilter([13, 35, 109, 777]) == 4

# Focus: Type Scenarios
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_float_inputs():
    assert specialFilter([11.0, 13.0, 15.0]) == 3

def test_specialFilter_mixed_numeric_types():
    assert specialFilter([11, 13.0, 15]) == 3