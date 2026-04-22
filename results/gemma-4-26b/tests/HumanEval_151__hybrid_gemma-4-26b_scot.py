
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

# Assuming the function is in solution.py
from solution import double_the_difference

@pytest.mark.parametrize("input_list, expected_output", [
    # --- Category 1: Empty and Zero-sum cases ---
    ([], 0),                         # Empty list
    ([0], 0),                        # Zero is even
    ([2, 4, 6, 8], 0),               # All even
    ([-1, -3, -5], 0),               # All negative odds
    ([1.0, 3.0, 5.0], 0),            # All floats (even if mathematically odd)
    ([0, 2, -2], 0),                 # Mix of even and negative
    
    # --- Category 2: Valid Inputs (Positive Odd Integers) ---
    ([7], 49),                       # Single valid element (7^2)
    ([1, 3, 5], 35),                 # Multiple valid (1+9+25)
    ([11, 13], 290),                 # Larger integers (121+169)
    ([99], 9801),                    # Single large integer
    
    # --- Category 3: Mixed Complex Scenarios (The Core Logic) ---
    # 1 (valid), 3 (valid), 2 (even), 0 (even), -1 (neg), 5.5 (float), -3 (neg)
    ([1, 3, 2, 0, -1, 5.5, -3], 10), 
    
    # 1 (valid), -1 (neg), 2 (even), 3.0 (float), 5 (valid), 0 (even), -3 (neg), 7.5 (float)
    # Calculation: 1^2 + 5^2 = 1 + 25 = 26
    ([1, -1, 2, 3.0, 5, 0, -3, 7.5], 26),
    
    # 3.0 (float), 5.0 (float), 7 (valid)
    ([3.0, 5.0, 7], 49),
    
    # 1 (valid), 2 (even), 3 (valid), 4 (even), 5 (valid), 6 (even)
    ([1, 2, 3, 4, 5, 6], 35),
])
def test_double_the_difference_parametrized(input_list, expected_output):
    """
    Comprehensive parametrized test covering empty lists, filtering logic 
    (negatives, evens, floats), and various combinations of valid/invalid inputs.
    """
    assert double_the_difference(input_list) == expected_output

def test_type_strictness():
    """
    Explicitly verifies that the function distinguishes between 
    integers and floats, even if the float has no fractional part.
    """
    # 3.0 is mathematically an odd integer, but its type is float.
    assert double_the_difference([3.0]) == 0
    assert double_the_difference([1, 3.0, 5]) == 26  # Only 1 and 5 are valid

def test_sign_and_parity_filtering():
    """
    Explicitly verifies that only positive odd integers are processed.
    """
    # -1 and -3 are odd but negative
    assert double_the_difference([-1, -3, 1, 3]) == 10
    # 0 is an integer but even
    assert double_the_difference([0, 1, 3]) == 10

def test_large_scale_summation():
    """
    Verifies the function handles larger lists and maintains correct 
    summation accumulation.
    """
    # Valid odd integers: 1, 3, 5, 7, 9, 11
    # Squares: 1, 9, 25, 49, 81, 121
    # Sum: 286
    # Mixed with invalid: even, negative, and floats
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, -3, 3.3, 5.5]
    assert double_the_difference(input_list) == 286