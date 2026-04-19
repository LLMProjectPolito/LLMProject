
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
    ([15, -73, 14, -15], 1),        # Example 1: Only 15 fits
    ([33, -2, -3, 45, 21, 109], 2), # Example 2: 33 and 109 fit
    ([], 0),                        # Empty list
    ([11, 13, 15, 17, 19], 5),      # All fit (first=1, last=odd, >10)
    ([21, 23, 25, 27, 29], 0),      # First digit even (2)
    ([10, 12, 14, 16, 18], 0),      # Last digit even
    ([10], 0),                      # Boundary: exactly 10 (must be > 10)
    ([9, 7, 5, 3, 1], 0),           # Single digits (not > 10)
    ([-11, -13, -15], 0),           # Negative numbers (not > 10)
    ([101, 303, 505, 707, 909], 5), # Three digits, first and last odd
    ([100, 200, 300], 0),           # Last digit 0 (even)
    ([1111, 3333, 5555], 3),        # Multi-digit, first and last odd
    ([211, 433, 655], 0),           # First digit even, last odd
    ([112, 334, 556], 0),           # First digit odd, last even
    ([222, 444, 666], 0),           # Both even
    ([10000001], 1),                # Large number, first=1, last=1
    ([10000002], 0),                # Large number, last even
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected