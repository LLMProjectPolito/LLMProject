
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
import math

@pytest.mark.parametrize("nums, expected", [
    ([10, 11, 12, 21, 101, 3007], 3),
    ([11, 1000000000000000000000000001, 13, 31, 9, 10, -11, 121], 5),
    ([11, 9, 10, 1001, 21, 12, -11], 2),
])
def test_specialFilter_edge_cases(nums, expected):
    assert specialFilter(nums) == expected