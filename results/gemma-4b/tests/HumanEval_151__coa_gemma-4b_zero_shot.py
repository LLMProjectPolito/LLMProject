
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
import pytest

def test_double_the_difference_positive_odd():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative_and_zero():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_positive_only():
    assert double_the_difference([9, -2]) == 81

# Focus: Type Scenarios
import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_no_odd_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_only_odd_positive_numbers():
    assert double_the_difference([1, 3, 5]) == 35

# Focus: Logic Branches
import pytest

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_positive_odd():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_double_the_difference_mixed_positive_negative():
    assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25

def test_double_the_difference_all_negative_odd():
    assert double_the_difference([-1, -3, -5]) == 1 + 9 + 25

def test_double_the_difference_no_odd_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_double_the_difference_zero_and_odd():
    assert double_the_difference([0, 1, 3]) == 1 + 9