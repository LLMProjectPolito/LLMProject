
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

def test_order_by_points_positive():
    nums = [1, 11, -1, -11, -12]
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(nums) == expected

def test_empty_input():
    assert order_by_points([]) == []

def test_order_by_points_wrong_type():
    """Test with a list containing a string."""
    try:
        order_by_points([1, 2, "a"])
    except TypeError:
        assert True
    else:
        assert False