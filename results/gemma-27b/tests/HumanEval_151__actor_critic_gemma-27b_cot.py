
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
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    total = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            total += num * num
    return total

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_negative():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([-1, 1, -2, 3]) == 10

def test_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_all_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_odd_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 10

def test_only_zero():
    assert double_the_difference([0]) == 0

def test_large_numbers():
    assert double_the_difference([101, 203, 305]) == 101**2 + 203**2 + 305**2

def test_mixed_floats_and_integers():
    assert double_the_difference([1.0, 2, 3.0, 4]) == 0

def test_negative_floats():
    assert double_the_difference([-1.0, -2.0]) == 0

def test_mixed_types():
    assert double_the_difference([1, 2.5, 3, "a"]) == 10

def test_large_positive_number():
    assert double_the_difference([10**9]) == 10**18

def test_large_number_smaller():
    assert double_the_difference([10**6]) == 10**12

def test_large_negative_number():
    assert double_the_difference([-10**9]) == 0

def test_positive_and_large_number():
    assert double_the_difference([1, 10**9]) == 1 + 10**18