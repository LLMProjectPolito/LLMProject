
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

@pytest.mark.parametrize("input_list, expected_output", [
    # Provided examples
    ([1, 3, 2, 0], 10),    # 1^2 + 3^2 = 1 + 9 = 10
    ([-1, -2, 0], 0),      # -1 is odd but negative, ignore
    ([9, -2], 81),         # 9^2 = 81
    ([0], 0),              # 0 is even
    ([], 0),               # Empty list returns 0
    
    # Edge cases: No odd numbers
    ([2, 4, 6, 8], 0),
    ([0, 2, 4], 0),
    
    # Edge cases: Only negative odd numbers
    ([-1, -3, -5], 0),
    ([-7, -2, -4], 0),
    
    # Edge cases: Non-integer types (should be ignored)
    ([1, 3.0, 5], 26),     # 1^2 + 5^2 = 26 (3.0 is float)
    ([1.1, 3.3, 5.5], 0),  # All floats
    (["1", "3", 5], 25),   # "1" and "3" are strings, 5^2 = 25
    ([None, 1, 3], 10),    # None is not an integer
    ([True, 1, 3], 11),    # True is an instance of int (1), 1^2 + 1^2 + 3^2 = 11
    
    # Edge cases: Mixed valid and invalid
    ([1, -1, 3, -3, 2, -2, 0], 10), # 1^2 + 3^2 = 10
    ([101], 10201),                # Large odd number
    ([1, 3, 5, 7], 1 + 9 + 25 + 49), # 84
])
def test_double_the_difference(input_list, expected_output):
    """
    Tests the double_the_difference function with various scenarios including
    provided examples, empty lists, negative numbers, non-integers, and mixed types.
    """
    assert double_the_difference(input_list) == expected_output

def test_double_the_difference_large_list():
    """Test with a larger list of odd numbers."""
    lst = [1] * 100  # 100 ones
    # Sum of 1^2 for 100 elements = 100
    assert double_the_difference(lst) == 100

def test_double_the_difference_all_invalid():
    """Test with a list containing no valid positive odd integers."""
    lst = [-1, -3, 2.2, "7", None, False]
    # False is 0 (even), others are negative or non-int
    assert double_the_difference(lst) == 0