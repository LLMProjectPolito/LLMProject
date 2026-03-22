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
            sum_of_squares += num**2
    return sum_of_squares

def test_double_the_difference_positive():
    assert double_the_difference([1, 2, 3]) == 10
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 1
    assert double_the_difference([-1, 2, -3]) == 1
    assert double_the_difference([1, -2, 3]) == 1
    assert double_the_difference([-1, 2, -3]) == 1

def test_double_the_difference_mixed():
    assert double_the_difference([1, 2, -3, 4]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, 5]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, -5]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, 5, -6]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, 5, -6, 7]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, 5, -6, 7, 8]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, 5, -6, 7, 8, 9]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, 5, -6, 7, 8, 9, 10]) == 1 + 9 + 16
    assert double_the_difference([1, 2, -3, 4, 5, -6, 7, 8, 9, 10, 11]) == 1 + 9 + 16
    assert double_the_difference([]) == 0