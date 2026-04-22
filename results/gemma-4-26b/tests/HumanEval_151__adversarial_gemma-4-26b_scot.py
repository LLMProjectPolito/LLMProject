
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

# The function is assumed to be defined in the environment.
# We are writing the test suite to detect bugs in it.

@pytest.mark.parametrize("input_list, expected", [
    # Docstring Examples
    ([1, 3, 2, 0], 10),      # 1^2 + 3^2 = 1 + 9 = 10
    ([-1, -2, 0], 0),       # All ignored
    ([9, -2], 81),          # 9^2 = 81
    ([0], 0),               # 0 is even
    
    # Edge Cases: Empty and Zero
    ([], 0),                # Empty list
    ([0, 0, 0], 0),         # Only zeros
    
    # Edge Cases: Negatives
    ([-1, -3, -5], 0),      # Negative odds ignored
    ([-2, -4, -6], 0),      # Negative evens ignored
    
    # Edge Cases: Even Numbers
    ([2, 4, 6, 8], 0),      # Positive evens ignored
    
    # Edge Cases: Non-integers (Floats)
    ([1.0, 3.0, 5.0], 0),   # Floats are not integers
    ([1, 3.5, 5], 26),      # 1^2 + 5^2 = 26 (3.5 ignored)
    
    # Mixed Scenarios
    ([1, 2, 3, 4, 5, 6], 35), # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    ([7, -7, 7.0, 9], 130),   # 7^2 + 9^2 = 49 + 81 = 130
    ([11, 13, 15], 455),      # 121 + 169 + 225 = 515? No: 121 + 169 + 225 = 515. 
                              # Let's re-calc: 11^2(121) + 13^2(169) + 15^2(225) = 515.
])
def test_double_the_difference_logic(input_list, expected):
    """
    Tests the core logic including filtering for odd, non-negative, and integer types.
    """
    # Note: I corrected the manual math in the parametrization for 11, 13, 15
    # 121 + 169 + 225 = 515
    if input_list == [11, 13, 15]:
        expected = 515
        
    from __main__ import double_the_difference
    assert double_the_difference(input_list) == expected

def test_double_the_difference_large_values():
    """
    Test with large odd integers to ensure no overflow issues (Python handles this, 
    but good for robustness).
    """
    from __main__ import double_the_difference
    large_odd = 1000001
    assert double_the_difference([large_odd]) == large_odd**2

def test_double_the_difference_type_safety():
    """
    Test how the function handles non-numeric types if they appear in the list.
    The docstring says 'Given a list of numbers', but a robust function 
    should ideally not crash if a non-number is passed, or at least we 
    should define the behavior.
    """
    from __main__ import double_the_difference
    # If the function is strictly for numbers, it might raise TypeError.
    # However, if it's robust, it should ignore them. 
    # We test for the assumption that it handles/ignores non-integers.
    try:
        result = double_the_difference([1, "3", None, 3])
        # If it ignores non-integers, result should be 1^2 + 3^2 = 10
        assert result == 10
    except TypeError:
        # If the function is expected to crash on bad types, this is also a valid behavior.
        # For this suite, we assume 'Ignore numbers that are... not integers' 
        # implies a type-check that handles non-int types gracefully.
        pass

def test_double_the_difference_all_invalid():
    """
    Test a list where no elements meet the criteria.
    """
    from __main__ import double_the_difference
    assert double_the_difference([-1, 2.2, 4, -5, 0]) == 0