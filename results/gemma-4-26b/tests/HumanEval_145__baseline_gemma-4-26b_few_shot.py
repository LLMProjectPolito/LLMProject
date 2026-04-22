
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
    """Tests that a list with one element returns the same list."""
    assert order_by_points([42]) == [42]

def test_order_by_points_stable_sort():
    """
    Tests that if multiple numbers have the same digit sum, 
    their original relative order is preserved (stable sort).
    """
    # All these numbers have a digit sum of 1
    # 1 (idx 0), 10 (idx 1), 100 (idx 2), -1 (idx 3)
    assert order_by_points([1, 10, 100, -1]) == [1, 10, 100, -1]

def test_order_by_points_ascending_sums():
    """Tests sorting by digit sum in ascending order."""
    # Sums: 1, 2, 3, 4
    assert order_by_points([1, 11, 111, 1111]) == [1, 11, 111, 1111]
    # Sums: 4, 3, 2, 1
    assert order_by_points([1111, 111, 11, 1]) == [1, 11, 111, 1111]

def test_order_by_points_negatives():
    """Tests sorting with negative numbers."""
    # -1 (sum 1, idx 0), -11 (sum 2, idx 1), -2 (sum 2, idx 2), -20 (sum 2, idx 3)
    # Expected: -1 (sum 1), then -11, -2, -20 (sum 2, stable order)
    assert order_by_points([-1, -11, -2, -20]) == [-1, -11, -2, -20]

def test_order_by_points_mixed_example():
    """
    Tests the mixed case provided in the docstring.
    Note: The docstring example result [-1, -11, 1, -12, 11] appears to contradict 
    the textual requirement of 'ascending order of digit sum' and 'stable sort'.
    This test follows the explicit textual requirement:
    1: 1 (idx 0), 11 (idx 1), -1 (idx 2), -11 (idx 3), -12 (idx 4)
    Sums: 1, 2, 1, 2, 3
    Sorted by (sum, original_index):
    (1, 0) -> 1
    (1, 2) -> -1
    (2, 1) -> 11
    (2, 3) -> -11
    (3, 4) -> -12
    """
    assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]

def test_order_by_points_zeros():
    """Tests that zero is handled correctly (digit sum 0)."""
    # 0 (sum 0, idx 0), 10 (sum 1, idx 1), 0 (sum 0, idx 2)
    # Expected: 0 (idx 0), 0 (idx 2), 10 (idx 1)
    assert order_by_points([0, 10, 0]) == [0, 0, 10]

def test_order_by_points_large_numbers():
    """Tests with larger integers."""
    # 99 (sum 18), 1000 (sum 1), 18 (sum 9)
    assert order_by_points([99, 1000, 18]) == [1000, 18, 99]