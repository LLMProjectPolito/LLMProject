
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
    assert order_by_points([-5]) == [-5]
    assert order_by_points([0]) == [0]

def test_order_by_points_basic_sorting():
    """Tests basic ascending sort by digit sum."""
    # 10 (sum 1), 20 (sum 2), 30 (sum 3)
    assert order_by_points([10, 20, 30]) == [10, 20, 30]
    # 30 (sum 3), 20 (sum 2), 10 (sum 1)
    assert order_by_points([30, 20, 10]) == [10, 20, 30]
    # Mixed: 100 (sum 1), 2 (sum 2), 11 (sum 2), 12 (sum 3)
    assert order_by_points([12, 11, 2, 100]) == [100, 11, 2, 12]

def test_order_by_points_stability():
    """
    Tests that items with the same digit sum maintain their 
    original relative order (stable sort).
    """
    # All have digit sum of 1. Original order should be preserved.
    assert order_by_points([1, 10, 100, -1, -10]) == [1, 10, 100, -1, -10]
    
    # Mix of sums:
    # 11 (sum 2, index 0), 2 (sum 2, index 1), 20 (sum 2, index 2)
    # 1 (sum 1, index 3)
    # 12 (sum 3, index 4)
    assert order_by_points([11, 2, 20, 1, 12]) == [1, 11, 2, 20, 12]

def test_order_by_points_negative_numbers():
    """
    Tests that negative numbers are handled correctly using absolute value for digit sum.
    """
    # -1 (sum 1), -11 (sum 2), -12 (sum 3)
    assert order_by_points([-12, -11, -1]) == [-1, -11, -12]
    
    # Mix of positive and negative with same sums
    # 1 (sum 1), -1 (sum 1), 11 (sum 2), -11 (sum 2)
    assert order_by_points([1, -1, 11, -11]) == [1, -1, 11, -11]

def test_order_by_points_large_numbers():
    """Tests handling of large integers."""
    # 999 (sum 27), 1000 (sum 1)
    assert order_by_points([999, 1000]) == [1000, 999]
    # 12345 (sum 15), 54321 (sum 15) -> Stable
    assert order_by_points([12345, 54321]) == [12345, 54321]

def test_order_by_points_zeros():
    """Tests behavior with zero."""
    assert order_by_points([0, 0, 0]) == [0, 0, 0]
    assert order_by_points([0, 1, 0]) == [0, 0, 1]
    assert order_by_points([10, 0, 1]) == [0, 10, 1]

def test_order_by_points_complex_mix():
    """Test a complex mix of values."""
    # 100 (1), 22 (4), -10 (1), -5 (5), 0 (0)
    # Sorted sums: 0, 1, 1, 4, 5
    # Stable order: 0, 100, -10, 22, -5
    assert order_by_points([100, 22, -10, -5, 0]) == [0, 100, -10, 22, -5]

def test_order_by_points_mixed_numbers():
    """General case with variety of integers."""
    nums = [1, 11, -1, -11, -12]
    # Sums: 1(1), 11(2), -1(1), -11(2), -12(3)
    # Stable sort by sum: 
    # Sum 1: 1, -1
    # Sum 2: 11, -11
    # Sum 3: -12
    assert order_by_points(nums) == [1, -1, 11, -11, -12]