
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
    # Provided examples
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    
    # Edge cases: Empty list
    ([], 0),
    
    # Edge cases: No odd numbers
    ([2, 4, 6, 8], 0),
    ([0, 2, 4], 0),
    
    # Edge cases: All negative numbers
    ([-1, -3, -5], 0),
    
    # Edge cases: Non-integers (floats)
    ([1.0, 3.0, 5.5], 0),
    
    # Mixed valid and invalid
    ([1, 3, 2, -1, 3.5, 5], 35),  # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    ([11, 13, 15], 515),         # 121 + 169 + 225 = 515
    ([0, -3, 1, 5, -2, 7], 75),  # 1^2 + 5^2 + 7^2 = 1 + 25 + 49 = 75
    
    # Large numbers
    ([101], 10201),
    
    # Multiple same odd numbers
    ([3, 3, 3], 27),
])
def test_double_the_difference(input_list, expected):
    """
    Tests the double_the_difference function with various inputs including
    provided examples, empty lists, negative numbers, floats, and mixed types.
    """
    assert double_the_difference(input_list) == expected

def test_double_the_difference_type_strictness():
    """
    Explicitly test that floats that are mathematically integers (like 3.0) 
    are ignored if the requirement 'not integers' refers to the data type.
    """
    # 1^2 + 5^2 = 26
    assert double_the_difference([1, 3.0, 5]) == 26

def test_double_the_difference_boolean_exclusion():
    """
    Explicitly test that booleans are ignored, as they are often 
    treated as non-integers in strict type-checking scenarios.
    """
    # 1^2 + 3^2 = 10
    assert double_the_difference([1, True, 3]) == 10