
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

@pytest.mark.parametrize("input_list, expected", [
    ([1, 3, 2, 0], 10),        # Basic case: 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),          # Negative numbers ignored
    ([9, -2], 81),             # Only 9 is odd and positive
    ([0], 0),                  # Zero is even
    ([], 0),                   # Empty list
    ([2, 4, 6, 8], 0),         # All even
    ([1, 3, 5], 35),           # All odd: 1 + 9 + 25 = 35
    ([1, 3, 5, 7, 9], 165),    # Sequence of odd numbers: 1+9+25+49+81 = 165
    ([7, -7, 11, -11], 170),   # Mixed positives and negatives: 49 + 121 = 170
    ([0, 0, 0], 0),            # Multiple zeros
    ([101], 10201),            # Single large odd number
    ([1001, 1], 1002002),      # Large odd numbers
    ([1], 1),                  # Single odd
    ([2], 0),                  # Single even
    ([-1], 0),                 # Single negative odd
])
def test_double_the_difference_parametrized(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_double_the_difference_types():
    """Test that non-integer types are ignored."""
    # Floats, strings, and None should be ignored
    assert double_the_difference([1, 2.5, 3]) == 10
    assert double_the_difference([1, "3", 5]) == 26
    assert double_the_difference([1, None, 3]) == 10
    assert double_the_difference([1.0, 3.0, 5.0]) == 0
    assert double_the_difference(["1", "3", "5"]) == 0
    # Booleans are technically ints in Python, but usually excluded in strict integer checks
    assert double_the_difference([None, True, False]) == 0

def test_double_the_difference_mixed_complex():
    """Test a variety of invalid types mixed with valid odd integers."""
    input_list = [1, 2, 3, -1, 3.0, "7", 5, -3, None, [], {}, True]
    # Valid odds: 1, 3, 5 -> 1 + 9 + 25 = 35
    assert double_the_difference(input_list) == 35

def test_double_the_difference_iterable():
    """Test behavior with non-list iterables like tuples."""
    assert double_the_difference((1, 3, 2)) == 10