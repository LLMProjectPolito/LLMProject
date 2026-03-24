
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
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_positive_and_negative_numbers():
    assert double_the_difference([9, -2]) == 81

def test_zero_and_odd_numbers():
    assert double_the_difference([0, 1, 3]) == 10

def test_only_zero():
    assert double_the_difference([0]) == 0

def test_large_numbers():
    assert double_the_difference([1001, 1003]) == 2006005

def test_list_with_non_integers():
    assert double_the_difference([1.5, 2, 3]) == 9

def test_list_with_negative_non_integers():
    assert double_the_difference([-1.5, 2, -3]) == 0

def test_list_with_mixed_types_and_odd_numbers():
    assert double_the_difference([1, "a", 3, 2.5, -1]) == 10