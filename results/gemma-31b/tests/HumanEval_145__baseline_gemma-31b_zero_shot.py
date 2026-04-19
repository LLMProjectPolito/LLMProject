
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

def test_order_by_points_empty():
    """Test that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test that a list with one element returns the same list."""
    assert order_by_points([10]) == [10]
    assert order_by_points([-10]) == [-10]
    assert order_by_points([0]) == [0]

def test_order_by_points_positive_numbers():
    """Test sorting with only positive integers."""
    # 10 (sum 1), 2 (sum 2), 11 (sum 2)
    assert order_by_points([10, 2, 11]) == [10, 2, 11]
    # 30 (sum 3), 20 (sum 2), 10 (sum 1)
    assert order_by_points([30, 20, 10]) == [10, 20, 30]

def test_order_by_points_negative_numbers():
    """
    Test sorting with only negative integers.
    Rule derived from example: first digit is negative, subsequent digits are positive.
    -1: -1
    -11: -1 + 1 = 0
    -12: -1 + 2 = 1
    -21: -2 + 1 = -1
    """
    # -1 (sum -1), -11 (sum 0), -12 (sum 1)
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]
    # -12 (sum 1), -11 (sum 0), -1 (sum -1)
    assert order_by_points([-12, -11, -1]) == [-1, -11, -12]
    # -21 (sum -1), -1 (sum -1) -> stable sort
    assert order_by_points([-21, -1]) == [-21, -1]

def test_order_by_points_mixed_numbers():
    """Test sorting with a mix of positive and negative integers."""
    # Example from problem description:
    # 1: sum 1
    # 11: sum 2
    # -1: sum -1
    # -11: sum 0
    # -12: sum 1
    # Sorted sums: -1 (-1), 0 (-11), 1 (1), 1 (-12), 2 (11)
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_stability():
    """Test that the sort is stable (maintains original order for equal sums)."""
    # All sum to 1: 1, 10, 100
    assert order_by_points([1, 10, 100]) == [1, 10, 100]
    assert order_by_points([100, 10, 1]) == [100, 10, 1]
    
    # Mixed stability:
    # -12: -1+2 = 1
    # 1: 1
    # 10: 1
    assert order_by_points([-12, 1, 10]) == [-12, 1, 10]
    assert order_by_points([1, 10, -12]) == [1, 10, -12]

def test_order_by_points_zero():
    """Test behavior with zero."""
    # 0: sum 0
    # -1: sum -1
    # 1: sum 1
    assert order_by_points([0, 1, -1]) == [-1, 0, 1]

def test_order_by_points_large_values():
    """Test with larger integers to ensure digit summation logic is correct."""
    # -100: -1+0+0 = -1
    # -101: -1+0+1 = 0
    # 100: 1+0+0 = 1
    # 101: 1+0+1 = 2
    assert order_by_points([101, 100, -101, -100]) == [-100, -101, 100, 101]