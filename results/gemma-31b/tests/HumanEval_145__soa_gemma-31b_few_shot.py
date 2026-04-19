
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

def get_digit_sum(n):
    """Helper to calculate sum of digits for testing purposes."""
    return sum(int(d) for d in str(abs(n)))

@pytest.mark.parametrize("nums, expected", [
    # Basic cases
    ([], []),
    ([0], [0]),
    ([5], [5]),
    
    # Already sorted by digit sum
    ([1, 2, 3, 10, 11]), # sums: 1, 2, 3, 1, 2 -> not sorted
    ([1, 10, 2, 11, 3]), # sums: 1, 1, 2, 2, 3 -> sorted
    
    # Reverse sorted by digit sum
    ([3, 11, 2, 10, 1]), # sums: 3, 2, 2, 1, 1 -> reverse
    ([1, 10, 2, 11, 3]), # expected result for the above
    
    # Stability tests (same digit sum, should maintain original order)
    ([10, 1, 100], [10, 1, 100]), # sums: 1, 1, 1
    ([20, 11, 2], [20, 11, 2]),   # sums: 2, 2, 2
    ([1, 2, 10], [1, 10, 2]),     # sums: 1, 2, 1 -> [1, 10, 2]
    
    # Negative numbers (digit sum usually based on absolute value)
    ([-1, -11, -12], [-1, -11, -12]), # sums: 1, 2, 3
    ([-12, -11, -1], [-1, -11, -12]), # sums: 3, 2, 1
    
    # Mixed positive and negative
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # sums: 1, 2, 1, 2, 3
    ([-10, 2, -20, 1], [-10, 1, 2, -20]), # sums: 1, 2, 2, 1 -> [ -10, 1, 2, -20]
    
    # Large numbers
    ([999, 1000, 11], [1000, 11, 999]), # sums: 27, 1, 2
    ([123456, 1], [1, 123456]), # sums: 21, 1
])
def test_order_by_points(nums, expected):
    """
    Tests that order_by_points sorts integers by the sum of their digits
    and maintains stability for items with the same sum.
    """
    assert order_by_points(nums) == expected

def test_order_by_points_stability():
    """
    Explicitly test stability with a larger set of identical digit sums.
    """
    # All these have a digit sum of 2
    nums = [2, 11, 20, 101, 110, 200]
    # Since they all have the same sum, the order should remain unchanged.
    assert order_by_points(nums) == nums

def test_order_by_points_large_range():
    """
    Test with a wide range of values.
    """
    nums = [10**9, 1, 10**9 - 1] # sums: 1, 1, 9*9=81
    # 10**9 and 1 both have sum 1. 10**9 comes first in original list.
    assert order_by_points(nums) == [10**9, 1, 10**9 - 1]

def test_order_by_points_all_negatives():
    """
    Test with only negative numbers.
    """
    nums = [-10, -1, -20, -2] # sums: 1, 1, 2, 2
    # Stable sort: -10 (1), -1 (1), -20 (2), -2 (2)
    assert order_by_points(nums) == [-10, -1, -20, -2]