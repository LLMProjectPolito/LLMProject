
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

def test_all_negative_numbers():
    assert double_the_difference([-2, -4, -6]) == 0

def test_mixed_positive_negative_and_zero():
    assert double_the_difference([-1, 0, 2, 3, -4, 5]) == 1 + 9 + 25

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2, 3.0, 4]) == 0

def test_string_in_list():
    assert double_the_difference([1, "a", 3]) == 1 + 9

def test_complex_number_in_list():
    assert double_the_difference([1, 2+1j, 3]) == 1 + 9

def test_large_numbers():
    assert double_the_difference([1001, 1003]) == 1001**2 + 1003**2

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([4]) == 0

def test_single_negative_number():
    assert double_the_difference([-5]) == 0

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81