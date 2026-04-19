
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

def test_double_diff_basic():
    """Test standard cases with positive odds, evens, and zeros."""
    assert double_the_difference([1, 3, 2, 0]) == 10  # 1^2 + 3^2
    assert double_the_difference([9, -2]) == 81       # 9^2
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6]) == 0      # No odds

def test_double_diff_negatives():
    """Test that negative numbers are ignored."""
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([-3, 3]) == 9        # Only positive 3 is counted

def test_double_diff_empty():
    """Test that an empty list returns 0."""
    assert double_the_difference([]) == 0

def test_double_diff_floats():
    """Verify that non-integers (floats) are ignored."""
    # 1^2 + 5^2 = 26; 3.0 should be ignored even though it is numerically odd
    assert double_the_difference([1, 3.0, 5]) == 26

def test_double_diff_booleans():
    """Verify that booleans are ignored (since True is an instance of int)."""
    # 1^2 + 3^2 = 10; True should be ignored
    assert double_the_difference([1, True, 3]) == 10

def test_double_diff_mixed_types():
    """Ensure the function doesn't crash when encountering non-numeric types."""
    # 1^2 + 3^2 = 10; "a" and None should be ignored
    assert double_the_difference([1, "a", None, 3]) == 10