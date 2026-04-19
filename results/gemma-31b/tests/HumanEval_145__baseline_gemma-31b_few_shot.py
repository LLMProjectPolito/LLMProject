
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
    """Tests that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Tests that a list with one element remains unchanged."""
    assert order_by_points([42]) == [42]

def test_order_by_points_basic_sorting():
    """Tests basic sorting based on the sum of digits."""
    # Sums: 1 (1), 2 (11), 1 (10) -> Sorted sums: 1, 1, 2
    # Stable sort: [1, 10, 11]
    assert order_by_points([1, 11, 10]) == [1, 10, 11]
    
    # Sums: 3 (12), 1 (10), 2 (11) -> Sorted sums: 1, 2, 3
    # Result: [10, 11, 12]
    assert order_by_points([12, 10, 11]) == [10, 11, 12]

def test_order_by_points_stability():
    """Tests that the original order is preserved for elements with the same digit sum."""
    # All these have a digit sum of 2
    # Original order: [20, 11, 2]
    assert order_by_points([20, 11, 2]) == [20, 11, 2]
    
    # All these have a digit sum of 1
    # Original order: [100, 10, 1]
    assert order_by_points([100, 10, 1]) == [100, 10, 1]

def test_order_by_points_negatives():
    """Tests that negative numbers are handled (typically using the sum of digits of their absolute value)."""
    # Sums: -1 (1), -11 (2), -10 (1) -> Sorted sums: 1, 1, 2
    # Stable sort: [-1, -10, -11]
    assert order_by_points([-1, -11, -10]) == [-1, -10, -11]

def test_order_by_points_mixed():
    """Tests a mix of positive and negative integers."""
    # Input: [1, 11, -1, -11, -12]
    # Sums: 1: 1, 11: 2, -1: 1, -11: 2, -12: 3
    # Sorted by sum (1, 1, 2, 2, 3) and stable:
    # Sum 1: 1 (idx 0), -1 (idx 2)
    # Sum 2: 11 (idx 1), -11 (idx 3)
    # Sum 3: -12 (idx 4)
    # Expected: [1, -1, 11, -11, -12]
    assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]

def test_order_by_points_large_numbers():
    """Tests sorting with larger integers."""
    # Sums: 999 (27), 1000 (1), 55 (10)
    # Sorted: [1000, 55, 999]
    assert order_by_points([999, 1000, 55]) == [1000, 55, 999]