
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
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_odd_even_positive():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25 == 35

def test_mixed_odd_even_negative():
    assert double_the_difference([-1, 2, 3, -4, 5]) == 9 + 25 == 34

def test_list_with_zero():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9 == 10

def test_list_with_non_integers():
    assert double_the_difference([1, 2.5, "a", 3]) == 9

def test_single_odd_number():
    assert double_the_difference([5]) == 25

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_large_numbers():
    assert double_the_difference([1001, 2]) == 1002001