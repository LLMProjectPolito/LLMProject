
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
    ([1, 3, 2, 0], 10),        # Basic case: 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),          # Negative numbers and zero ignored
    ([9, -2], 81),             # Single positive odd, one negative even
    ([0], 0),                  # Single zero
    ([], 0),                   # Empty list
    ([1, 3, 5], 35),           # All positive odds: 1 + 9 + 25 = 35
    ([2, 4, 6], 0),            # All positive evens
    ([-1, -3, -5], 0),         # All negative odds
    ([1.5, 3.0, 2.1], 0),      # Non-integers (floats) ignored
    ([1, "a", None, 3], 10),   # Mixed types (non-integers) ignored
    ([101], 10201),            # Large odd number
    ([7, 11], 49 + 121),       # Multiple odds: 170
    ([0, -1, 2, -3, 4, -5], 0),# Mix of zero, negative odds, and positive evens
])
def test_double_the_difference(lst, expected):
    assert double_the_difference(lst) == expected