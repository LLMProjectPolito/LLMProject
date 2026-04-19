
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
    """Test with an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test with a single element list."""
    assert order_by_points([10]) == [10]
    assert order_by_points([-10]) == [-10]
    assert order_by_points([0]) == [0]

def test_order_by_points_already_sorted():
    """Test with a list already sorted by sum of digits."""
    # Sums: 1, 2, 3
    assert order_by_points([1, 11, 111]) == [1, 11, 111]

def test_order_by_points_reverse_sorted():
    """Test with a list sorted in reverse order of sum of digits."""
    # Sums: 3, 2, 1
    assert order_by_points([111, 11, 1]) == [1, 11, 111]

def test_order_by_points_stability():
    """Test that the sort is stable (maintains original index for equal sums)."""
    # Sums: 1, 1, 1
    # Original indices: 0, 1, 2
    assert order_by_points([10, 1, 100]) == [10, 1, 100]
    
    # Sums: 2, 2, 2
    # Original indices: 0, 1, 2
    assert order_by_points([11, 20, 101]) == [11, 20, 101]

def test_order_by_points_negative_numbers():
    """Test with negative numbers to ensure absolute value is used for digit sum."""
    # Sums: 1, 2, 3
    assert order_by_points([-1, -11, -111]) == [-1, -11, -111]
    # Sums: 3, 2, 1
    assert order_by_points([-111, -11, -1]) == [-1, -11, -111]

def test_order_by_points_mixed_signs():
    """Test with a mix of positive and negative numbers."""
    # Sums: 1, 1, 2, 2
    # Indices: 0, 1, 2, 3
    # Expected stable sort: [1, -1, 11, -11]
    assert order_by_points([1, -1, 11, -11]) == [1, -1, 11, -11]

def test_order_by_points_zeros():
    """Test with zeros."""
    assert order_by_points([0, 0, 0]) == [0, 0, 0]
    # Sums: 1, 0, 1
    assert order_by_points([10, 0, 1]) == [0, 10, 1]

def test_order_by_points_large_numbers():
    """Test with large numbers."""
    # Sums: 27, 1
    assert order_by_points([999, 1000]) == [1000, 999]
    # Sums: 1, 27
    assert order_by_points([1000, 999]) == [1000, 999]

def test_order_by_points_example_logic():
    """
    Test the logic described in the prompt text:
    'sorts the given list of integers in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits, order them based on their index in original list.'
    """
    # Input: [1, 11, -1, -11, -12]
    # Sums: 1, 2, 1, 2, 3
    # Stable sort by sum:
    # Sum 1: 1 (idx 0), -1 (idx 2)
    # Sum 2: 11 (idx 1), -11 (idx 3)
    # Sum 3: -12 (idx 4)
    # Result: [1, -1, 11, -11, -12]
    assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]