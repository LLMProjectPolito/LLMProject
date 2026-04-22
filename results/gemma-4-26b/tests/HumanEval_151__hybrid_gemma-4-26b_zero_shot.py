
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
    # Using type(x) is int to strictly exclude booleans, as True/False are instances of int
    return sum(x**2 for x in lst if type(x) is int and x >= 0 and x % 2 != 0)

@pytest.mark.parametrize("input_list, expected", [
    # --- Docstring Examples ---
    ([1, 3, 2, 0], 10),        # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),          # All negative or even
    ([9, -2], 81),             # 9^2 = 81
    ([0], 0),                  # 0 is even
    
    # --- Boundary and Empty Cases ---
    ([], 0),                   # Empty list
    ([1], 1),                  # Single odd integer
    ([2], 0),                  # Single even integer
    
    # --- Negative Number Handling ---
    ([-1, -3, -5], 0),         # All negative odd integers
    ([-2, -4, -6], 0),         # All negative even integers
    ([1, -3, 5], 26),          # Mixed positive and negative (1^2 + 5^2)
    ([-1, -3, 1, 3], 10),      # Negative odds ignored, positive odds counted
    
    # --- Non-Integer Handling (Floats) ---
    ([1.0, 3.0, 5.0], 0),      # Floats are not integers
    ([1, 3.5, 5], 26),         # 1^2 + 5^2 (3.5 is ignored)
    ([1, 2, 3.0, 4, 5.0], 1),  # Only 1 is a valid odd integer
    ([-1.5, -2, 0.5, 4.4, -7], 0), # Only floats and negatives
    
    # --- Non-Numeric Type Handling ---
    ([1, "3", None, 5], 26),   # String and None are ignored
    ([1, [3], {"val": 5}, 7], 50), # List and Dict are ignored (1^2 + 7^2)
    
    # --- Boolean Handling ---
    # Booleans are instances of int, but type(True) is bool. 
    # Strict requirement "not integers" implies excluding bools.
    ([True, 1, 3], 10),        # True is ignored
    
    # --- Mixed and Large Parity ---
    ([101, 102, 103], 20810),  # 101^2 + 103^2
    ([2, 4, 6, 8, 10], 0),     # All even
    ([1, 3, 5, 7, 9], 165),    # All positive odd
    ([11, 13], 290),           # 121 + 169
    ([0, 1, -1, 2, 3.0, 5], 26), # Mixed: 1^2 + 5^2
])
def test_double_the_difference(input_list, expected):
    """
    Tests the double_the_difference function with a comprehensive set of 
    inputs including docstring examples, edge cases, and type variations.
    """
    assert double_the_difference(input_list) == expected

def test_input_immutability():
    """
    Ensure the function does not mutate the original input list.
    """
    original = [1, 3, 5]
    input_copy = list(original)
    double_the_difference(input_copy)
    assert input_copy == original

def test_large_input_list():
    """
    Test with a large list of numbers to ensure performance and correctness.
    """
    lst = [i for i in range(100)]
    # Sum of squares of odd numbers from 1 to 99
    expected = sum(x**2 for x in range(1, 100, 2))
    assert double_the_difference(lst) == expected