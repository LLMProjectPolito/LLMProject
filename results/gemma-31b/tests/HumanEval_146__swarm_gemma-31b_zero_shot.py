
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
    ([11, 10, 9, -11, -13, 101, 1000000001], 3),
    ([11, 10, 9, -11, 101, 110, 211], 2),
    ([11, 10, 9, -11, 101, 100000000000000000001, 102, 201], 3),
])
def test_specialFilter_scenarios(input_list, expected):
    """
    Tests specialFilter with various edge cases including boundary values (>10),
    negative numbers, and very large integers.
    """
    assert specialFilter(input_list) == expected