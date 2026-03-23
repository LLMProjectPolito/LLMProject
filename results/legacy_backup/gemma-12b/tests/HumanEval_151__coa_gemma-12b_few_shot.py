import pytest
import math


# Focus: Boundary Values
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_negative_and_non_integer():
    assert double_the_difference([-1, -2, 0, 1.5]) == 1

# Focus: Type Scenarios
def test_double_the_difference_positive_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_double_the_difference_mixed():
    assert double_the_difference([1, 3, 2, 0, -1]) == 10

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

# Focus: Logic Branches
def test_double_the_difference_positive_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_double_the_difference_mixed():
    assert double_the_difference([1, 3, 2, 0, -1]) == 10

def test_double_the_difference_negative_and_non_integer():
    assert double_the_difference([-1, -2, 0, 1.5]) == 0