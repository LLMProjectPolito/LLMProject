
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
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([], 0),
    ([10], 0),
    ([11], 1),
    ([12], 0),
    ([21], 0),
    ([22], 0),
    ([135], 1),
    ([235], 0),
    ([136], 0),
    ([99], 1),
    ([-11], 0),
    ([-15], 0),
    ([101], 1),
    ([100], 0),
    ([1001], 1),
    ([2002], 0),
    ([3000], 0),
    ([3003], 1),
    ([5], 0),
    ([1000000001], 1),
])
def test_special_filter(nums, expected):
    assert specialFilter(nums) == expected

def test_special_filter_all_invalid():
    # None of these meet all three criteria (>10, first odd, last odd)
    nums = [2, 4, 6, 8, 10, 12, 21, 23, 41, 45, -11, -13, -15]
    assert specialFilter(nums) == 0

def test_special_filter_all_valid():
    # All meet criteria
    nums = [11, 13, 15, 31, 33, 35, 51, 53, 55, 71, 73, 75, 91, 93, 95, 101, 303, 505]
    assert specialFilter(nums) == len(nums)