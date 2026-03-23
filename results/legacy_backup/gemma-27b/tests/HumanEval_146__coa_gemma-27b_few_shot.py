import pytest
import math


# Focus: Boundary Values
def test_specialfilter_empty():
    assert specialFilter([]) == 0

def test_specialfilter_single_element_valid():
    assert specialFilter([11]) == 1

def test_specialfilter_single_element_invalid():
    assert specialFilter([10]) == 0

def test_specialfilter_boundary_10():
    assert specialFilter([10]) == 0

def test_specialfilter_boundary_11():
    assert specialFilter([11]) == 1

# Focus: Logic Branches
def test_specialfilter_empty():
    assert specialFilter([]) == 0

def test_specialfilter_no_match():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_specialfilter_some_match():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

# Focus: Invalid Input Handling
def test_specialfilter_invalid_input_non_list():
    with pytest.raises(TypeError):
        specialFilter("not a list")

def test_specialfilter_invalid_input_list_non_numeric():
    with pytest.raises(TypeError):
        specialFilter([1, 2, "a"])

def test_specialfilter_invalid_input_list_mixed_types():
    with pytest.raises(TypeError):
        specialFilter([11, 13, "15"])