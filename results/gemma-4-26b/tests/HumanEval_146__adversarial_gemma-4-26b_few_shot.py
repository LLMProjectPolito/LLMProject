
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

# The function signature for reference
# def specialFilter(nums: list[int]) -> int: ...

@pytest.mark.parametrize("input_list, expected", [
    # --- Provided Examples (Sanity Checks) ---
    ([15, -73, 14, -15], 1),        # Only 15: >10, 1 is odd, 5 is odd
    ([33, -2, -3, 45, 21, 109], 2), # 33 and 109: >10, first/last odd
    
    # --- Boundary Condition: The "Greater than 10" Rule ---
    ([10], 0),                      # Exactly 10 (must be > 10)
    ([11], 1),                      # First valid number (11 > 10, 1 and 1 are odd)
    ([9], 0),                       # Single digit < 10
    
    # --- Digit Parity Logic (First and Last) ---
    ([13, 31, 33, 55, 77, 91, 99], 7), # All match: >10 and odd/odd
    ([21, 12, 22, 43, 34, 81, 18], 0), # All fail: either first or last is even
    ([101, 121, 141, 161, 181], 5),    # Multi-digit: 1 is odd, middle doesn't matter
    ([303, 505, 707, 909], 4),         # Multi-digit: middle zeros
    ([1111111], 1),                    # Long odd-digit number
    
    # --- Negative Numbers (The "Greater than 10" Rule) ---
    # Even if digits are odd, they must be > 10
    ([-11, -13, -15, -31, -33], 0), 
    ([-1, -3, -5, -7, -9], 0),
    
    # --- Empty and Small Inputs ---
    ([], 0),                        # Empty list
    ([5], 0),                       # Single element < 10
    ([13], 1),                      # Single element > 10 and valid
    
    # --- Large Numbers ---
    ([1000000000000000000000000000001], 1), # Very large number (checks for overflow/string conversion)
    ([999999999999999999999999999999], 1),  # Large number with even last digit (if it were 99...98)
])
def test_special_filter_logic(input_list, expected):
    """Tests various logical combinations of the filter requirements."""
    from your_module import specialFilter # Replace with actual module name
    assert specialFilter(input_list) == expected

def test_special_filter_non_integer_elements():
    """
    QA Note: Testing how the function handles floats. 
    The prompt says 'array of numbers', which could imply floats.
    If the implementation uses string conversion, floats might behave unexpectedly.
    """
    from your_module import specialFilter
    # 15.1 is > 10. First digit 1 (odd), last digit 1 (odd).
    # This test determines if the requirement applies to the mathematical value or integer representation.
    # Assuming standard integer-based logic for this challenge:
    try:
        # If the function is strictly for ints, this might raise a TypeError.
        # If it's robust, it should handle or ignore.
        result = specialFilter([15.1])
        assert isinstance(result, int)
    except TypeError:
        pass # This is also an acceptable behavior if the spec implies integers only

def test_special_filter_input_types():
    """Tests robustness against invalid input types."""
    from your_module import specialFilter
    with pytest.raises(TypeError):
        specialFilter(None)
    with pytest.raises(TypeError):
        specialFilter("not a list")