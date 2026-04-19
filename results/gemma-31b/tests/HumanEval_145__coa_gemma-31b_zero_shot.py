
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
    assert order_by_points([0]) == [0]

def test_order_by_points_stability():
    # All elements have a digit sum of 2. 
    # Should maintain original order based on the stability requirement.
    assert order_by_points([11, 2, 20]) == [11, 2, 20]

# Focus: Value Scenarios
import pytest

def test_order_by_points_mixed_stability():
    # -2: sum -2, -11: sum 0, 11: sum 2, 2: sum 2
    # 11 and 2 have the same sum; 11 appears first in original list.
    assert order_by_points([11, -11, 2, -2]) == [-2, -11, 11, 2]

def test_order_by_points_negatives():
    # -20: -2+0 = -2, -1: -1, -11: -1+1 = 0
    assert order_by_points([-1, -11, -20]) == [-20, -1, -11]

def test_order_by_points_empty_and_zero():
    assert order_by_points([]) == []
    assert order_by_points([0]) == [0]

# Focus: Logic Branches
import pytest

def test_order_by_points_empty():
    """Test the logic branch for an empty input list."""
    assert order_by_points([]) == []

def test_order_by_points_stability():
    """Test the logic branch where multiple items have the same digit sum (stable sort)."""
    # 11 (sum 2), 20 (sum 2), 2 (sum 2) -> should maintain original order
    assert order_by_points([11, 20, 2]) == [11, 20, 2]
    # 10 (sum 1), 11 (sum 2), 2 (sum 2) -> 10 first, then 11 and 2 in original order
    assert order_by_points([10, 11, 2]) == [10, 11, 2]

def test_order_by_points_mixed_values():
    """Test the logic branch for mixed positive and negative integers with varying digit sums."""
    # -1 (sum 1), 11 (sum 2), 10 (sum 1), -12 (sum 3)
    # Sorted by sum: [-1, 10] (sum 1), [11] (sum 2), [-12] (sum 3)
    assert order_by_points([-1, 11, 10, -12]) == [-1, 10, 11, -12]