
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
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49 == 84

def test_mixed_even_and_odd_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 == 10

def test_list_with_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_list_with_zero():
    assert double_the_difference([0]) == 0

def test_list_with_single_odd_number():
    assert double_the_difference([1]) == 1

def test_list_with_single_even_number():
    assert double_the_difference([2]) == 0

def test_list_with_large_numbers():
    assert double_the_difference([1000000, 2000001]) == 1000000000000 + 400000000001 == 400000000001000000

def test_list_with_floating_point_numbers():
    assert double_the_difference([1.0, 2.0, 3.0]) == 0