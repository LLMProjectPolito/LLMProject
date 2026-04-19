
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

# The function double_the_difference is already defined in the environment.

@pytest.mark.parametrize("input_lst, expected", [
    ([1, 3, 2, 0], 10),   # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),     # All negative or even
    ([9, -2], 81),        # 9^2 = 81
    ([0], 0),             # Zero is even
    ([], 0),              # Empty list
])
def test_docstring_examples(input_lst, expected):
    """Verify the examples explicitly provided in the function docstring."""
    assert double_the_difference(input_lst) == expected

@pytest.mark.parametrize("input_lst", [
    ([]), 
    ([0]), 
    ([0, 0, 0]),
])
def test_empty_and_zero_cases(input_lst):
    """Verify that empty lists or lists containing only zeros return 0."""
    assert double_the_difference(input_lst) == 0

@pytest.mark.parametrize("input_lst, expected", [
    ([1], 1),               # Single odd: 1^2
    ([1, 1, 1], 3),         # Multiple identical odds: 1^2 + 1^2 + 1^2
    ([1, 3, 5], 35),        # Multiple distinct odds: 1^2 + 3^2 + 5^2 = 1 + 9 + 25
    ([7, 11], 170),         # Larger odds: 49 + 121 = 170
])
def test_positive_odd_logic(input_lst, expected):
    """Ensure only positive odd integers are squared and summed."""
    assert double_the_difference(input_lst) == expected

@pytest.mark.parametrize("input_lst", [
    ([2, 4, 6, 8],),        # Only positive evens
    ([-1, -3, -5],),        # Only negative odds
    ([-2, -4, -6],),        # Only negative evens
    ([-1, -2, -3],),        # Mixed negatives
])
def test_invalid_integer_filtering(input_lst):
    """Ensure positive evens and all negative numbers are ignored."""
    # Note: input_lst is passed as a tuple of lists in parametrize to avoid 
    # pytest interpreting the list as multiple test cases.
    for lst in input_lst:
        assert double_the_difference(lst) == 0

@pytest.mark.parametrize("input_lst, expected", [
    ([3.0, 5.0], 0),        # Floats that look like odds
    ([1, 3.5, 3], 10),      # Mixed int and float: 1^2 + 3^2
    (["1", "3"], 0),        # Strings
    ([None], 0),            # NoneType
    ([True, False], 0),     # Booleans (should be ignored as they are not strictly 'integers' in this context)
    ([1.1, 3.3, 5.5], 0),   # All floats
])
def test_non_integer_type_filtering(input_lst, expected):
    """Ensure non-integer types (floats, strings, None, bools) are ignored."""
    assert double_the_difference(input_lst) == expected

@pytest.mark.parametrize("input_lst, expected", [
    ([101], 10201),         # 101^2
    ([1001], 1002001),       # 1001^2
    ([101, 103], 20810),    # 10201 + 10609
    ([1001, 1003], 2008010),# 1002001 + 1006009
])
def test_large_integers(input_lst, expected):
    """Verify the function handles larger odd integers correctly."""
    assert double_the_difference(input_lst) == expected

def test_comprehensive_mixed_scenario():
    """
    A comprehensive test combining all constraints:
    - Positive Odds: 1, 3, 5 (1+9+25 = 35)
    - Positive Evens: 2, 4 (Ignore)
    - Negative Odds: -1, -3 (Ignore)
    - Negative Evens: -2 (Ignore)
    - Non-ints: 3.0, "5", None, True (Ignore)
    - Zero: 0 (Ignore)
    """
    mixed_list = [1, -1, 2, 3, 3.0, "5", None, 5, -3, 0, 4, -2, True]
    # Expected: 1^2 + 3^2 + 5^2 = 35
    assert double_the_difference(mixed_list) == 35