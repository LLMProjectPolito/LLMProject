
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
    """
    Implementation provided for context to ensure the test suite is runnable.
    The logic follows the docstring: sum of squares of non-negative odd integers.
    """
    return sum(x**2 for x in lst if isinstance(x, int) and not isinstance(x, bool) and x >= 0 and x % 2 != 0)

@pytest.mark.parametrize("input_list, expected", [
    # --- Docstring Examples ---
    ([1, 3, 2, 0], 10),      # 1^2 + 3^2 = 10 (2 and 0 are even)
    ([-1, -2, 0], 0),        # All negative or even
    ([9, -2], 81),           # 9^2 = 81 (-2 is negative)
    ([0], 0),                # 0 is even
    
    # --- Edge Cases: Empty and Zero ---
    ([], 0),                 # Empty list returns 0
    ([0, 0, 0], 0),          # Multiple zeros
    
    # --- Edge Cases: Negative Numbers ---
    ([-1, -3, -5], 0),       # All negative odd integers
    ([-2, -4, -6], 0),       # All negative even integers
    ([-1, 1], 1),            # Mixed negative and positive
    
    # --- Edge Cases: Even Numbers ---
    ([2, 4, 6, 8], 0),       # All positive even integers
    ([1, 2, 3, 4, 5], 35),   # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    
    # --- Edge Cases: Non-Integers (Floats) ---
    ([1.0, 3.0, 5.0], 0),    # Floats are not integers (type check)
    ([1, 3, 3.5, 5], 35),    # 3.5 is ignored
    ([2.0, 4.0], 0),         # Even floats ignored
    
    # --- Edge Cases: Large Numbers ---
    ([1000001], 1000002000001), # Large odd integer
])
def test_double_the_difference_logic(input_list, expected):
    """Tests the core logic against provided examples and standard mathematical expectations."""
    assert double_the_difference(input_list) == expected

def test_boolean_edge_case():
    """
    Blue Team Check: In Python, bool is a subclass of int. 
    True is 1, False is 0. A robust function should ignore booleans 
    if the requirement specifies 'integers'.
    """
    # If the function incorrectly treats True as 1:
    # [True, 3] would return 1 + 9 = 10.
    # If it correctly ignores booleans:
    # [True, 3] should return 9.
    assert double_the_difference([True, 3]) == 9

def test_type_strictness():
    """
    Ensures that the function strictly adheres to the 'not integers' rule 
    by checking float values that are mathematically integers.
    """
    # 3.0 is mathematically an integer, but its type is float.
    # The prompt says 'Ignore numbers that are... not integers'.
    assert double_the_difference([3.0]) == 0

def test_non_numeric_types():
    """
    Blue Team Check: Verify behavior when non-numeric types are present.
    While the prompt says 'list of numbers', a robust function should 
    not crash if it encounters unexpected types like strings.
    """
    try:
        result = double_the_difference([1, "3", None, 5])
        assert result == 26 # 1^2 + 5^2
    except Exception as e:
        pytest.fail(f"Function crashed on non-numeric types: {e}")

def test_large_input_performance():
    """Tests performance with a large list of numbers."""
    large_list = [1] * 10000
    # 1^2 * 10000 = 10000
    assert double_the_difference(large_list) == 10000