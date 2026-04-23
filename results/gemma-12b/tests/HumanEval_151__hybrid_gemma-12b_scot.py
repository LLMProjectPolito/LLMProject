
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
    """Checks the behavior with an empty list."""
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    """Checks a list containing only even numbers."""
    assert double_the_difference([2, 4, 6]) == 0

def test_only_odd_numbers():
    """Checks a list containing only odd numbers."""
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_mixed_odd_and_even():
    """Checks a list with a mix of odd and even numbers."""
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    """Checks a list containing negative numbers."""
    assert double_the_difference([-1, -2, -3]) == 0

def test_non_integer_numbers():
    """Checks a list containing non-integer numbers (floats)."""
    assert double_the_difference([1.5, 2.0, 3.7]) == 0

def test_mixed_valid_and_invalid():
    """Checks a list with a mix of valid and invalid numbers."""
    assert double_the_difference([1, -2, 3.0, 5, -6]) == 1 + 25

def test_zero_in_list():
    """Checks a list containing zero."""
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_large_numbers():
    """Checks a list with large odd numbers."""
    assert double_the_difference([1001, 1003]) == 1002001 + 1006009

def test_single_odd_number():
    """Checks a list with a single odd number."""
    assert double_the_difference([7]) == 49

def test_single_even_number():
    """Checks a list with a single even number."""
    assert double_the_difference([2]) == 0

def test_only_negative_numbers():
    """Checks a list containing only negative numbers."""
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_numbers():
    """Checks a list with a mix of positive, negative, and zero."""
    assert double_the_difference([1, 2, 3, -4, 5, 0]) == 1 + 9 + 25