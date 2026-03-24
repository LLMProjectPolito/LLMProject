
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
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_floats():
    assert double_the_difference([1.5, 2.0, 3.7]) == 0

def test_mixed_types():
    assert double_the_difference([1, 2.5, "3", 4, 5]) == 26

def test_single_odd():
    assert double_the_difference([5]) == 25

def test_single_even():
    assert double_the_difference([4]) == 0

def test_zero():
    assert double_the_difference([0]) == 0

def test_large_numbers():
    assert double_the_difference([99, 101, 103]) == 9801 + 10201 + 10609