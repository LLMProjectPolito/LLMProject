import pytest
import math


# Focus: Boundary Values
def test_double_the_difference_boundary_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_boundary_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_boundary_zero_and_positive():
    assert double_the_difference([0, 1]) == 1

# Focus: Type Scenarios
def test_empty_list():
    assert double_the_difference([]) == 0

def test_list_with_negative_and_non_integer():
    assert double_the_difference([-1, -2, 0, 1.5]) == 1

def test_list_with_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

# Focus: Logic Branches
def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_mixed_positive_negative_and_zero():
    assert double_the_difference([1, 3, 2, 0, -1]) == 10