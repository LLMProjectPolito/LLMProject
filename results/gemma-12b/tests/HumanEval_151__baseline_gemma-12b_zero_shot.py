
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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_mixed_positive_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_negative_and_positive_mixed():
    assert double_the_difference([-1, 2, 3, -4, 5]) == 1 + 9 + 25

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_all_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_single_negative_number():
    assert double_the_difference([-5]) == 0

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_floats_and_strings():
    assert double_the_difference([1.5, "a", 3]) == 9

def test_complex_list():
    assert double_the_difference([1, 3, 2, 0, -1, -2, 5]) == 1 + 9 + 25

def test_large_numbers():
    assert double_the_difference([101, 303, 505]) == 10201 + 91809 + 255025

def test_list_with_only_negative_and_non_integer():
    assert double_the_difference([-1, -2.5, "abc"]) == 0