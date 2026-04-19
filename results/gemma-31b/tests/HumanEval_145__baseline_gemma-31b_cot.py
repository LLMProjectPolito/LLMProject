
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

def test_order_by_points_example():
    """Test the example provided in the docstring."""
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    """Test with an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test with a single element list."""
    assert order_by_points([10]) == [10]
    assert order_by_points([-10]) == [-10]
    assert order_by_points([0]) == [0]

def test_order_by_points_all_positive():
    """Test with only positive integers."""
    # 10 -> 1, 2 -> 2, 11 -> 2
    # Stable sort: 10, 2, 11
    assert order_by_points([10, 2, 11]) == [10, 2, 11]
    # 1 -> 1, 10 -> 1, 2 -> 2
    assert order_by_points([1, 10, 2]) == [1, 10, 2]

def test_order_by_points_all_negative():
    """Test with only negative integers."""
    # -10 -> -1+0 = -1
    # -2 -> -2
    # -11 -> -1+1 = 0
    # Sorted: -2 (-2), -10 (-1), -11 (0)
    assert order_by_points([-10, -2, -11]) == [-2, -10, -11]

def test_order_by_points_zeros():
    """Test with zeros."""
    assert order_by_points([0, 0, 0]) == [0, 0, 0]
    # 0 -> 0, 1 -> 1, -1 -> -1
    # Sorted: -1, 0, 1
    assert order_by_points([0, 1, -1]) == [-1, 0, 1]

def test_order_by_points_stability():
    """Test that the sort is stable (maintains original order for ties)."""
    # 10 -> 1, 1 -> 1
    assert order_by_points([10, 1]) == [10, 1]
    assert order_by_points([1, 10]) == [1, 10]
    # -10 -> -1, -1 -> -1
    assert order_by_points([-10, -1]) == [-10, -1]
    assert order_by_points([-1, -10]) == [-1, -10]

def test_order_by_points_large_numbers():
    """Test with larger integers."""
    # 100 -> 1
    # -100 -> -1 + 0 + 0 = -1
    assert order_by_points([100, -100]) == [-100, 100]
    # 999 -> 27
    # -999 -> -9 + 9 + 9 = 9
    assert order_by_points([999, -999]) == [-999, 999]

def test_order_by_points_mixed_complex():
    """Test a more complex mixed list."""
    # 15 -> 6
    # -15 -> -1 + 5 = 4
    # 20 -> 2
    # -20 -> -2 + 0 = -2
    # 5 -> 5
    # -5 -> -5
    # Sums: 15:6, -15:4, 20:2, -20:-2, 5:5, -5:-5
    # Sorted sums: -5, -2, 2, 4, 5, 6
    # Result: [-5, -20, 20, -15, 5, 15]
    assert order_by_points([15, -15, 20, -20, 5, -5]) == [-5, -20, 20, -15, 5, 15]