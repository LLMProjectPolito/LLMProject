
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
    assert order_by_points([20, 10, 11]) == [10, 20, 11]

def test_empty():
    assert order_by_points([]) == []

import pytest

def test_order_by_points_wrong_type():
    with pytest.raises(TypeError):
        order_by_points([1, "2", 3])