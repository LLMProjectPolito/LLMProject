
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
    ([5], [5]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    
    # Stability: items with same digit sum should maintain original order
    ([10, 1, 100, 1000], [10, 1, 100, 1000]),
    ([12, 3, 21, 30], [12, 3, 21, 30]),
    
    # Negative numbers: digit sum is calculated on the absolute value
    ([-1, -11, -12], [-1, -11, -12]),
    ([-12, -11, -1], [-1, -11, -12]),
    
    # Mixed positive and negative numbers
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]),
    
    # Zeros
    ([0, 0, 0], [0, 0, 0]),
    ([10, 0, 1], [0, 10, 1]), # 0 (sum 0), 10 (sum 1), 1 (sum 1)
    
    # Large numbers
    ([99, 100, 1, 10], [100, 1, 10, 99]), # 100 (sum 1), 1 (sum 1), 10 (sum 1), 99 (sum 18)
    ([1000000, 1], [1000000, 1]), # Both sum to 1, stable sort
    
    # Complex mixed case
    # 20 (2), 11 (2), 3 (3), -1 (1), -2 (2), -10 (1)
    # Sums: -1:1, -10:1, 20:2, 11:2, -2:2, 3:3
    # Result: [-1, -10, 20, 11, -2, 3]
    ([20, 11, 3, -1, -2, -10], [-1, -10, 20, 11, -2, 3]),
])
def test_order_by_points(nums, expected):
    """
    Tests that order_by_points correctly sorts integers by the sum of their digits
    and maintains original order for ties (stable sort).
    """
    assert order_by_points(nums) == expected

def test_order_by_points_identity():
    """Test that sorting an already sum-sorted list returns the same list."""
    # Sums: 1, 3, 6, 4, 4
    # Sorted sums: 1, 3, 4, 4, 6 -> [1, 12, 4, 13, 123]
    assert order_by_points([1, 12, 4, 13, 123]) == [1, 12, 4, 13, 123]