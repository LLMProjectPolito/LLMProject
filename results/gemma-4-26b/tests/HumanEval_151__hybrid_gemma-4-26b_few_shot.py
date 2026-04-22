
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

# The function being tested (for context)
# def double_the_difference(lst):
#     return sum(x**2 for x in lst if isinstance(x, int) and not isinstance(x, bool) and x >= 0 and x % 2 != 0)

def test_provided_examples():
    """Tests the specific examples provided in the original problem description."""
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_empty_list():
    """Tests that an empty list returns 0."""
    assert double_the_difference([]) == 0

@pytest.mark.parametrize("input_list, expected", [
    # Numeric Logic: Positive, Negative, Even, Odd
    ([2, 4, 6, 8], 0),          # All even
    ([-1, -3, -5], 0),          # All negative odd
    ([-2, -4, -6], 0),          # All negative even
    ([1, 5, 7], 1 + 25 + 49),   # All positive odd
    ([10, 20, 30], 0),          # All positive even
    ([-7, 3], 9),               # Mixed negative and positive odd
    ([101, 103], 101**2 + 103**2), # Large numbers
], ids=["all_even", "all_neg_odd", "all_neg_even", "all_pos_odd", "all_pos_even", "mixed_neg_pos_odd", "large_numbers"])
def test_numeric_logic(input_list, expected):
    """Tests various combinations of positive, negative, even, and odd integers."""
    assert double_the_difference(input_list) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([1, 3.0, 5], 26),          # 3.0 is a float, should be ignored
    ([1, 2.5, 3], 10),          # 2.5 is ignored
    ([1.1, 3.3, 5.5], 0),       # All floats
    ([1, '3', [5], None], 1),   # Mixed types: string, list, and None ignored
    ([True, 3, 5], 34),         # Boolean True is ignored (strict type check)
    ([1.0, 3.0], 0),            # Floats that are mathematically integers are still ignored
], ids=["float_interruption", "float_decimal", "all_floats", "non_numeric_types", "boolean_exclusion", "float_integers"])
def test_type_filtering(input_list, expected):
    """Tests that non-integers and non-numeric types are correctly ignored."""
    assert double_the_difference(input_list) == expected

def test_complex_integration():
    """
    A comprehensive 'stress test' combining valid odd integers, 
    even integers, negatives, and various non-integer types.
    """
    # Valid: 3, 7, 11 -> 9 + 49 + 121 = 179
    # Invalid: -3 (neg), 4 (even), 5.5 (float), "9" (str), 0 (even), True (bool)
    input_list = [3, -3, 4, 5.5, "9", 7, 0, 11, True]
    assert double_the_difference(input_list) == 179

@pytest.mark.parametrize("input_val, expected", [
    ([1], 1),           # Single element valid
    ([8], 0),           # Single element invalid (even)
    ([-7], 0),          # Single element invalid (negative)
    ([7.0], 0),         # Single element invalid (float)
    ([-1, 1], 1),       # Mixed negative/positive
    ([1, "1", 1.0], 1), # Mixed types with same value
])
def test_edge_cases(input_val, expected):
    """Tests granular edge cases like single-element lists and value-identity overlaps."""
    assert double_the_difference(input_val) == expected