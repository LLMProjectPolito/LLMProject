import pytest
import math


# Focus: Boundary Values
def test_double_the_difference_positive():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_single_positive():
    assert double_the_difference([0]) == 0

# Focus: Type Scenarios
def test_double_the_difference_positive():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_single():
    assert double_the_difference([0]) == 0

# Focus: Logic Branches
def test_double_the_difference_positive():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_single():
    assert double_the_difference([0]) == 0