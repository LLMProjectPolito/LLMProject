
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

def test_list_with_only_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_list_with_only_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_list_with_mixed_positive_and_negative_numbers():
    assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25

def test_list_with_floats():
    assert double_the_difference([1.5, 2.0, 3.7]) == 0

def test_list_with_valid_and_invalid_inputs():
    assert double_the_difference([1, 2.5, -3, 4, 5]) == 1 + 25

def test_list_with_zero():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_list_with_odd_numbers():
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49

def test_example_cases():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0