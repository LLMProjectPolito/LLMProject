
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

@pytest.mark.parametrize("input_data, expected", [
    # Basic cases from prompt
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    # Edge cases: Empty and All Even
    ([], 0),
    ([0, 2, 4, 6, 8], 0),
    # Edge cases: All Odd and Negatives (Negative odds are ignored per requirements)
    ([1, 3, 5], 35),
    ([-1, -3, -5], 0),
    ([1, -1, 3, -3], 10),
    # Type handling: Non-integers (floats, strings, None)
    ([1.5, 3.0, 5.5], 0),
    (["1", "3", "5"], 0),
    ([None], 0),
    # Mixed types
    ([1, "a", 3.0, -5, 7, None], 50),
    # Large values to ensure arbitrary-precision handling
    ([10**10 + 1], (10**10 + 1)**2),
    # Input Type Flexibility: Other iterables
    ((1, 3, 2), 10),
    ({1, 3, 2}, 10),
])
def test_sum_squares_positive_odds_scenarios(input_data, expected):
    """
    Tests the sum of squares of positive odd integers across various 
    input values, types, and iterable structures.
    """
    assert double_the_difference(input_data) == expected

def test_sum_squares_positive_odds_boolean_handling():
    """
    Explicitly test that booleans are ignored.
    In Python, isinstance(True, int) is True, so the implementation 
    must use type(x) is int to correctly exclude booleans.
    """
    # True is treated as 1 (odd), False as 0 (even). Both should be ignored.
    assert double_the_difference([True, False]) == 0
    assert double_the_difference([1, True]) == 1  # Only the integer 1 should be squared

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    45.67
])
def test_sum_squares_positive_odds_non_iterable_input(invalid_input):
    """
    Verify that non-iterable inputs raise a TypeError.
    """
    with pytest.raises(TypeError):
        double_the_difference(invalid_input)