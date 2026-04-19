
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

@pytest.mark.parametrize("nums, expected", [
    # Basic cases
    ([], []),
    ([1], [1]),
    ([10], [10]),
    ([0], [0]),
    
    # Sorting by sum of digits
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([10, 20, 30], [10, 20, 30]),
    ([30, 20, 10], [10, 20, 30]),
    ([100, 11, 2], [100, 2, 11]), # Sums: 1, 2, 2
    
    # Stability (original index)
    ([10, 1, 100], [10, 1, 100]), # All sums are 1
    ([20, 11, 2], [20, 11, 2]),   # All sums are 2
    ([11, 2, 20], [2, 11, 20]),   # Sums: 2, 2, 2 -> stable
    
    # Negative numbers (sum of digits of absolute value)
    ([-1, -2, -3], [-1, -2, -3]),
    ([-3, -2, -1], [-1, -2, -3]),
    ([-10, -1, -100], [-10, -1, -100]), # All sums are 1
    
    # Mixed positive and negative
    ([1, -1], [1, -1]),             # Sums: 1, 1 -> stable
    ([-1, 1], [-1, 1]),             # Sums: 1, 1 -> stable
    ([11, -1, 2], [-1, 11, 2]),     # Sums: 2, 1, 2 -> -1 first, then 11, 2
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # Sums: 1, 2, 1, 2, 3
    
    # Large numbers
    ([999, 1000], [1000, 999]),     # Sums: 27, 1
    ([12345, 54321], [12345, 54321]), # Sums: 15, 15 -> stable
    
    # Zeros and mixed signs
    ([0, -0, 10, -10], [0, -0, 10, -10]), # Sums: 0, 0, 1, 1 -> stable
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected

def test_order_by_points_stability_explicit():
    """Explicitly check that the sort is stable for items with the same digit sum."""
    # All these have a digit sum of 2
    nums = [11, 2, 20, -11, -2, -20]
    # Since they all have the same sum, the order should remain unchanged
    assert order_by_points(nums) == nums

def test_order_by_points_large_range():
    """Test with a larger range of numbers to ensure consistency."""
    nums = [100, 1, 10, 200, 2, 20]
    # Sums: 1, 1, 1, 2, 2, 2
    # Stable order: 100, 1, 10, 200, 2, 20
    assert order_by_points(nums) == [100, 1, 10, 200, 2, 20]