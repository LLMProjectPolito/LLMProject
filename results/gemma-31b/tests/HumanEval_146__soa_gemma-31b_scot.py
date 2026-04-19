
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
    ([15, -73, 14, -15], 1),  # Only 15: >10, 1 is odd, 5 is odd
    ([33, -2, -3, 45, 21, 109], 2),  # 33 and 109: >10, first/last odd
    
    # Edge cases: Empty and small lists
    ([], 0),
    ([10], 0),  # Not greater than 10
    ([11], 1),  # >10, 1 is odd, 1 is odd
    ([9], 0),   # Not greater than 10
    
    # Digit parity checks
    ([12], 0),  # >10, 1 odd, 2 even
    ([21], 0),  # >10, 2 even, 1 odd
    ([22], 0),  # >10, 2 even, 2 even
    ([13], 1),  # >10, 1 odd, 3 odd
    
    # Multi-digit numbers
    ([101], 1), # >10, 1 odd, 1 odd
    ([102], 0), # >10, 1 odd, 2 even
    ([201], 0), # >10, 2 even, 1 odd
    ([202], 0), # >10, 2 even, 2 even
    ([13579], 1), # >10, 1 odd, 9 odd
    ([30007], 1), # >10, 3 odd, 7 odd
    
    # Negative numbers (should all be ignored as they are not > 10)
    ([-11], 0),
    ([-15], 0),
    ([-33], 0),
    ([-109], 0),
    
    # Mixed types of failures
    ([10, 11, 12, 21, 22, 31, 32, 41, 51], 3), # 11, 31, 51
    ([100, 200, 300, 400, 500], 0), # All end in 0 (even)
    ([1001, 2002, 3003, 4004, 5005], 3), # 1001, 3003, 5005
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected