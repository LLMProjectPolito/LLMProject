
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
    ([1, 3, 2, 0], 10),        # Standard case: 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),          # Negative numbers and zero
    ([9, -2], 81),             # One odd, one negative even
    ([0], 0),                  # Single zero
    ([], 0),                   # Empty list
    ([1, 3, 5], 35),           # All odd: 1 + 9 + 25 = 35
    ([2, 4, 6], 0),            # All even
    ([-1, -3, -5], 0),         # All negative odd
    ([1.5, 3.0, 5.2], 0),      # Floats (not integers)
    ([1, 2, "3", 5], 26),      # Mixed types (string ignored): 1^2 + 5^2 = 26
    ([7, -7, 11, -11], 170),   # Positive and negative odds: 49 + 121 = 170
    ([None, True, False], 1),  # Booleans are ints in Python (True=1, False=0), 1^2 = 1
    ([101], 10201),            # Large odd number
])
def test_double_the_difference(lst, expected):
    assert double_the_difference(lst) == expected

def test_double_the_difference_non_list_input():
    """Test behavior with non-list iterable if applicable, 
    though the prompt specifies 'list'."""
    assert double_the_difference((1, 3)) == 10