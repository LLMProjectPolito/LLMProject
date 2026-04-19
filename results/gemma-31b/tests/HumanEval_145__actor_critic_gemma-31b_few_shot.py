
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
    assert order_by_points([10]) == [10]
    assert order_by_points([-5]) == [-5]

def test_order_by_points_basic_sorting():
    """Tests basic sorting based on the sum of digits."""
    # Sums: 15(6), 20(2), 11(2), 30(3)
    # Sorted sums: 2, 2, 3, 6
    # Stable sort: 20, 11, 30, 15
    assert order_by_points([15, 20, 11, 30]) == [20, 11, 30, 15]

def test_order_by_points_stability():
    """Tests that elements with the same digit sum maintain their original relative order."""
    # All these have a digit sum of 1
    input_list = [10, 1, 100, -1, -10]
    # Since all sums are 1, the order should remain exactly the same
    assert order_by_points(input_list) == input_list

def test_order_by_points_negatives():
    """Tests that negative numbers are handled (sum of digits usually based on absolute value)."""
    # -11 (sum 2), -20 (sum 2), -1 (sum 1)
    # Sorted: -1 (1), -11 (2), -20 (2)
    assert order_by_points([-11, -20, -1]) == [-1, -11, -20]

def test_order_by_points_mixed_signs():
    """Tests sorting with a mix of positive and negative integers."""
    # 11 (2), -11 (2), 2 (2), -2 (2)
    # All sums are 2, should maintain original order
    input_list = [11, -11, 2, -2]
    assert order_by_points(input_list) == input_list

def test_order_by_points_large_numbers():
    """Tests sorting with larger integers."""
    # 999 (27), 100 (1), 1 (1), 55 (10)
    # Sorted sums: 1, 1, 10, 27
    # Stable: 100, 1, 55, 999
    assert order_by_points([999, 100, 1, 55]) == [100, 1, 55, 999]

def test_order_by_points_zeros():
    """Tests that zeros are handled correctly (sum is 0)."""
    # 0 (0), 10 (1), 0 (0)
    # Sorted: 0, 0, 10
    assert order_by_points([0, 10, 0]) == [0, 0, 10]