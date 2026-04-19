
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
    ([1, 3, 2, 0], 10),    # 1^2 + 3^2 = 1 + 9 = 10
    ([-1, -2, 0], 0),      # All negative or even
    ([9, -2], 81),         # 9^2 = 81
    ([0], 0),              # 0 is even
    ([], 0),               # Empty list
    
    # Edge cases: All odd positive
    ([1, 3, 5], 35),       # 1 + 9 + 25 = 35
    
    # Edge cases: All even positive
    ([2, 4, 6, 8], 0),
    
    # Edge cases: All negative odd
    ([-1, -3, -5], 0),
    
    # Edge cases: Mixed positive/negative odd
    ([1, -1, 3, -3, 5, -5], 35), # 1^2 + 3^2 + 5^2 = 35
    
    # Edge cases: Non-integer types (should be ignored)
    ([1, 3, 2.5, 5.5], 10),    # Floats ignored: 1^2 + 3^2 = 10
    ([1, "3", 5], 26),         # Strings ignored: 1^2 + 5^2 = 26
    ([1, None, 3], 10),        # None ignored: 1^2 + 3^2 = 10
    ([1, [3], 5], 26),         # Lists ignored: 1^2 + 5^2 = 26
    ([1.0, 3.0, 5.0], 0),      # Floats (even if whole) are not 'int' type
    
    # Edge cases: Booleans (In Python, bool is a subclass of int)
    # If the function uses isinstance(x, int), True is 1 (odd) and False is 0 (even).
    # If the function uses type(x) is int, booleans are ignored.
    # Most robust implementations for this prompt should ignore booleans or handle them as ints.
    # We test for standard integer behavior.
    ([True, 3], 10),           # True is 1: 1^2 + 3^2 = 10
    ([False, 3], 9),           # False is 0: 3^2 = 9
    
    # Large numbers
    ([101], 10201),            # 101^2 = 10201
])
def test_double_the_difference(input_list, expected):
    """
    Tests the double_the_difference function against various scenarios including
    provided examples, empty lists, negative numbers, non-integers, and mixed types.
    """
    assert double_the_difference(input_list) == expected

def test_double_the_difference_type_stability():
    """
    Ensure the function returns an integer even for empty or invalid inputs.
    """
    assert isinstance(double_the_difference([]), int)
    assert isinstance(double_the_difference(["a", "b"]), int)