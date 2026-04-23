
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
    
    # Edge cases: Empty and Even
    ([], 0),
    ([2, 4, 6, 8], 0),
    ([0, 2, 4, 10], 0),
    
    # Edge cases: Negative numbers
    ([-1, -3, -5, -7], 0),
    
    # Edge cases: Non-integers (floats)
    ([1.0, 3.0, 5.0], 0),
    ([1.1, 3.3, 5.5], 0),
    ([1.5], 0),
    
    # Mixed valid and invalid (floats, negatives, evens)
    ([1, 2, 3.5, -3, 5], 26),          # 1^2 + 5^2
    ([1, 1.0, 3, 3.0, 5], 35),         # 1^2 + 3^2 + 5^2
    ([1, 2.0, 4, -3, 5, 7.7], 26),     # 1^2 + 5^2
    ([3.0, 5], 25),                    # 5^2
    ([1, 2, 3.0, 4, 5.5], 1),          # 1^2
    
    # Mixed non-numeric types
    ([1, "a", None, 3], 10),           # 1^2 + 3^2
    
    # Large numbers and duplicates
    ([11, 13], 121 + 169),
    ([3, 3, 3], 27),
    
    # Single element cases
    ([7], 49),
    ([8], 0),
    ([-1], 0),
])
def test_double_the_difference(input_list, expected):
    """
    Tests the double_the_difference function with a variety of inputs 
    including docstring examples, edge cases, and mixed types.
    """
    assert double_the_difference(input_list) == expected