
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
    # All elements have a digit sum of 1; should maintain original relative order
    assert order_by_points([1, 10, 100, -1, -10]) == [1, 10, 100, -1, -10]

# Focus: Negative Number Handling
import pytest

def test_negative_numbers_sum_calculation():
    """Test that negative numbers are sorted based on the sum of their absolute digits."""
    # -1 (sum 1), -12 (sum 3), -21 (sum 3), -100 (sum 1)
    # Sorted by sum: -1 (1), -100 (1), -12 (3), -21 (3)
    assert order_by_points([-1, -12, -21, -100]) == [-1, -100, -12, -21]

def test_negative_numbers_stability():
    """Test that negative numbers with the same digit sum maintain their original relative order."""
    # -11 (sum 2), -20 (sum 2), -2 (sum 2)
    # All have sum 2, should remain in original order
    assert order_by_points([-11, -20, -2]) == [-11, -20, -2]

def test_mixed_signs_stability():
    """Test that mixed positive and negative numbers with the same digit sum maintain original order."""
    # 11 (sum 2), -2 (sum 2), 20 (sum 2), -11 (sum 2)
    # All have sum 2, should remain in original order
    assert order_by_points([11, -2, 20, -11]) == [11, -2, 20, -11]

# Focus: Stability
import pytest

def test_stability_identical_sums():
    """Test that elements with the same digit sum maintain their original relative order."""
    # All these numbers have a digit sum of 1
    nums = [10, 1, 100, -1, -10]
    assert order_by_points(nums) == [10, 1, 100, -1, -10]

def test_stability_interleaved_sums():
    """Test stability when elements with the same sums are separated by others."""
    # Sums: 10(1), 20(2), 1(1), 2(2)
    # Expected: [10, 1] (sum 1) then [20, 2] (sum 2)
    nums = [10, 20, 1, 2]
    assert order_by_points(nums) == [10, 1, 20, 2]

def test_stability_mixed_values():
    """Test stability with a mix of positive and negative integers with overlapping sums."""
    # Sums: 11(2), 2(2), -11(2), 20(2)
    # All have sum 2, should remain in original order
    nums = [11, 2, -11, 20]
    assert order_by_points(nums) == [11, 2, -11, 20]