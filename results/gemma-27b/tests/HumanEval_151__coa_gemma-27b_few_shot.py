import pytest
import math


# Focus: Boundary Values
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_negatives():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_zero_and_negatives():
    assert double_the_difference([0, -1, -2]) == 0

# Focus: Invalid Input Handling
def test_double_the_difference_invalid_input_string():
    assert double_the_difference(['a', 'b', 'c']) == 0

def test_double_the_difference_invalid_input_float():
    assert double_the_difference([1.5, 2.5, 3.5]) == 0

def test_double_the_difference_invalid_input_mixed():
    assert double_the_difference([1, 'a', 2.5, 3]) == 1 + 9

# Focus: Logic Branches
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_negatives_and_non_integers():
    assert double_the_difference([-1, -2, 0, 2.5]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([1, 3, 2, 0]) == 10