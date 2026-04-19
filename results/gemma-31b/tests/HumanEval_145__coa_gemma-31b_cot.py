
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


# Focus: Boundary Values
def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([42]) == [42]

def test_order_by_points_same_sum_stability():
    # All elements have a digit sum of 1; should maintain original order
    assert order_by_points([10, 1, 100]) == [10, 1, 100]

# Focus: Type Scenarios
def test_order_by_points_empty():
    """Test with an empty list to ensure it handles the base case of the input type."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test with a single-element list to ensure it handles the minimum non-empty size."""
    assert order_by_points([42]) == [42]

def test_order_by_points_large_integers():
    """Test with very large integers to ensure the digit sum logic handles large numeric types."""
    # Both 10**10 and 100 have a digit sum of 1.
    # Stable sort should preserve their original relative order.
    assert order_by_points([10000000000, 100]) == [10000000000, 100]

# Focus: Logic Branches
import pytest

def test_order_by_points_stability():
    # Tests the logic branch where multiple items have the same digit sum.
    # They should remain in their original relative order (stable sort).
    assert order_by_points([10, 1, 20, 2]) == [10, 1, 20, 2]
    assert order_by_points([11, 2, 20]) == [11, 2, 20]

def test_order_by_points_sorting_logic():
    # Tests the logic branch where items have different digit sums.
    # Should sort in ascending order of the sums.
    assert order_by_points([30, 10, 20]) == [10, 20, 30]
    assert order_by_points([100, 11, 1]) == [100, 1, 11]

def test_order_by_points_edge_cases():
    # Tests the logic branches for empty lists and single-element lists.
    assert order_by_points([]) == []
    assert order_by_points([5]) == [5]