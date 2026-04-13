
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

def test_mixed_types():
    assert double_the_difference([1, 3, 2, 0, "a", 1.5]) == 10

def test_negative_and_non_integer():
    assert double_the_difference([-1, -2, 0, 3.5]) == 0

# Focus: Logic Branches
def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_mixed_positive_negative_and_zero():
    assert double_the_difference([1, 3, 2, 0, -1]) == 10