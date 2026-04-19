
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
    ([10, 20, 30], [10, 20, 30]),
    ([30, 20, 10], [10, 20, 30]),
    
    # Stable sort: items with same sum should maintain original relative order
    ([10, 1, 100], [10, 1, 100]), # All have sum 1
    ([11, 2, 20], [2, 20, 11]),   # 2 and 20 have sum 2, 11 has sum 2. Wait: 2(2), 20(2), 11(2). All sum 2.
    ([11, 2, 20], [11, 2, 20]),   # All sum 2, should remain in order
    
    # Negative numbers (sum of digits of absolute value)
    ([-1, -11, -12], [-1, -11, -12]), # Sums: 1, 2, 3
    ([-12, -11, -1], [-1, -11, -12]), # Sums: 3, 2, 1
    
    # Mixed positive and negative
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # Sums: 1, 2, 1, 2, 3 -> Stable sort: (1,0), (1,2), (2,1), (2,3), (3,4)
    ([-1, 1, -11, 11], [-1, 1, -11, 11]),           # Sums: 1, 1, 2, 2
    
    # Large numbers
    ([999, 1000, 11], [1000, 11, 999]), # Sums: 27, 1, 2
    
    # Zeros
    ([0, 0, 0], [0, 0, 0]),
    ([10, 0, 1], [0, 10, 1]), # Sums: 1, 0, 1 -> Stable: 0, 10, 1
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected

def test_order_by_points_stability():
    """Explicitly test that the sort is stable for elements with the same digit sum."""
    # All these numbers have a digit sum of 2
    nums = [2, 11, 20, 101, 110, 200]
    # Since they all have the same sum, the output should be identical to the input
    assert order_by_points(nums) == nums

def test_order_by_points_large_negatives():
    """Test with large negative numbers to ensure absolute value is handled."""
    nums = [-99, -10, -1]
    # Sums: 18, 1, 1
    # Stable sort: -10 (idx 1), -1 (idx 2), -99 (idx 0)
    assert order_by_points(nums) == [-10, -1, -99]