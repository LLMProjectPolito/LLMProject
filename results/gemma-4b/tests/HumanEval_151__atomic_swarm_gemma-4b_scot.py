
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

import pytest

def test_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([-1, 3, -5, 7]) == 1 + 9 + 25 + 49

def test_zeroes_and_odds():
    assert double_the_difference([1, 3, 0, 5]) == 1 + 9 + 25

def test_only_zeroes():
    assert double_the_difference([0, 0, 0]) == 0

def test_negative_limits():
    assert double_the_difference([-1, -2, -3]) == 0

def test_large_numbers():
    assert double_the_difference([1001, 1003, 1002]) == 1001001 + 1003003

def test_single_odd_number():
    assert double_the_difference([5]) == 25

def test_single_negative_odd_number():
    assert double_the_difference([-5]) == 25

def test_single_zero():
    assert double_the_difference([0]) == 0

import pytest

def test_empty_list():
    assert double_the_difference([]) == 0