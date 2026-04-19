
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
    ([11, 13, 15, 17, 19], 5),
    ([21, 23, 25, 27, 29], 0),
    ([10, 12, 14, 16, 18], 0),
    ([101, 303, 505, 707, 909], 5),
    ([102, 304, 506, 708, 900], 0),
    ([201, 403, 605, 807, 009], 0),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 0),
    ([-11, -13, -15], 0),
    ([111, 121, 131], 2),
    ([1001, 2002, 3003], 2),
    ([1000, 1002, 1004], 0),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected