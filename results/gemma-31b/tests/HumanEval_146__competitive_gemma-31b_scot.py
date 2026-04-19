
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
    ([101], 1),
    ([102], 0),
    ([201], 0),
    ([202], 0),
    ([13579], 1),
    ([23578], 0),
    ([-11], 0),
    ([1, 3, 5, 7, 9], 0),
    ([11, 13, 15, 17, 19], 5),
    ([31, 33, 35, 37, 39], 5),
    ([51, 53, 55, 57, 59], 5),
    ([71, 73, 75, 77, 79], 5),
    ([91, 93, 95, 97, 99], 5),
    ([100, 200, 300], 0),
    ([1001], 1),
    ([1002], 0),
    ([2001], 0),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected