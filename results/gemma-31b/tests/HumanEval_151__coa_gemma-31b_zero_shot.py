
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
def test_double_the_difference_floats():
    # Floats should be ignored even if they represent whole numbers (e.g., 3.0)
    assert double_the_difference([1, 3.0, 2.5, 5]) == 1**2 + 5**2

def test_double_the_difference_non_numeric():
    # Strings, None, and other non-integer types should be ignored
    assert double_the_difference([1, "3", None, 7, [1]]) == 1**2 + 7**2

def test_double_the_difference_mixed_types():
    # Combination of valid odd ints, even ints, floats, and strings
    assert double_the_difference([1, 2, 3.14, "odd", 3, -5]) == 1**2 + 3**2

# Focus: Boundary Values
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_no_valid_odds():
    assert double_the_difference([0, -1, -3, 2, 2.5, "a"]) == 0

def test_double_the_difference_single_boundary_odd():
    assert double_the_difference([1]) == 1

# Focus: Logic Branches
def test_double_the_difference_mixed_branches():
    # Tests odd positives (included), even positives (ignored), negatives (ignored), and non-integers (ignored)
    assert double_the_difference([1, 3, 2, 4, -1, -3, 2.5, "a"]) == 10

def test_double_the_difference_exclusion_branches():
    # Tests cases where no numbers meet the criteria (only negatives, evens, or non-integers)
    assert double_the_difference([-1, -5, 0, 2, 4, 1.1]) == 0

def test_double_the_difference_empty_branch():
    # Tests the specific branch for an empty input list
    assert double_the_difference([]) == 0