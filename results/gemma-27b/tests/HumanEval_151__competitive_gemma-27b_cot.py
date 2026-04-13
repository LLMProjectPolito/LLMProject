
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

def test_positive_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_positive_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_mixed_positive_and_negative_numbers():
    assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25

def test_zeroes():
    assert double_the_difference([0, 0, 0]) == 0

def test_mixed_numbers_with_zeroes():
    assert double_the_difference([1, 0, 3, 0, 5]) == 1 + 9 + 25

def test_float_numbers():
    assert double_the_difference([1.0, 3.0, 2.0]) == 1 + 9

def test_mixed_integer_and_float_numbers():
    assert double_the_difference([1, 3.0, 2, 5.0]) == 1 + 9 + 25

def test_string_numbers():
    assert double_the_difference(['1', '3', '2']) == 0

def test_mixed_numbers_and_strings():
    assert double_the_difference([1, '3', 2, '5']) == 1

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81

def test_example_4():
    assert double_the_difference([0]) == 0