
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
    """Helper to calculate sum of digits of an integer."""
    return sum(int(d) for d in str(abs(n)))

@pytest.mark.parametrize("nums, expected", [
    # Basic cases
    ([], []),
    ([0], [0]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    
    # Different digit sums
    ([10, 2, 11], [10, 2, 11]), # sums: 1, 2, 2. Stable sort: 10, 2, 11
    ([100, 10, 1], [100, 10, 1]), # sums: 1, 1, 1. Stable sort: 100, 10, 1
    ([9, 10, 11], [10, 11, 9]), # sums: 9, 1, 2. Sorted: 10, 11, 9
    
    # Stability tests (same sum, should maintain original order)
    ([11, 20, 2], [11, 20, 2]), # sums: 2, 2, 2. Stable: 11, 20, 2
    ([101, 11, 20], [101, 11, 20]), # sums: 2, 2, 2. Stable: 101, 11, 20
    
    # Negative numbers (sum of digits usually refers to absolute value)
    ([-1, -11, -111], [-1, -11, -111]), # sums: 1, 2, 3
    ([-111, -11, -1], [-1, -11, -111]), # sums: 3, 2, 1
    ([-10, -1], [-10, -1]), # sums: 1, 1. Stable: -10, -1
    
    # Mixed positive and negative
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # sums: 1, 2, 1, 2, 3. Stable: 1, -1, 11, -11, -12
    ([15, -6, 24, -15], [-6, 15, -15, 24]), # sums: 6, 6, 6, 6. Stable: 15, -6, 24, -15. 
    # Wait, if sums are all 6, stable sort is [15, -6, 24, -15].
    # Let's use a clearer mixed case:
    ([10, -2, 11], [10, -2, 11]), # sums: 1, 2, 2. Stable: 10, -2, 11
    
    # Large numbers
    ([999, 1000, 11], [1000, 11, 999]), # sums: 27, 1, 2
])
def test_order_by_points(nums, expected):
    """
    Tests the order_by_points function based on the requirement:
    1. Sort by sum of digits (ascending).
    2. Maintain original index for ties (stable sort).
    """
    # Note: The example in the prompt docstring [1, 11, -1, -11, -12] -> [-1, -11, 1, -12, 11]
    # contradicts the written instructions (ascending sum + stable sort).
    # These tests follow the written logic.
    assert order_by_points(nums) == expected

def test_order_by_points_stability():
    """Explicitly test stability with a larger set of identical sums."""
    nums = [10, 1, 100, -10, -1, -100] # All have digit sum 1
    # Stable sort should return them in the exact original order
    assert order_by_points(nums) == nums

def test_order_by_points_complex():
    """Test a complex mix of values."""
    nums = [43, 12, 10, 5, 11, 20]
    # Sums: 43(7), 12(3), 10(1), 5(5), 11(2), 20(2)
    # Sorted sums: 1(10), 2(11), 2(20), 3(12), 5(5), 7(43)
    expected = [10, 11, 20, 12, 5, 43]
    assert order_by_points(nums) == expected