
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
    ([], []),                                       # Empty list
    ([5], [5]),                                     # Single element
    ([10, 20, 30], [10, 20, 30]),                   # Already sorted by sum (1, 2, 3)
    ([30, 20, 10], [10, 20, 30]),                   # Reverse sorted by sum (3, 2, 1)
    
    # Stability (Equal sums should maintain original relative order)
    ([10, 1, 100], [10, 1, 100]),                   # Sums: 1, 1, 1
    ([11, 2, 20], [11, 2, 20]),                     # Sums: 2, 2, 2
    ([123, 321, 111], [111, 123, 321]),             # Sums: 6, 6, 3 -> 111 (3), 123 (6), 321 (6)
    
    # Negative numbers (Digit sum of absolute value)
    ([-1, -11, -12], [-1, -11, -12]),               # Sums: 1, 2, 3
    ([-12, -11, -1], [-1, -11, -12]),               # Sums: 3, 2, 1
    ([-1, -10, -100], [-1, -10, -100]),             # Sums: 1, 1, 1
    
    # Mixed positive and negative
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # Sums: 1, 2, 1, 2, 3 -> Stable: 1, -1, 11, -11, -12
    ([10, -10, 1, -1], [10, -10, 1, -1]),           # Sums: 1, 1, 1, 1
    
    # Large numbers
    ([999, 1000], [1000, 999]),                     # Sums: 27, 1
    ([12345, 54321], [12345, 54321]),               # Sums: 15, 15
    
    # Zeroes
    ([0, 0, 0], [0, 0, 0]),                         # Sums: 0, 0, 0
    ([0, 1, -1], [0, 1, -1]),                       # Sums: 0, 1, 1
])
def test_order_by_points_parametrized(nums, expected):
    """
    Tests that order_by_points sorts integers by the sum of their digits 
    in ascending order, maintaining stability for identical sums.
    """
    assert order_by_points(nums) == expected

def test_order_by_points_mixed_stability():
    """Explicit test for mixed positive/negative stability and sum sorting."""
    nums = [-5, 5, -10, 10]
    # -10 (sum 1, idx 2), 10 (sum 1, idx 3), -5 (sum 5, idx 0), 5 (sum 5, idx 1)
    assert order_by_points(nums) == [-10, 10, -5, 5]

def test_order_by_points_stability_deep():
    """Deep test for stability with many elements having the same digit sum."""
    nums = [10, 1, 100, 1000, 20, 2, 200, 11]
    # Sum 1: 10, 1, 100, 1000
    # Sum 2: 20, 2, 200, 11
    expected = [10, 1, 100, 1000, 20, 2, 200, 11]
    assert order_by_points(nums) == expected

def test_order_by_points_negative_stability():
    """Test stability specifically for negative numbers with same sums."""
    nums = [-11, -2, -20, -101]
    # All sum to 2
    assert order_by_points(nums) == nums

def test_order_by_points_large_digits():
    """Test with numbers that have many digits."""
    nums = [999999, 1000000, 111111]
    # Sums: 54, 1, 6
    assert order_by_points(nums) == [1000000, 111111, 999999]

def test_order_by_points_different_sums():
    """Test with a variety of different digit sums."""
    nums = [9, 10, 11, 12, 13] 
    # Sums: 9, 1, 2, 3, 4
    # Expected: 10, 11, 12, 13, 9
    assert order_by_points(nums) == [10, 11, 12, 13, 9]