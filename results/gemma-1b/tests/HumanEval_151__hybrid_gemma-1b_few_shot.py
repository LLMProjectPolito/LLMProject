
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
    if not lst:
        return 0
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_double_the_difference_positive():
    assert double_the_difference([1, 2, 3]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([1, 2, -3, 4]) == 1 + 9 + 16
    assert double_the_difference([2, 4, 6]) == 4 + 16
    assert double_the_difference([1, 3, 5]) == 1 + 9
    assert double_the_difference([1, 2, 3, 4, 5, 6]) == 1 + 9 + 16 + 25
    assert double_the_difference([1, 2, 3, 4, 5, 6, 7]) == 1 + 9 + 16 + 25 + 36
    assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 9 + 16 + 25 + 36 + 49
    assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1 + 9 + 16 + 25 + 36 + 49
    assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 9 + 16 + 25 + 36 + 49 + 64
    assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 1 + 9 + 16 + 25 + 36 + 49 + 64
    assert double_the_difference([]) == 0

### Problem:
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """

### Tests (Pytest):