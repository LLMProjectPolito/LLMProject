
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
    ([15, -73, 14, -15], 1), 
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge cases: empty list, zero, and boundary values
    ([], 0),
    ([0], 0),
    ([10], 0),
    ([11], 1),
    
    # Numbers <= 10 (should be ignored regardless of digits)
    ([1, 3, 5, 7, 9], 0),
    ([-11, -13, -15, -101, -303], 0),
    
    # First digit even, last digit odd (should fail)
    ([21, 43, 65, 87, 201, 403], 0),
    
    # First digit odd, last digit even (should fail)
    ([12, 34, 56, 78, 102, 304], 0),
    
    # Both digits even (should fail)
    ([22, 44, 66, 88, 202, 404], 0),
    
    # Both digits odd (Positive and > 10)
    ([11, 13, 31, 33, 55, 77, 99], 7),
    
    # Multi-digit and Large numbers
    ([101, 303, 505, 707, 909], 5),
    ([1001, 3003, 9999], 3),
    ([1000, 2000], 0),
    ([1000000001, 2000000001, 1000000002], 1),
    
    # Mixed cases
    ([11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 111], 6),
    ([11, 12, 21, 33, 10, 101, -11], 3),
])
def test_specialFilter_parametrized(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_large_input():
    # Test with a larger list to ensure performance/stability
    nums = [11] * 1000 + [22] * 1000
    assert specialFilter(nums) == 1000