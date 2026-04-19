
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
    # Provided example cases
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge Case: Empty list
    ([], 0),
    
    # Edge Case: Numbers <= 10 (should all be ignored)
    ([10, 9, 8, 0, -1, -11, -15], 0),
    ([1, 3, 5, 7, 9], 0),
    
    # Digit Parity Logic: Numbers > 10
    ([11], 1),              # Min boundary: Odd-Odd
    ([21, 41, 61, 81], 0),  # First digit even, last odd
    ([12, 14, 16, 18], 0),  # First digit odd, last even
    ([22, 44, 66, 88], 0),  # Both digits even
    ([13, 31, 55, 79, 97], 5), # All satisfying
    
    # Multi-digit and Large Numbers
    ([101], 1),             # 3 digits: 1(O), 1(O)
    ([102], 0),             # 3 digits: 1(O), 2(E)
    ([201], 0),             # 3 digits: 2(E), 1(O)
    ([3003], 1),            # 4 digits: 3(O), 3(O)
    ([1000000001], 1),      # Large: 1(O), 1(O)
    ([10000000000000000000001], 1), # Extremely large: 1(O), 1(O)
    ([20000000000000000000001], 0), # Extremely large: 2(E), 1(O)
    ([1357913579, 2468024680, 1000000001], 2), # Valid: 1357913579, 1000000001
    
    # Mixed cases
    ([11, 12, 13, 23, 33, 34, 43, 53, 10, 9], 4), # 11, 13, 33, 53
    ([11, 12, 21, 22, 33, 34, 43, 44, 55], 3),    # 11, 33, 55
    
    # Negative numbers that look valid if absolute value is used
    ([-11, -33, -55, -101], 0), # Must be > 10
])
def test_special_filter_parametrized(nums, expected):
    """Test specialFilter across basic, boundary, and parity scenarios."""
    assert specialFilter(nums) == expected

def test_special_filter_all_valid():
    """Test a list where every single element meets the criteria."""
    nums = [11, 33, 55, 77, 99, 101, 303, 505, 707, 909]
    assert specialFilter(nums) == 10

def test_special_filter_none_valid():
    """Test a list where no elements meet the criteria."""
    nums = [2, 4, 6, 8, 10, 12, 21, 22, 40, -11, -13]
    assert specialFilter(nums) == 0

def test_special_filter_digit_extremes():
    """Test numbers > 10 consisting only of even or only of odd digits."""
    # Only even digits: should be 0 because first/last are even
    assert specialFilter([20, 22, 24, 26, 28, 40, 42, 60, 88]) == 0
    # Only odd digits: should all be valid
    assert specialFilter([11, 13, 15, 31, 33, 35, 51, 53, 55]) == 9