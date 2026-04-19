
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
def test_double_the_difference_non_integers():
    # Test with floats and strings which should be ignored
    assert double_the_difference([1, 3.0, "5", 3]) == 1**2 + 3**2
    assert double_the_difference([2.2, 4.4, "odd"]) == 0

def test_double_the_difference_mixed_types():
    # Test with a mix of None, booleans, and other types
    # Note: In Python, True is an instance of int, but typically ignored in these constraints
    assert double_the_difference([1, None, 5, [1], {1}]) == 1**2 + 5**2

# Focus: Boundary Values
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_single_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_single_odd():
    assert double_the_difference([1]) == 1

# Focus: Logic Branches
def test_odd_even_branching():
    # Tests the branch that distinguishes between odd and even positive integers
    assert double_the_difference([1, 2, 3, 4]) == 10  # 1^2 + 3^2

def test_filtering_branching():
    # Tests the branches that ignore negative numbers and non-integers
    assert double_the_difference([-1, -3, 2.5, 5, "a"]) == 25  # Only 5^2

def test_empty_branching():
    # Tests the branch for an empty input list
    assert double_the_difference([]) == 0