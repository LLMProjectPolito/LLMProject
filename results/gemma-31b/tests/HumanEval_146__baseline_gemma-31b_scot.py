
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
    ([15, -73, 14, -15], 1),        # 15 is valid; -73 is < 10; 14 ends in even; -15 is < 10
    ([33, -2, -3, 45, 21, 109], 2), # 33 and 109 are valid; 45 starts with even; 21 starts with even
    
    # Edge Case: Empty list
    ([], 0),
    
    # Edge Case: Numbers <= 10
    ([1, 3, 5, 7, 9], 0),           # All <= 10
    ([10], 0),                      # Exactly 10
    ([-11, -13, -15], 0),           # Negative numbers with odd digits are still < 10
    
    # Digit Parity Tests (Numbers > 10)
    ([21], 0),                      # First digit (2) is even
    ([12], 0),                      # Last digit (2) is even
    ([22], 0),                      # Both digits even
    ([11], 1),                      # Both digits odd
    ([13], 1),                      # Both digits odd
    ([31], 1),                      # Both digits odd
    ([33], 1),                      # Both digits odd
    
    # Multi-digit numbers
    ([101], 1),                     # First=1, Last=1 (Odd, Odd)
    ([102], 0),                     # First=1, Last=2 (Odd, Even)
    ([201], 0),                     # First=2, Last=1 (Even, Odd)
    ([202], 0),                     # First=2, Last=2 (Even, Even)
    ([3007], 1),                    # First=3, Last=7 (Odd, Odd)
    ([5555], 1),                    # First=5, Last=5 (Odd, Odd)
    ([7000], 0),                    # First=7, Last=0 (Odd, Even)
    
    # Mixed complex case
    ([11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 102], 6), 
    # Valid: 11, 33, 55, 77, 99, 101
])
def test_special_filter(nums, expected):
    """
    Tests the specialFilter function against various scenarios including 
    boundary values, parity checks, and multi-digit numbers.
    """
    assert specialFilter(nums) == expected