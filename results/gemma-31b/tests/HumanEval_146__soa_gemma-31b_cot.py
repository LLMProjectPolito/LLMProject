
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
    ([15, -73, 14, -15], 1),            # Only 15 fits
    ([33, -2, -3, 45, 21, 109], 2),    # 33 and 109 fit
    ([], 0),                           # Empty list
    ([11, 13, 15, 17, 19], 5),         # All fit
    ([21, 23, 25, 27, 29], 0),         # First digit even
    ([10, 12, 14, 16, 18], 0),         # Last digit even or not > 10
    ([10, 9, 8, 7], 0),                # None > 10
    ([101, 303, 505, 707, 909], 5),    # Multi-digit, first and last odd
    ([100, 200, 300], 0),              # Last digit 0 is even
    ([1111, 2222, 3333], 2),           # 1111 and 3333 fit
    ([-11, -13, -15], 0),              # Negative numbers are not > 10
    ([1011, 1012, 1013], 2),           # 1011 and 1013 fit
    ([11, 11.0], 2),                   # Float representation of odd digits
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_large_numbers():
    # Test with very large numbers to ensure string conversion/digit check works
    nums = [100000000000000000001, 200000000000000000001, 300000000000000000003]
    assert specialFilter(nums) == 2

def test_specialFilter_boundary_10():
    # Test exactly 10 (should be False because it must be > 10)
    assert specialFilter([10]) == 0
    # Test 11 (should be True)
    assert specialFilter([11]) == 1