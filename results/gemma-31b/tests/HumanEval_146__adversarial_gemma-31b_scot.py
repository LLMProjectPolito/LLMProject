
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

# The function specialFilter is assumed to be defined in the environment.
# We are testing it as a Blue Team QA engineer.

@pytest.mark.parametrize("nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),        # Only 15: >10, 1 is odd, 5 is odd
    ([33, -2, -3, 45, 21, 109], 2), # 33 and 109
    
    # Empty and No-match cases
    ([], 0),                        # Empty list
    ([2, 4, 6, 8], 0),              # All <= 10
    ([22, 44, 66, 88], 0),          # All > 10 but digits are even
    
    # Boundary cases for > 10
    ([10], 0),                      # Exactly 10 (should be excluded)
    ([11], 1),                      # Just above 10, both odd
    ([9], 0),                       # Just below 10
    
    # Parity combinations
    ([21], 0),                      # First even, last odd
    ([12], 0),                      # First odd, last even
    ([22], 0),                      # Both even
    ([11], 1),                      # Both odd
    
    # Negative numbers (should be excluded by > 10)
    ([-11], 0),                     # Both digits odd, but < 10
    ([-15], 0),                     # Both digits odd, but < 10
    ([-101], 0),                    # Both digits odd, but < 10
    
    # Large numbers
    ([10001], 1),                   # First 1, Last 1 (Odd)
    ([3000000007], 1),              # First 3, Last 7 (Odd)
    ([2000000001], 0),              # First 2 (Even)
    ([1000000002], 0),              # Last 2 (Even)
    
    # Mixed list
    ([11, 12, 13, 21, 23, 31, 32, 33], 4), # 11, 13, 31, 33
])
def test_special_filter_scenarios(nums, expected):
    """Test various scenarios including boundaries, parity, and negative numbers."""
    assert specialFilter(nums) == expected

def test_special_filter_type_stability():
    """Test that the function handles lists containing different numeric types."""
    # If the function uses string conversion for digits, floats might behave differently.
    # This test checks if floats that satisfy the logic are counted or if they cause errors.
    # 11.0 > 10, first digit '1', last digit '0' (if treated as string) or '1' (if cast to int).
    # Given the prompt "digits", it usually implies integer logic.
    try:
        # 15.0: > 10, first digit 1, last digit 5 (if treated as int)
        # We test to ensure it doesn't crash.
        specialFilter([15.0, 11.0])
    except Exception as e:
        pytest.fail(f"specialFilter raised an unexpected exception with floats: {e}")

def test_special_filter_large_input():
    """Test performance/stability with a larger list."""
    nums = [11] * 1000  # 1000 elements that all match
    assert specialFilter(nums) == 1000