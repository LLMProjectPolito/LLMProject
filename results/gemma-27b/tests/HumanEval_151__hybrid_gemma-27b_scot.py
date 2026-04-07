
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
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num

    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_only_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_only_non_integer_numbers():
    assert double_the_difference([1.5, 2.7, 3.9]) == 0

def test_mixed_valid_and_invalid_numbers():
    assert double_the_difference([1, 2, -3, 4.5, 3, -5, 5]) == 1 + 9 + 25

def test_single_odd_number():
    assert double_the_difference([3]) == 9

def test_multiple_odd_numbers():
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_large_numbers():
    assert double_the_difference([99, 101, 103]) == 9801 + 10201 + 10609

def test_mixed_types():
    assert double_the_difference([1, "2", 3.0, 5, -7]) == 1 + 25