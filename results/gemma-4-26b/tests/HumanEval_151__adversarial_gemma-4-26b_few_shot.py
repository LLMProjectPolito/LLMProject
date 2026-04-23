
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

# The function signature for context
# def double_the_difference(lst): ...

@pytest.mark.parametrize("input_list, expected", [
    # --- Docstring Examples ---
    ([1, 3, 2, 0], 10),      # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),        # All negative or even
    ([9, -2], 81),           # 9^2 = 81
    ([0], 0),                # 0 is even
    ([], 0),                 # Empty list requirement

    # --- Boundary & Mathematical Cases ---
    ([1], 1),                # Single odd element
    ([2], 0),                # Single even element
    ([1, 1, 1], 3),          # Duplicate odd elements
    ([1000001], 1000002000001), # Large odd integer (testing large number handling)
    
    # --- Negative/Even Filtering ---
    ([-1, -3, -5], 0),       # Negative odds should be ignored
    ([2, 4, 6, 8], 0),       # Positive evens should be ignored
    ([-2, -4, 0], 0),        # Negative evens and zero should be ignored
])
def test_double_the_difference_logic(input_list, expected):
    """Tests the core mathematical logic and requirement constraints."""
    from your_module import double_the_difference # Replace with actual module name
    assert double_the_difference(input_list) == expected

@pytest.mark.parametrize("input_list, expected", [
    # --- Type Safety: "Ignore numbers that are... not integers" ---
    ([1, 2.0, 3.0, 3], 10),          # 2.0 and 3.0 are floats, should be ignored
    ([1, "3", None, [5]], 1),        # Strings, None, and Lists should be ignored
    ([1, 3.5, 5], 26),               # 3.5 is a float, should be ignored (1^2 + 5^2)
    ([1, True, 3], 1),               # CRITICAL: In Python, isinstance(True, int) is True. 
                                     # However, True % 2 is 1. 
                                     # A strict implementation should check type(x) is int.
])
def test_double_the_difference_types(input_list, expected):
    """Tests the requirement to ignore non-integer types."""
    from your_module import double_the_difference
    assert double_the_difference(input_list) == expected

def test_double_the_difference_extreme_mixed_types():
    """Tests a highly chaotic list to ensure no crashes occur."""
    from your_module import double_the_difference
    chaotic_list = [1, "apple", -3, 5.5, None, 7, {"key": "val"}, 9, 0, -10]
    # Expected: 1^2 (1) + 7^2 (49) + 9^2 (81) = 131
    assert double_the_difference(chaotic_list) == 131

def test_double_the_difference_large_input():
    """Tests performance/stability with a larger list."""
    from your_module import double_the_difference
    large_list = [1] * 1000  # 1000 instances of 1
    assert double_the_difference(large_list) == 1000