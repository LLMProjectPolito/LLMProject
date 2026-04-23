
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
    """Tests that a list with a single element returns the same list."""
    assert order_by_points([1]) == [1]
    assert order_by_points([-5]) == [-5]
    assert order_by_points([0]) == [0]

def test_order_by_points_positive_numbers():
    """Tests sorting of positive integers (ascending, descending, and large)."""
    assert order_by_points([1, 22, 333]) == [1, 22, 333]
    assert order_by_points([3, 2, 1]) == [1, 2, 3]
    assert order_by_points([1000000, 1, 100]) == [1, 100, 1000000]

def test_order_by_points_negative_numbers():
    """Tests sorting of negative and mixed numbers."""
    # Sums (abs): -1 (1), -11 (2), -10 (1), -2 (2)
    # Stable sort: -1 (idx 0), -10 (idx 2), -11 (idx 1), -2 (idx 3)
    assert order_by_points([-1, -11, -10, -2]) == [-1, -10, -11, -2]
    
    # Mixed: 1 (1, idx 0), 11 (2, idx 1), -1 (1, idx 2), -11 (2, idx 3), -12 (3, idx 4)
    # Stable sort: 1, -1, 11, -11, -12
    assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]

def test_order_by_points_stability():
    """Tests the tie-breaker rule: if sums are equal, preserve original index order."""
    # Sums: 1, 1, 2, 2
    assert order_by_points([10, 1, 20, 2]) == [10, 1, 20, 2]
    # Sums: 1, 1, 1
    assert order_by_points([100, 10, 1]) == [100, 10, 1]
    # Sums: 1, 1, 1, 1
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]
    # All sums are 2
    assert order_by_points([11, 2, 20, 101, 110]) == [11, 2, 20, 101, 110]

def test_order_by_points_zeros():
    """Tests the behavior with zero."""
    # Sums: 0, 1, 0, 1
    assert order_by_points([0, 10, 0, 1]) == [0, 0, 10, 1]
    # Sums: 1, 0, 1
    assert order_by_points([1, 0, -1]) == [0, 1, -1]

def test_order_by_points_large_digit_sums():
    """Tests numbers with large digit sums and large values."""
    # Sums: 27, 1, 2
    assert order_by_points([999, 100, 11]) == [100, 11, 999]
    # Sums: 9, 9, 1
    assert order_by_points([18, 9, 1000000]) == [1000000, 18, 9]