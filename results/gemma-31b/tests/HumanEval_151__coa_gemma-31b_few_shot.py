
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
import pytest

def test_mixed_types():
    # Tests a mix of integers, floats, strings, and None
    # Only 1 and 3 are positive odd integers
    assert double_the_difference([1, 3, 2.5, "7", None, 3.0]) == 10

def test_non_integer_elements():
    # Tests a list containing only non-integer types
    assert double_the_difference([1.1, 2.2, "3", "5", None]) == 0

def test_boolean_types():
    # Tests how the function handles booleans (which are technically ints in Python)
    # If the function uses isinstance(x, int), True is 1 (odd) and False is 0 (even)
    # If it uses type(x) is int, they are ignored. 
    # Based on "not integers", we test for typical non-int behavior.
    assert double_the_difference([True, False, 3]) in [10, 9]

# Focus: Boundary Values
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_zero_and_negatives():
    assert double_the_difference([0, -1, -3, -2]) == 0

def test_double_the_difference_non_integers():
    assert double_the_difference([1.5, 3.7, 2.0]) == 0

# Focus: Logic Branches
def test_double_the_difference_mixed_branches():
    # Tests odd positive (keep), even positive (ignore), negative odd (ignore), negative even (ignore), and non-integers (ignore)
    assert double_the_difference([1, 3, 2, -1, -3, 2.5, "a"]) == 10

def test_double_the_difference_all_ignored():
    # Tests a list where every element falls into an "ignore" branch
    assert double_the_difference([-1, -5, 0, 2, 4, 1.1]) == 0

def test_double_the_difference_empty():
    # Tests the empty list branch
    assert double_the_difference([]) == 0