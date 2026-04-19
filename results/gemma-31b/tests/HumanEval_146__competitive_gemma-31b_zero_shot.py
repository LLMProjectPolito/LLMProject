
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
    ([11], 1),
    ([10], 0),
    ([12], 0),
    ([21], 0),
    ([22], 0),
    ([101], 1),
    ([102], 0),
    ([201], 0),
    ([303], 1),
    ([999], 1),
    ([1000], 0),
    ([1001], 1),
    ([-11], 0),
    ([5], 0),
    ([135, 357, 579, 791, 913], 5),
    ([20, 40, 60, 80], 0),
    ([11, 13, 15, 17, 19], 5),
    ([1000000001], 1),
    ([2000000001], 0),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected