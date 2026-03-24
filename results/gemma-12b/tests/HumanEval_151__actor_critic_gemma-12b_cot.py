
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
        if isinstance(num, int) and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty():
    assert double_the_difference([]) == 0

def test_basic():
    assert double_the_difference([1, 3, 5]) == 35
    assert double_the_difference([2, 4, 6]) == 0
    assert double_the_difference([1, 2, 3, 4, 5]) == 35
    assert double_the_difference([0]) == 0
    assert double_the_difference([0, 1, 2, 3, 4, 5]) == 35
    assert double_the_difference([7]) == 49
    assert double_the_difference([8]) == 0

def test_negative_and_non_integer():
    assert double_the_difference([-1, -2, -3]) == 0
    assert double_the_difference([-1, 2, 3, -4, 5]) == 34
    assert double_the_difference([1.5, 2, 3.5, 4]) == 0
    assert double_the_difference([1, 2.5, 3, 4.5, 5]) == 35
    assert double_the_difference([-1.5, -2, -3.5]) == 0
    assert double_the_difference([1.5, 2.5, 3.5]) == 0

def test_large_numbers():
    assert double_the_difference([101, 203]) == 51410
    assert double_the_difference([10001, 20003]) == 500100002