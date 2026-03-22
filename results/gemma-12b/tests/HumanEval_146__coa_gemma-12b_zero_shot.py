import pytest
import math


# Focus: Boundary Values
def test_boundary_value_1():
    assert specialFilter([11, 33, 55, 77, 99]) == 0

def test_boundary_value_2():
    assert specialFilter([10, 20, 30, 40, 50]) == 0

def test_boundary_value_3():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

# Focus: Type Scenarios
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_mixed_types():
    assert specialFilter([15, -73, 14, -15, "abc"]) == 1

# Focus: Logic Branches
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_mixed_branches():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2