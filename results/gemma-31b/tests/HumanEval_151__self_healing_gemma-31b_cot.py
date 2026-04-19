
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
    return sum(x**2 for x in lst if type(x) is int and x >= 0 and x % 2 != 0)

import pytest

def test_provided_examples():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_even_positive():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_all_odd_positive():
    # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([1, 3, 5]) == 35

def test_negative_odds():
    # Negative odds should be ignored
    assert double_the_difference([-1, -3, -5]) == 0

def test_non_integer_types():
    # Floats and other types should be ignored
    assert double_the_difference([1.0, 3.0, 5.5, 2.1]) == 0
    assert double_the_difference(["1", "3", None, [], {}]) == 0

def test_mixed_types_and_values():
    # Only 1, 3, 7 are positive odd integers: 1^2 + 3^2 + 7^2 = 1 + 9 + 49 = 59
    mixed_list = [1, 3, 2, 0, -1, -3, 7, 4.5, "odd", None]
    assert double_the_difference(mixed_list) == 59

def test_large_numbers():
    # 101^2 = 10201
    assert double_the_difference([101]) == 10201

def test_zero_handling():
    assert double_the_difference([0, 0, 0]) == 0