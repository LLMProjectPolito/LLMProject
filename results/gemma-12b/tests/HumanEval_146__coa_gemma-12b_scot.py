import pytest
import math


# Focus: Boundary Values
def test_specialFilter_boundary_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_boundary_equal_to_10():
    assert specialFilter([10, 20, 30, 40, 50]) == 0

def test_specialFilter_boundary_just_below_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

# Focus: Type Scenarios
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_specialFilter_mixed_types():
    assert specialFilter([15, -73, 14, -15, "abc", 33.5]) == 1

# Focus: Logic Branches
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_mixed_conditions():
    assert specialFilter([15, -73, 14, -15, 35, 71]) == 3