
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

@pytest.mark.parametrize("input_list, expected", [
    ([11, 10, 101, 100, -11, 9], 2),
    ([11, 101, -11, 10, 21, 12], 2),
    ([11, 12, 21, -11, 101], 2),
])
def test_special_filter_edge_cases(input_list, expected):
    assert specialFilter(input_list) == expected