
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

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_mixed_positive_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_negative_and_positive_numbers():
    assert double_the_difference([-1, 1, -2, 2, 3]) == 1 + 9

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_all_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_numbers_with_zero():
    assert double_the_difference([1, -2, 0, 3, -4, 5]) == 1 + 9 + 25

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([4]) == 0

def test_single_negative_number():
    assert double_the_difference([-5]) == 0

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_floats_and_strings():
    assert double_the_difference([1.5, "a", 3]) == 9

def test_complex_list():
    assert double_the_difference([1, 3, 2, 0, -1, -2, 5, 7, "hello", 9.9]) == 1 + 9 + 25 + 49 + 81

def test_large_numbers():
    assert double_the_difference([101, 303, 505]) == 10201 + 91809 + 255025

def test_all_negative_odd_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_mixed_negative_and_even_odd():
    assert double_the_difference([-1, 2, 3, -5, 4, 7]) == 1 + 9 + 49