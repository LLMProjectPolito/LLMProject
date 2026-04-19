
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

@pytest.mark.parametrize("input_list, expected_count", [
    ([11, 1000000001, 101, 12, 21, 10, 9, -11], 3),
    ([11, 10001, 10, -11, 121, 202], 3),
    ([11, 10, -11, 101, 110, 135, 235, 1000000001], 4),
])
def test_specialFilter_edge_cases(input_list, expected_count):
    """
    Tests specialFilter with various edge cases:
    - Minimum value > 10 with odd first/last digits (11)
    - Large numbers with internal zeros (1000000001, 10001)
    - Numbers with odd boundaries but even internals (101, 121)
    - Boundary values not > 10 (10, 9)
    - Negative numbers ( -11)
    - Numbers with only one odd boundary (12, 21, 110, 235)
    """
    assert specialFilter(input_list) == expected_count