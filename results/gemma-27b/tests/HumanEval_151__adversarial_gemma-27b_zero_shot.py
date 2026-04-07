
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

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_positive_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_positive_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_and_negative():
    assert double_the_difference([1, -2, 3, -4]) == 10

def test_zero():
    assert double_the_difference([0]) == 0

def test_single_odd_number():
    assert double_the_difference([9]) == 81

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_floats_and_integers():
    assert double_the_difference([1, 2.5, 3, 4.0]) == 10

def test_strings_and_integers():
    assert double_the_difference([1, "2", 3, "4"]) == 10

def test_mixed_types():
    assert double_the_difference([1, 3.14, -2, "hello", 5]) == 1 + 25

def test_large_numbers():
    assert double_the_difference([101, 103]) == 101**2 + 103**2

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0