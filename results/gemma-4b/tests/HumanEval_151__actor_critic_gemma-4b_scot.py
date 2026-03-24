
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
    total = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            total += num * num
    return total

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `double_the_difference` calculates the sum of squares of odd integers in a list.
# It ignores negative numbers and non-integer numbers. An empty list should return 0.
# We need to test various scenarios including empty lists, lists with only even numbers,
# lists with only odd numbers, lists with mixed positive and negative odd numbers,
# lists with zero, and lists with non-integer values.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list
# test_all_even
# test_all_odd
# test_mixed_positive_negative_odd
# test_with_zero
# test_with_non_integer
# test_single_odd
# test_single_even
# test_negative_odd
# test_positive_odd

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_even():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_all_odd():
    assert double_the_difference([1, 3, 5, 7]) == 85

def test_mixed_positive_negative_odd():
    assert double_the_difference([1, -3, 2, 0, 5]) == 35

def test_with_zero():
    assert double_the_difference([0, 1, 3]) == 10

def test_with_non_integer():
    assert double_the_difference([1, 2.5, 3, "a"]) == 10

def test_single_odd():
    assert double_the_difference([1]) == 1

def test_single_even():
    assert double_the_difference([2]) == 0

def test_negative_odd():
    assert double_the_difference([-1, -3]) == 10

def test_positive_odd():
    assert double_the_difference([1, 3]) == 10