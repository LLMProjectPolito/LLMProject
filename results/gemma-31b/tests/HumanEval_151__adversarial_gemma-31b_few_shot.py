
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

def test_double_the_difference_basic():
    """Tests standard cases provided in the docstring."""
    assert double_the_difference([1, 3, 2, 0]) == 10  # 1^2 + 3^2
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    """Tests that an empty list returns 0."""
    assert double_the_difference([]) == 0

def test_double_the_difference_all_even():
    """Tests that a list of only even positive numbers returns 0."""
    assert double_the_difference([2, 4, 6, 8, 10]) == 0

def test_double_the_difference_all_odd():
    """Tests a list containing only positive odd numbers."""
    # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([1, 3, 5]) == 35

def test_double_the_difference_type_safety():
    """
    Tests that non-integer types are ignored.
    This is a critical 'Blue Team' check to ensure the function doesn't crash 
    when encountering unexpected types (strings, floats, None).
    """
    # 3.0 is a float, not an int. "5" is a string. None is None.
    # Only 1 and 7 should be counted: 1^2 + 7^2 = 1 + 49 = 50
    assert double_the_difference([1, 3.0, "5", None, 7, [1]]) == 50

def test_double_the_difference_negative_odds():
    """Tests that negative odd numbers are explicitly ignored."""
    # -1 and -3 are odd, but negative, so they must be ignored.
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_large_numbers():
    """Tests the function with larger integers to ensure no overflow/performance issues."""
    # 1001^2 = 1002001
    assert double_the_difference([1001]) == 1002001

@pytest.mark.parametrize("input_list, expected", [
    ([1, 1, 1], 3),             # Duplicate odds
    ([0, 0, 0], 0),             # Multiple zeros
    ([1.1, 2.2, 3.3], 0),       # All floats
    (["1", "3"], 0),            # Numeric strings
    ([True, False], 1),         # Booleans (In Python, True == 1, which is odd) 
                                # Note: Depending on strictness, True might be 
                                # considered an int. This test checks behavior.
])
def test_double_the_difference_edge_cases(input_list, expected):
    """Parametrized test for various edge cases."""
    assert double_the_difference(input_list) == expected