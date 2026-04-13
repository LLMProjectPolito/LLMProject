
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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_odd_numbers():
    assert double_the_difference([-1, -3, -2, 0]) == 0

def test_mixed_positive_negative_odd_even():
    assert double_the_difference([9, -2]) == 81

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_single_odd():
    assert double_the_difference([1]) == 1

def test_single_negative_odd():
    assert double_the_difference([-1]) == 1

def test_mixed_types():
    assert double_the_difference([1, 2.5, 3, -4, "a"]) == 10

def test_all_negative_non_ints():
    assert double_the_difference([-1.5, -2.5, -3.5]) == 0

def test_large_numbers():
    assert double_the_difference([1000000001, 1000000003]) == 2000000002000000001