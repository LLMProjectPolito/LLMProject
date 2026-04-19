
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
    '''
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
    
    # Edge cases: Positive odd numbers
    ([1], 1),              # Single odd
    ([1, 1, 1], 3),        # Multiple same odds
    ([1, 3, 5], 35),       # 1 + 9 + 25 = 35
    
    # Edge cases: Even numbers and Zero
    ([2, 4, 6, 8], 0),     # All positive evens
    ([0, 0, 0], 0),        # All zeros
    
    # Edge cases: Negative numbers
    ([-1, -3, -5], 0),     # Negative odds should be ignored
    ([-2, -4, -6], 0),     # Negative evens should be ignored
    ([-1, 1], 1),          # Mixed negative/positive odd
    
    # Edge cases: Non-integers
    ([1.5, 3.5], 0),       # Floats
    ([3.0, 5.0], 0),       # Floats that are mathematically integers (should be ignored per "not integers")
    (["1", "3"], 0),       # Strings
    ([None, True, False], 0), # None and Booleans (True is technically 1 in Python, but not a "number" in this context)
    
    # Mixed types
    ([1, 2.2, 3, -5, "text", 5], 35), # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    ([7, None, -7, 2, 11], 170),      # 7^2 + 11^2 = 49 + 121 = 170
    
    # Large numbers
    ([101], 10201),        # 101^2
    ([1001, 1], 1002002),  # 1001^2 + 1^2 = 1002001 + 1
])
def test_double_the_difference(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_double_the_difference_mutation():
    """Ensure the function does not mutate the original list."""
    original = [1, 3, 5]
    copy_original = original[:]
    double_the_difference(original)
    assert original == copy_original