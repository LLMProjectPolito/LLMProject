import pytest

def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    """
    if not lst:
        return 0
    
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

import sys
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_positive_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_mixed_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 4
    
def test_double_the_difference_single_odd_number():
    assert double_the_difference([1]) == 1

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_double_the_difference_negative_odd():
    assert double_the_difference([-1, -3, -5]) == 9