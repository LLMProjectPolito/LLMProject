
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

def test_basic():
    assert order_by_points([15, 20, 11, 3]) == [20, 11, 3, 15]

def test_stability():
    # Extreme case: All numbers have the same sum of digits.
    # This tests if the function maintains the original index order (stability).
    assert order_by_points([10, 1, 100, -1, -10]) == [10, 1, 100, -1, -10]

import pytest

def test_order_by_points_wrong_types():
    with pytest.raises(TypeError):
        order_by_points([1, "2", 3])