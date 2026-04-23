
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

def test_double_the_difference_provided_examples():
    """Tests the specific examples provided in the docstring."""
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty_list():
    """Tests that an empty list returns 0."""
    assert double_the_difference([]) == 0

def test_double_the_difference_only_even():
    """Tests a list containing only even integers."""
    assert double_the_difference([2, 4, 6, 8, 0]) == 0

def test_double_the_difference_only_negative():
    """Tests a list containing only negative integers."""
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_non_integers():
    """Tests that floats are ignored even if they are mathematically 'odd' (e.g., 3.0)."""
    # 3.0 is a float, not an int, so it should be ignored.
    assert double_the_difference([1, 3.0, 5]) == 1 + 25  # 1^2 + 5^2 = 26
    assert double_the_difference([3.5, 7.1]) == 0

def test_double_the_difference_mixed_types():
    """Tests a mix of valid odd integers, even integers, negatives, and floats."""
    # Valid: 1 (1^2=1), 5 (5^2=25), 7 (7^2=49)
    # Invalid: -3 (negative), 4 (even), 2.0 (float), 0 (even)
    assert double_the_difference([1, -3, 4, 5, 2.0, 0, 7]) == 1 + 25 + 49

def test_double_the_difference_large_numbers():
    """Tests with larger integer values."""
    assert double_the_difference([11, 13]) == 121 + 169

def test_double_the_difference_all_invalid():
    """Tests a list where no elements meet the criteria."""
    assert double_the_difference([-2, -4, 2, 4, 0, 0.5]) == 0