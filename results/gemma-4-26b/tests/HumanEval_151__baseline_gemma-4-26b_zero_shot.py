
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
    # Docstring examples
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    
    # Edge case: Empty list
    ([], 0),
    
    # Edge case: All even numbers (should return 0)
    ([2, 4, 6, 8, 10], 0),
    
    # Edge case: All negative numbers (should return 0)
    ([-1, -3, -5, -7], 0),
    
    # Edge case: All non-integers (floats) (should return 0)
    ([1.1, 3.3, 5.5], 0),
    ([1.0, 3.0, 5.0], 0),
    
    # Mixed valid and invalid numbers
    ([1, 2, 3, 4, 5], 35),           # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    ([1, 3, 5.5, 7], 59),            # 1^2 + 3^2 + 7^2 = 1 + 9 + 49 = 59
    ([7, -1, 2, 3.3, 9], 130),       # 7^2 + 9^2 = 49 + 81 = 130
    ([1, 1, 1], 3),                  # 1^2 + 1^2 + 1^2 = 3
    
    # Single element cases
    ([1], 1),                        # Single odd integer
    ([2], 0),                        # Single even integer
    ([-1], 0),                       # Single negative odd integer
    ([1.5], 0),                      # Single float
    ([101], 10201),                  # Large odd integer
])
def test_double_the_difference(input_list, expected):
    """
    Tests the double_the_difference function with various inputs including
    docstring examples, edge cases, and mixed types.
    """
    assert double_the_difference(input_list) == expected