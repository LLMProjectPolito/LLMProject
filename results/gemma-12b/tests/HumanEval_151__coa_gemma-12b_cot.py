import pytest
import math


# Focus: Boundary Values
def test_empty_list():
    assert double_the_difference([]) == 0

def test_zero_boundary():
    assert double_the_difference([0]) == 0

def test_negative_boundary():
    assert double_the_difference([-1]) == 0

def test_one_boundary():
    assert double_the_difference([1]) == 1

def test_small_odd_boundary():
    assert double_the_difference([3]) == 9

# Focus: Type Scenarios
def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_mixed_types():
    assert double_the_difference([1, 2.5, "a", 3]) == 1 + 9

def test_double_the_difference_negative_and_non_integer():
    assert double_the_difference([-1, -2, 0, 1.5]) == 1

# Focus: Logic Branches
def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_and_non_integer_values():
    assert double_the_difference([-1, -2, 0, 1.5]) == 1

def test_mixed_odd_even_positive_and_negative():
    assert double_the_difference([1, 3, 2, -1, 0, 5]) == 1 + 9 + 0 + 25 == 35