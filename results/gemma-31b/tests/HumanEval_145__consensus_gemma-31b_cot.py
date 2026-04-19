
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
    """Test that a single element list returns the same list."""
    assert order_by_points([10]) == [10]
    assert order_by_points([-10]) == [-10]
    assert order_by_points([0]) == [0]

def test_order_by_points_already_sorted():
    """Test with a list that is already sorted by digit sum."""
    # Sums: 1, 2, 3
    assert order_by_points([1, 11, 12]) == [1, 11, 12]
    # Sums: 0, 1, 2
    assert order_by_points([0, 10, 20]) == [0, 10, 20]

def test_order_by_points_reverse_sorted():
    """Test with a list that is reverse sorted by digit sum."""
    # Sums: 3, 2, 1
    assert order_by_points([12, 11, 1]) == [1, 11, 12]
    # Sums: 9, 5, 1
    assert order_by_points([9, 14, 10]) == [10, 14, 9]

def test_order_by_points_stability():
    """Test that the sort is stable (maintains original index for ties)."""
    # All have sum 1. Should maintain order.
    assert order_by_points([1, 10, 100, -1, -10]) == [1, 10, 100, -1, -10]
    
    # Mix of sums: 1 (10), 2 (11), 1 (1), 2 (2)
    # Sorted sums: 1, 1, 2, 2
    # Stable order: 10 (idx 0), 1 (idx 2), 11 (idx 1), 2 (idx 3)
    assert order_by_points([10, 11, 1, 2]) == [10, 1, 11, 2]

def test_order_by_points_negative_numbers():
    """Test that negative numbers are handled correctly (sum of digits of absolute value)."""
    # Sums: 3, 2, 1
    assert order_by_points([-12, -11, -1]) == [-1, -11, -12]
    # Sums: 1, 2, 1
    # Stable order: -1, -10, -2
    assert order_by_points([-1, -2, -10]) == [-1, -10, -2]

def test_order_by_points_mixed_signs():
    """Test mixing positive and negative numbers."""
    # 1: sum 1, 11: sum 2, -1: sum 1, -11: sum 2, -12: sum 3
    # Sorted sums: 1, 1, 2, 2, 3
    # Stable order: 1 (0), -1 (2), 11 (1), -11 (3), -12 (4)
    assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]

def test_order_by_points_large_numbers():
    """Test with larger integers."""
    # 999: 27, 1000: 1, 111: 3
    assert order_by_points([999, 1000, 111]) == [1000, 111, 999]
    # 1000001: 2, 1000000: 1
    assert order_by_points([1000001, 1000000]) == [1000000, 1000001]

def test_order_by_points_zeros():
    """Test with zeros."""
    # 0: sum 0, 10: sum 1, 0: sum 0
    # Sorted: 0 (0), 0 (2), 10 (1)
    assert order_by_points([0, 10, 0]) == [0, 0, 10]
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_order_by_points_all_same_sum():
    """Test where all elements have the same digit sum."""
    nums = [11, 20, 101, 110, 2]
    # All sum to 2
    assert order_by_points(nums) == nums