
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
    
    # Edge cases: Empty list and lists with no matches
    ([], 0),
    ([2, 4, 6, 8], 0),
    ([10], 0),
    ([9], 0),
    ([-11, -13, -15], 0),
    
    # Single element tests
    ([11], 1),
    ([12], 0),
    ([21], 0),
    ([22], 0),
    
    # Multi-digit tests
    ([101], 1),
    ([102], 0),
    ([201], 0),
    ([303], 1),
    ([555], 1),
    ([7009], 1),
    ([8009], 0),
    ([7008], 0),
    
    # Mixed lists and parity combinations
    ([11, 13, 15, 17, 19], 5),
    ([20, 30, 40, 50], 0),
    ([11, 22, 33, 44, 55], 3),
    ([21, 43, 65, 87], 0),
    ([12, 34, 56, 78], 0),
    ([22, 44, 66, 88, 20], 0),
    ([101, 303, 505, 707, 909], 5),
    ([100, 110, 120], 0),
    ([111, 222, 333], 2),
    ([10, 11, 12], 1),
    ([101, 111, 121, 131], 4),
    ([100, 200, 300], 0),
])
def test_specialFilter_parametrized(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_large_numbers():
    # Test with very large numbers to ensure digit extraction works
    assert specialFilter([1000000000000000000000000000001]) == 1
    assert specialFilter([2000000000000000000000000000001]) == 0
    assert specialFilter([3000000000000000000000000000007]) == 1
    assert specialFilter([1000000000000000000000000000002]) == 0