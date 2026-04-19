
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

@pytest.mark.parametrize("nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),        # Only 15: >10, 1 is odd, 5 is odd
    ([33, -2, -3, 45, 21, 109], 2), # 33 and 109: >10, first/last odd
    
    # Edge cases: Empty and Small lists
    ([], 0),                        # Empty list
    ([10], 0),                      # Exactly 10 (must be > 10)
    ([9], 0),                       # Single digit (must be > 10)
    
    # Condition: Greater than 10
    ([-11], 0),                     # Negative number (not > 10)
    ([-15, -33], 0),                # Negative numbers with odd digits (not > 10)
    
    # Condition: First digit odd
    ([21, 23, 25], 0),              # First digit 2 is even
    ([41, 63, 85], 0),              # First digits are even
    ([11, 31, 51], 3),              # First digits are odd, last digits are odd
    
    # Condition: Last digit odd
    ([12, 14, 16], 0),              # Last digits are even
    ([30, 50, 70], 0),              # Last digit 0 is even
    ([11, 13, 15], 3),              # First digits are odd, last digits are odd
    
    # Mixed conditions
    ([11, 21, 12, 22], 1),          # Only 11 fits
    ([101, 102, 201, 202], 1),      # Only 101 fits
    ([999, 1000, 1001], 2),         # 999 and 1001 fit
    ([13579, 24680], 1),            # 13579 fits
])
def test_special_filter(nums, expected):
    """
    Tests the specialFilter function with various scenarios including:
    - Basic functionality based on examples.
    - Boundary values (10, 0, negative numbers).
    - Parity checks for first and last digits.
    - Empty input.
    """
    assert specialFilter(nums) == expected