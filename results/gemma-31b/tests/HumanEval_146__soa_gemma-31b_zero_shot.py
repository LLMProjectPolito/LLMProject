
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
    ([15, -73, 14, -15], 1),           # Example 1: Only 15 fits
    ([33, -2, -3, 45, 21, 109], 2),    # Example 2: 33 and 109 fit
    ([], 0),                           # Empty list
    ([11], 1),                         # Minimum valid number (11 > 10, 1 odd, 1 odd)
    ([10], 0),                         # Boundary: exactly 10 (must be > 10)
    ([9], 0),                          # Single digit (not > 10)
    ([12], 0),                         # Last digit even
    ([21], 0),                         # First digit even
    ([22], 0),                         # Both digits even
    ([135], 1),                        # Three digits, first and last odd
    ([136], 0),                        # Three digits, last even
    ([235], 0),                        # Three digits, first even
    ([101], 1),                        # Three digits, first and last odd, middle even
    ([100], 0),                        # Three digits, last even
    ([-11], 0),                        # Negative number (not > 10)
    ([-135], 0),                       # Negative number (not > 10)
    ([11111], 1),                      # Large number, first and last odd
    ([21112], 0),                      # Large number, first and last even
    ([1000000001], 1),                 # Very large number, first and last odd
    ([13, 15, 17, 19], 4),             # All fit
    ([12, 14, 16, 18], 0),             # None fit (last digit even)
    ([21, 23, 25, 27], 0),             # None fit (first digit even)
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected