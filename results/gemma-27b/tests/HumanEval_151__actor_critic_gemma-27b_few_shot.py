
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
    
    >>> double_the_difference([1, 3, 2, 0])
    10
    >>> double_the_difference([-1, -2, 0])
    0
    >>> double_the_difference([9, -2])
    81
    >>> double_the_difference([0])
    0
    
    If the input list is empty, return 0.
    >>> double_the_difference([])
    0
    '''
    if not lst:
        return 0
    
    total = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            total += num * num
    return total

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_floats():
    assert double_the_difference([1.0, 3.0, 2.5, 0.0]) == 0

def test_double_the_difference_strings():
    assert double_the_difference(['1', '3', '2', '0']) == 0

def test_double_the_difference_mixed_types():
    assert double_the_difference([1, 3, 2.5, '0']) == 10

def test_double_the_difference_large_numbers():
    assert double_the_difference([101, 103, 105]) == 101**2 + 103**2 + 105**2

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_single_odd():
    assert double_the_difference([5]) == 25

def test_double_the_difference_varied_mixed():
    assert double_the_difference([1, -2, 3, 'a', 5, 4.5, 0, -1]) == 1 + 9 + 25

def test_double_the_difference_large_list():
    large_list = list(range(1, 1000, 2))  # List of odd numbers from 1 to 999
    expected_sum = sum(x**2 for x in large_list)
    assert double_the_difference(large_list) == expected_sum