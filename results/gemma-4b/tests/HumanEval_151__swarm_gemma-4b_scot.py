
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
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            total += num * num
    return total

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_negative_zero():
    assert double_the_difference([-1, 2, 0, 3]) == 10

def test_only_zeroes():
    assert double_the_difference([0, 0, 0]) == 0

def test_single_odd_positive():
    assert double_the_difference([1]) == 1

def test_single_even_positive():
    assert double_the_difference([2]) == 0

def test_single_negative():
    assert double_the_difference([-1]) == 0

def test_large_numbers():
    assert double_the_difference([1001, 1003]) == 1001*1001 + 1003*1003

def test_single_zero():
    assert double_the_difference([0]) == 0