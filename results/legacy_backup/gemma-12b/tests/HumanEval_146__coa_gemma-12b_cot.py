import pytest
import math


# Focus: Boundary Values
import pytest

def test_specialFilter_boundary_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_boundary_all_less_than_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

def test_specialFilter_boundary_one_valid_number():
    assert specialFilter([15, 20, 33, 44, 55]) == 1

def test_specialFilter_boundary_negative_numbers():
    assert specialFilter([-15, -73, -11, -22]) == 0

def test_specialFilter_boundary_zero():
    assert specialFilter([0, 15, 33]) == 1

# Focus: Type Scenarios
def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_mixed_types_raises_typeerror():
    try:
        specialFilter([15, "abc", 33])
        assert False, "TypeError not raised"
    except TypeError:
        pass

# Focus: Logic Branches
import pytest

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_mixed_conditions():
    assert specialFilter([15, -73, 14, -15, 33, 57, 91]) == 3

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -35, -57, -79]) == 0

def test_specialFilter_single_matching_number():
    assert specialFilter([11]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 0