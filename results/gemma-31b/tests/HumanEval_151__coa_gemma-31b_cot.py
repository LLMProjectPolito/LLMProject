
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''

import pytest
import math


# Focus: Type Scenarios
def test_double_the_difference_mixed_types():
    assert double_the_difference([1, "3", 3, 5.5, None]) == 10

def test_double_the_difference_non_integer_types():
    assert double_the_difference([2.0, 4.0, "7", None, [], {}]) == 0

def test_double_the_difference_float_integers():
    assert double_the_difference([3.0, 5.0, 7.0]) == 0

# Focus: Logic Branches
def test_double_the_difference_odd_even_branches():
    # Tests the branch for odd positive integers vs even positive integers
    assert double_the_difference([1, 3, 2, 4]) == 10  # 1^2 + 3^2 = 10
    assert double_the_difference([0, 2, 4, 6]) == 0   # All even/zero

def test_double_the_difference_invalid_branches():
    # Tests the branches for negative numbers and non-integer types
    assert double_the_difference([-1, -3, -5]) == 0   # Negative odds ignored
    assert double_the_difference([1.5, 3.5, 2.0]) == 0 # Non-integers ignored
    assert double_the_difference([-1, 1.1, 3]) == 9    # Mixed invalid and valid odd

def test_double_the_difference_empty_branch():
    # Tests the branch for an empty input list
    assert double_the_difference([]) == 0

# Focus: Boundary Values
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_zero_and_negatives():
    assert double_the_difference([0]) == 0
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_non_integers():
    assert double_the_difference([1.1, 3.3, 5.5]) == 0