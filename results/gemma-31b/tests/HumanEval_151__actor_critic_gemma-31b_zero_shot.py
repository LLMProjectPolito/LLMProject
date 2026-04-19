
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
    # Removed 'if not lst: return 0' to allow TypeError when lst is None,
    # while still returning 0 for an empty list via the total initialization.
    total = 0
    for x in lst:
        # Check if it is an integer and not a boolean (since bool is a subclass of int)
        if type(x) is int and x >= 0 and x % 2 != 0:
            total += x**2
    return total

@pytest.mark.parametrize("input_list, expected", [
    # Docstring examples
    ([1, 3, 2, 0], 10),    # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),      # All negative or even
    ([9, -2], 81),         # 9^2 = 81
    ([0], 0),              # Even
    ([], 0),               # Empty list
    
    # Edge cases: Types
    ([1, 3, 2.5, "3", None], 10), # Ignore float, string, None
    ([1, True, 3], 10),           # Booleans are ints in Python, but should be ignored
    
    # Edge cases: Values
    ([1, 3, 5], 35),       # All odd: 1 + 9 + 25 = 35
    ([2, 4, 6], 0),        # All even
    ([-1, -3, -5], 0),     # All negative odd
    ([0, 0, 0], 0),        # All zeros
    ([101], 10201),        # Single large odd number
    
    # Mixed complex case
    ([1, -1, 2, -2, 3, -3, 4.4, 'text', 5], 35), # 1^2 + 3^2 + 5^2 = 35
])
def test_double_the_difference(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_non_list_input():
    """Test that non-iterable input (like None) raises a TypeError."""
    with pytest.raises(TypeError):
        double_the_difference(None)