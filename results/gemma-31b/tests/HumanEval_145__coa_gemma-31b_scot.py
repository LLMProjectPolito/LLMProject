
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
    """Test the boundary case of an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_single_and_zero():
    """Test the boundary cases of a single element and the value zero."""
    assert order_by_points([0]) == [0]
    assert order_by_points([5]) == [5]

def test_order_by_points_stability():
    """Test the boundary case where multiple elements have the same digit sum to ensure stability."""
    # All elements have a digit sum of 1; they should remain in their original relative order.
    assert order_by_points([10, 1, 100, -1, -10]) == [10, 1, 100, -1, -10]

# Focus: Negative Number Handling
import pytest

def test_negative_numbers_digit_sum():
    """Test that negative numbers are sorted based on the sum of their absolute digits."""
    # -1 (sum 1), -11 (sum 2), -2 (sum 2), -12 (sum 3)
    # Expected order: -1, -11, -2, -12 (stable sort for -11 and -2)
    assert order_by_points([-11, -1, -2, -12]) == [-1, -11, -2, -12]

def test_mixed_signs_stability():
    """Test stability and digit sum handling with a mix of positive and negative integers."""
    # 10 (sum 1), -1 (sum 1), 11 (sum 2), -2 (sum 2)
    # Expected: [10, -1, 11, -2]
    assert order_by_points([10, -1, 11, -2]) == [10, -1, 11, -2]

def test_negative_numbers_different_sums():
    """Test sorting when negative numbers have significantly different digit sums."""
    # -100 (sum 1), -99 (sum 18), -11 (sum 2)
    # Expected: [-100, -11, -99]
    assert order_by_points([-99, -100, -11]) == [-100, -11, -99]

# Focus: Stability/Tie-breaking
import pytest

def test_order_by_points_stability_same_sum():
    """Test that elements with the same digit sum maintain their original relative order."""
    # All have digit sum of 1
    assert order_by_points([100, 10, 1]) == [100, 10, 1]
    # All have digit sum of 2
    assert order_by_points([20, 11, 2]) == [20, 11, 2]

def test_order_by_points_stability_mixed_sums():
    """Test stability when elements with the same sum are interspersed with others."""
    # Sums: 11(2), 2(2), 10(1), 20(2), 1(1)
    # Expected: Sum 1s (10, 1) then Sum 2s (11, 2, 20)
    assert order_by_points([11, 2, 10, 20, 1]) == [10, 1, 11, 2, 20]

def test_order_by_points_stability_with_negatives():
    """Test stability specifically for negative numbers with identical digit sums."""
    # Assuming digit sum of -10 is 1 and -1 is 1
    # Original order: -10, -1
    assert order_by_points([-10, -1]) == [-10, -1]