
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
    # Examples from docstring
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge Cases: Empty and Small lists
    ([], 0),
    ([11], 1),
    ([10], 0),
    ([9], 0),
    
    # Condition: Greater than 10
    ([10, 9, 0, -1, -11, -15], 0),
    ([-11, -13, -15, -31, -33], 0),
    ([-101, -909], 0),
    
    # Condition: First digit odd, Last digit odd
    ([11], 1), # 1 odd, 1 odd
    ([12], 0), # 1 odd, 2 even
    ([21], 0), # 2 even, 1 odd
    ([22], 0), # 2 even, 2 even
    ([31], 1), # 3 odd, 1 odd
    ([32], 0), # 3 odd, 2 even
    ([41], 0), # 4 even, 1 odd
    ([55], 1), # 5 odd, 5 odd
    
    # Multi-digit numbers
    ([101], 1), # 1 odd, 1 odd
    ([102], 0), # 1 odd, 2 even
    ([201], 0), # 2 even, 1 odd
    ([303], 1), # 3 odd, 3 odd
    ([1009], 1), # 1 odd, 9 odd
    ([9001], 1), # 9 odd, 1 odd
    ([1000], 0), # 1 odd, 0 even
    
    # Mixed lists and bulk tests
    ([11, 13, 15, 17, 19], 5),
    ([21, 23, 25, 27, 29], 0),
    ([10, 12, 14, 16, 18], 0),
    ([111, 222, 333, 444, 555], 3), # 111, 333, 555
    ([10, 11, 20, 21, 30, 31], 2), # 11, 31
    ([11, 12, 21, 22, 101, 102, 201, 111, 9, -11, 10, 307], 4), # 11, 101, 111, 307
])
def test_specialFilter_parametrized(nums, expected):
    assert specialFilter(nums) == expected

def test_specialFilter_large_numbers():
    # Testing very large numbers to ensure digit extraction is robust
    # 1000000001: >10, first 1 (odd), last 1 (odd) -> Match
    # 2000000001: >10, first 2 (even) -> Fail
    # 1000000002: >10, last 2 (even) -> Fail
    # 3000000003: >10, first 3 (odd), last 3 (odd) -> Match
    assert specialFilter([1000000001, 2000000001, 1000000002]) == 1
    assert specialFilter([3000000003]) == 1

def test_specialFilter_all_fail():
    # Test cases where no element should pass
    assert specialFilter([2, 4, 6, 8, 10]) == 0
    assert specialFilter([21, 41, 61, 81]) == 0
    assert specialFilter([12, 14, 16, 18]) == 0
    assert specialFilter([22, 44, 66, 88]) == 0