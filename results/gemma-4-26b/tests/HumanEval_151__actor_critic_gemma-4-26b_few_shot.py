
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

# Note: The function name is 'sum_squares_of_positive_odds' 
# to accurately reflect its behavior.

def test_provided_examples():
    """Tests the examples provided in the docstring."""
    assert sum_squares_of_positive_odds([1, 3, 2, 0]) == 10
    assert sum_squares_of_positive_odds([-1, -2, 0]) == 0
    assert sum_squares_of_positive_odds([9, -2]) == 81
    assert sum_squares_of_positive_odds([0]) == 0

def test_empty_list():
    """Tests that an empty list returns 0."""
    assert sum_squares_of_positive_odds([]) == 0

def test_type_filtering():
    """
    Consolidated test: Verifies that non-integers (floats, strings, None, etc.) 
    are correctly ignored, even if they represent whole numbers.
    """
    # 1.0 and 3.0 are floats (ignored)
    # 5 and 1 are positive odd integers (included)
    # 3.5 is a float (ignored)
    # "3" is a string (ignored)
    # None and [5] are non-numeric (ignored)
    # 3 is a positive odd integer (included)
    input_data = [1.0, 3.0, 5, 1, 3.5, "3", None, [5], 3]
    # Expected: 5^2 + 1^2 + 3^2 = 25 + 1 + 9 = 35
    assert sum_squares_of_positive_odds(input_data) == 35

def test_boolean_edge_case():
    """
    Tests how booleans are handled. 
    Since bool is a subclass of int in Python, True is treated as 1 and False as 0.
    """
    assert sum_squares_of_positive_odds([True, 3]) == 10 # 1^2 + 3^2
    assert sum_squares_of_positive_odds([False, 5]) == 25 # 5^2

def test_large_numbers():
    """Tests the function with significantly larger odd integers."""
    large_odd_1 = 1000001
    large_odd_2 = 2000001
    expected = (large_odd_1**2) + (large_odd_2**2)
    assert sum_squares_of_positive_odds([large_odd_1, large_odd_2]) == expected

@pytest.mark.parametrize("non_iterable", [None, 5, 1.2, "string"])
def test_non_iterable_input(non_iterable):
    """Tests that passing a non-iterable input raises a TypeError."""
    with pytest.raises(TypeError):
        sum_squares_of_positive_odds(non_iterable)

def test_other_iterables():
    """Tests that the function works with tuples, sets, and generators."""
    assert sum_squares_of_positive_odds((1, 3, 2, 0)) == 10  # Tuple
    assert sum_squares_of_positive_odds({1, 3, 2, 0}) == 10  # Set
    assert sum_squares_of_positive_odds(x for x in [1, 3, 2, 0]) == 10  # Generator

def test_special_float_values():
    """Tests that special float values (inf, nan) are ignored and don't crash the function."""
    assert sum_squares_of_positive_odds([float('inf'), float('nan'), 1, 3]) == 10
    assert sum_squares_of_positive_odds([float('inf')]) == 0

@pytest.mark.parametrize("input_list, expected", [
    ([1, 1, 1], 3),           # Multiple same odd numbers
    ([7], 49),                # Single odd number
    ([2, 4, 6, -1, -3], 0),   # Mix of even and negative
    ([1, 2, 3, 4, 5], 35),    # Standard sequence
    ([-1, -3, -5, -7], 0),    # Only negative numbers
    ([2, 4, 6, 8, 0], 0),     # Only even numbers
])
def test_parameterized_cases(input_list, expected):
    """Comprehensive parameterized testing for various scenarios."""
    assert sum_squares_of_positive_odds(input_list) == expected