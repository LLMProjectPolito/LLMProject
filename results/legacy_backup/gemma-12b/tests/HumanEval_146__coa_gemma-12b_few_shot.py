import pytest
import math


# Focus: Boundary Values
def test_specialFilter_boundary_empty():
    assert specialFilter([]) == 0

def test_specialFilter_boundary_all_false():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_boundary_one_true():
    assert specialFilter([11]) == 1

# Focus: Type Scenarios
def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

# Focus: Logic Branches
def test_special_filter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_multiple():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_no_match():
    assert specialFilter([2, 4, 6, 8, 10]) == 0