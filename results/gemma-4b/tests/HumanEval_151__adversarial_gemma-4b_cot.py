
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
    total = 0
    for num in lst:
        if isinstance(num, int) and num > 0:
            total += num * num
    return total

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_positive_odd_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative_and_zero():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_positive_and_negative():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_single_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_single_positive():
    assert double_the_difference([5]) == 25

def test_double_the_difference_mixed_positive_negative_zero():
    assert double_the_difference([1, -2, 3, 0, 5]) == 35

def test_double_the_difference_large_numbers():
    assert double_the_difference([1001, 2, 3]) == 1002001

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -2, -3]) == 0

def test_double_the_difference_non_integer_values():
    assert double_the_difference([1, 2.5, 3, "a"]) == 10

def test_double_the_difference_with_negative_odd():
    assert double_the_difference([-1, 3]) == 10