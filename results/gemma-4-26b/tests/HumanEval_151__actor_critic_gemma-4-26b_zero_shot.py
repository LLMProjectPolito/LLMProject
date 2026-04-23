
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

def sum_squares_of_odd_ints(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative, 
    not integers, or booleans.
    
    sum_squares_of_odd_ints([1, 3, 2, 0]) == 1 + 9 = 10
    sum_squares_of_odd_ints([-1, -2, 0]) == 0
    sum_squares_of_odd_ints([9, -2]) == 81
    sum_squares_of_odd_ints([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    total = 0
    for x in lst:
        # Using type(x) is int instead of isinstance(x, int) to ensure 
        # booleans (which are a subclass of int) are explicitly ignored.
        if type(x) is int and x >= 0 and x % 2 != 0:
            total += x**2
    return total

@pytest.mark.parametrize("input_list, expected", [
    # Docstring examples
    ([1, 3, 2, 0], 10),      # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),       # All negative or even
    ([9, -2], 81),          # 9^2 = 81
    ([0], 0),               # 0 is even
    
    # Edge Case: Empty list
    ([], 0),
    
    # Edge Case: All negative numbers
    ([-1, -3, -5, -7], 0),
    
    # Edge Case: All even numbers
    ([2, 4, 6, 8, 0], 0),
    
    # Edge Case: Non-integer numbers (floats)
    ([1.0, 3.0, 5.5], 0),   # 1.0 and 3.0 are floats, not ints
    ([1, 3.0, 5], 26),      # 1^2 + 5^2 = 26 (3.0 is ignored)
    
    # Edge Case: Mixed valid and invalid types
    ([1, 2, 3, 4, 5, -1, 7.5, 9], 116), # 1^2 + 3^2 + 5^2 + 9^2 = 1 + 9 + 25 + 81 = 116
    
    # Edge Case: Large numbers
    ([11, 13], 290),        # 11^2 + 13^2 = 121 + 169 = 290
    
    # Edge Case: Single elements
    ([7], 49),              # Single odd
    ([8], 0),               # Single even
    ([-7], 0),              # Single negative odd
    ([7.0], 0),             # Single float odd
    
    # Edge Case: Booleans (Clarifying that True/False are not treated as 1/0)
    ([True, 3], 9),         # True is ignored, 3^2 = 9
    ([False, 1], 1),        # False is ignored, 1^2 = 1
    
    # Edge Case: Non-numeric types
    ([1, "string", None, [2]], 1), # Only 1 is a valid odd integer
    
    # Edge Case: Mixed numeric types (Merged from redundant test)
    ([3, 3.0], 9),          # 3^2 = 9 (3.0 is ignored)
])
def test_sum_squares_of_odd_ints(input_list, expected):
    """Tests the sum_squares_of_odd_ints function with various scenarios."""
    assert sum_squares_of_odd_ints(input_list) == expected