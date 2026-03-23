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
        if isinstance(num, int) and num % 2 != 0:
            total += num * num
    return total

def test_empty_list():
    assert double_the_difference([]) == 0

def test_list_with_only_zeros():
    assert double_the_difference([0, 0, 0]) == 0

def test_list_with_negative_and_zero():
    assert double_the_difference([-1, -2, 0]) == 0

def test_list_with_mixed_positive_and_negative_odd():
    assert double_the_difference([1, -3, 5, -7]) == 1 + 9 + 25 + 49