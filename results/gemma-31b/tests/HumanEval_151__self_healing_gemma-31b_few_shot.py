
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
    return sum(x**2 for x in lst if type(x) is int and x >= 0 and x % 2 != 0)

import pytest

def test_double_the_difference_basic():
    """Test basic functionality based on provided examples."""
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    """Test with an empty list."""
    assert double_the_difference([]) == 0

def test_double_the_difference_all_even():
    """Test with a list containing only even numbers."""
    assert double_the_difference([2, 4, 6, 8, 10]) == 0

def test_double_the_difference_all_odd():
    """Test with a list containing only positive odd numbers."""
    # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([1, 3, 5]) == 35

def test_double_the_difference_mixed_types():
    """Test that non-integers are ignored."""
    # 1^2 + 5^2 = 1 + 25 = 26. Floats and strings should be ignored.
    assert double_the_difference([1, 3.5, "3", None, 5, [1]]) == 26

def test_double_the_difference_negative_odds():
    """Test that negative odd numbers are ignored."""
    # Only 7 is a positive odd integer. 7^2 = 49.
    assert double_the_difference([-1, -3, -5, 7]) == 49

def test_double_the_difference_large_numbers():
    """Test with larger odd numbers."""
    # 101^2 = 10201
    assert double_the_difference([101]) == 10201

@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 1, 1], 3),
    ([2, 2, 2], 0),
    ([1, 2, 3, 4, 5], 35), # 1+9+25
    ([-10, -20, -30], 0),
    ([1.1, 3.3, 5.5], 0),
])
def test_double_the_difference_parametrized(input_list, expected_output):
    """Parametrized tests for various scenarios."""
    assert double_the_difference(input_list) == expected_output