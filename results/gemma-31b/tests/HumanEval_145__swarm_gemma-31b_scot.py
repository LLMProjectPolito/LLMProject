
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

import pytest
import math

@pytest.mark.parametrize("nums, expected", [
    # Test case focusing on stability and the handling of negative numbers and zero.
    ([10, -10, 2, -2, 1, -1, 0], [0, 10, -10, 1, -1, 2, -2]),
    # Test with a mix of zeros, negatives, and multiple elements sharing the same digit sum.
    ([10, -10, 0, 1, -1, 100, 2], [0, 10, -10, 1, -1, 100, 2]),
    # Tests stability when multiple numbers share the same digit sum.
    ([10, -1, 100, -10, 0, 1], [0, 10, -1, 100, -10, 1]),
])
def test_order_by_points_stability_and_negatives(nums, expected):
    """
    Verifies that order_by_points performs a stable sort based on the 
    absolute digit sum, correctly handling zero and negative integers.
    """
    assert order_by_points(nums) == expected