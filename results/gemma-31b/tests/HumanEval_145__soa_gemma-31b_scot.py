
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
    ([0], [0]),
    ([5], [5]),
    # Already sorted by digit sum
    ([1, 2, 3], [1, 2, 3]),
    ([10, 11, 12], [10, 11, 12]),
    # Reverse sorted by digit sum
    ([3, 2, 1], [1, 2, 3]),
    ([12, 11, 10], [10, 11, 12]),
    # Stable sort: items with same digit sum should maintain original order
    ([11, 2, 20], [11, 2, 20]),  # Sums: 2, 2, 2
    ([10, 1, 100], [10, 1, 100]), # Sums: 1, 1, 1
    # Negative numbers (digit sum usually based on absolute value)
    ([-1, -2, -3], [-1, -2, -3]),
    ([-10, -11, -12], [-10, -11, -12]),
    ([-12, -11, -10], [-10, -11, -12]),
    # Mixed positive and negative
    ([1, -1, 11, -11], [1, -1, 11, -11]), # Sums: 1, 1, 2, 2
    ([-1, 1, -11, 11], [-1, 1, -11, 11]), # Sums: 1, 1, 2, 2
    # Large numbers
    ([999, 1000, 11], [1000, 11, 999]), # Sums: 27, 1, 2
    # Complex mixed case
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # Sums: 1, 2, 1, 2, 3
])
def test_order_by_points(nums, expected):
    """
    Tests the order_by_points function based on the requirement:
    1. Sort by sum of digits in ascending order.
    2. Maintain original index for ties (stable sort).
    """
    assert order_by_points(nums) == expected

def test_order_by_points_stability():
    """
    Explicitly test stability with a larger set of identical sums.
    """
    # All these have a digit sum of 2
    nums = [2, 11, 20, 101, 110, 200]
    # Since they all have the same sum, the order should remain unchanged.
    assert order_by_points(nums) == nums

def test_order_by_points_large_values():
    """
    Test with very large integers to ensure digit summation is robust.
    """
    nums = [10**10, 1, 10**10 - 1] 
    # 10**10: sum = 1
    # 1: sum = 1
    # 10**10 - 1: sum = 9 * 10 = 90
    # Expected: [10**10, 1, 9999999999]
    assert order_by_points(nums) == [10**10, 1, 10**10 - 1]

def test_order_by_points_zeros():
    """
    Test behavior with zeros.
    """
    nums = [0, 0, 0]
    assert order_by_points(nums) == [0, 0, 0]
    
    nums_mixed_zero = [10, 0, 1]
    # Sums: 1, 0, 1
    # Sorted: 0 (sum 0), 10 (sum 1), 1 (sum 1)
    assert order_by_points(nums_mixed_zero) == [0, 10, 1]