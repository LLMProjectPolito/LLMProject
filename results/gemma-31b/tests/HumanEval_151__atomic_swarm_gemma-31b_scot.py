
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

def test_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_extreme_edge_cases():
    assert double_the_difference([]) == 0
    assert double_the_difference([-1, -3, -5, 0, 2, 2.5, "a"]) == 0

def test_double_the_difference_mixed_types():
    assert double_the_difference([3, 2.5, "string", -1, None]) == 9