
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

# The function is assumed to be defined as provided in the problem description.
# from solution import double_the_difference 

@pytest.mark.parametrize("input_data, expected", [
    ([1, 3, 2, 0], 10),           # Basic: 1^2 + 3^2 = 10
    ([9, -2], 81),                # Single positive odd
    ([10**12 + 1], (10**12 + 1)**2), # Large odd integer
    ([1, 10**12 + 3], 1 + (10**12 + 3)**2), # Mixed large and small
    ([], 0),                      # Empty list
])
def test_positive_odd_integers(input_data, expected):
    """Test valid positive odd integers and large number precision."""
    assert double_the_difference(input_data) == expected

@pytest.mark.parametrize("input_data", [
    ([0]),                        # Zero
    ([0, 0, 0]),                  # Multiple zeros
    ([-1, -3, -5]),               # Negative odds
    ([-2, -4, -6]),               # Negative evens
    ([2, 4, 6, 8]),               # Positive evens
    ([-1, -2, 0]),                # Mix of non-positive/even
])
def test_ignored_integers(input_data):
    """Test that evens, negatives, and zeros are ignored (should return 0)."""
    assert double_the_difference(input_data) == 0

@pytest.mark.parametrize("input_data", [
    ([1.0, 3.0, 5.0]),             # Floats (even if whole numbers)
    ([1.5, 3.7]),                  # Standard floats
    (["1", "3"]),                  # Strings
    ([None]),                      # NoneType element
    ([True, False]),               # Booleans: Strict type check required (bool is subclass of int)
])
def test_non_integer_elements(input_data):
    """
    Test that non-integer types are strictly ignored.
    Note: This validates that the implementation uses `type(x) is int` 
    rather than `isinstance(x, int)` to exclude booleans.
    """
    assert double_the_difference(input_data) == 0

@pytest.mark.parametrize("invalid_input", [
    None, 
    123, 
    True, 
    4.5
])
def test_invalid_input_types(invalid_input):
    """Test behavior when the entire input is not an iterable."""
    # Since the function expects to iterate over 'lst', 
    # passing a non-iterable should raise a TypeError.
    with pytest.raises(TypeError):
        double_the_difference(invalid_input)

def test_iterable_types():
    """Test that the function handles various iterable types correctly."""
    assert double_the_difference((1, 3, 2)) == 10          # Tuple
    assert double_the_difference({1, 3, 5}) == 35          # Set
    assert double_the_difference((x for x in [1, 3, 2])) == 10 # Generator

def test_mixed_comprehensive():
    """Test a complex list containing a mix of all possible edge cases."""
    # Valid: 1, 3, 5 -> 1^2 + 3^2 + 5^2 = 35
    # Ignored: 2 (even), -1 (neg), 3.0 (float), "7" (str), -4 (neg even), 0 (even), True (bool)
    mixed_list = [1, 2, -1, 3, 3.0, "7", 5, -4, 0, True]
    assert double_the_difference(mixed_list) == 35