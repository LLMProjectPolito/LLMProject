
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

def test_order_by_points_with_large_numbers():
    """Tests the function with large numbers to ensure digit sum calculation is correct."""
    nums = [1000, 100, 10, 1]
    expected = [1, 10, 100, 1000]
    assert order_by_points(nums) == expected