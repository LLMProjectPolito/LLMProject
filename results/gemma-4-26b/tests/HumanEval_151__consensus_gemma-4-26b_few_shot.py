
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

@pytest.mark.parametrize("lst, expected", [
    ([], 0),                                # Empty list
    ([1, 3, 2, 0], 10),                     # Docstring example 1 (1^2 + 3^2)
    ([-1, -2, 0], 0),                       # Docstring example 2 (No non-negative odd integers)
    ([9, -2], 81),                          # Docstring example 3 (9^2)
    ([0], 0),                               # Docstring example 4
    ([1, 2, 3, 4, 5], 35),                  # Standard sequence (1 + 9 + 25)
    ([2, 4, 6, 8], 0),                      # All even
    ([0, 2, 4, 6], 0),                      # Even numbers including zero
    ([-5, -3, -1], 0),                      # All negative odd integers
    ([1, 3, 5, 7], 84),                     # All positive odd integers (1 + 9 + 25 + 49)
    ([1, 3, 5.0, 7], 59),                   # Ignore float 5.0 (not an int) -> 1 + 9 + 49
    ([1, 2, 3.0, 4, 5], 26),                # Ignore float 3.0 -> 1 + 25
    ([1, 2.5, 3, 4.0, 5], 35),              # Mixed with floats (2.5 and 4.0 are ignored)
    ([1.1, 3.3, 5.5], 0),                   # All floats
    ([11], 121),                            # Single odd number
    ([101], 10201),                         # Single large odd number
    ([1, 1, 1], 3),                         # Duplicate odd numbers
    ([1, -1, 1], 2),                        # Ignore negative odd
    ([1, -1, 3, -3, 5, -5], 35),            # Mixed positive and negative odd integers
])
def test_double_the_difference(lst, expected):
    """
    Tests the double_the_difference function with various inputs including:
    - Empty lists
    - Lists with only odd, only even, or only negative numbers
    - Mixed lists of integers, floats, and negative numbers
    - Lists with duplicate values and large integers
    """
    assert double_the_difference(lst) == expected