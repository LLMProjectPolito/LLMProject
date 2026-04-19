
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

# The function is provided in the problem description; 
# we are testing the logic described in the docstring.

def test_empty_list():
    """Test that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_single_element():
    """Test that a list with a single element returns the same list."""
    assert order_by_points([10]) == [10]
    assert order_by_points([-5]) == [-5]
    assert order_by_points([0]) == [0]

def test_basic_sorting():
    """Test basic ascending sort based on digit sums."""
    # 1 (sum 1), 2 (sum 2), 10 (sum 1), 11 (sum 2), 12 (sum 3)
    # Sorted by sum: 1, 10, 2, 11, 12
    assert order_by_points([1, 2, 10, 11, 12]) == [1, 10, 2, 11, 12]
    # 100 (sum 1), 20 (sum 2), 11 (sum 2), 3 (sum 3)
    assert order_by_points([100, 20, 11, 3]) == [100, 20, 11, 3]

def test_stability():
    """
    Test that if digit sums are equal, the original index order is preserved.
    """
    # All these have sum = 1
    nums = [1, 10, 100, -1, -10]
    # Since they all have sum 1, the order should remain exactly the same.
    assert order_by_points(nums) == [1, 10, 100, -1, -10]
    
    # Mixed sums: 11 (sum 2), 2 (sum 2), 20 (sum 2)
    nums2 = [11, 2, 20]
    assert order_by_points(nums2) == [11, 2, 20]

def test_negative_numbers():
    """Test that negative numbers are sorted by the sum of their absolute digits."""
    # -1 (sum 1), -11 (sum 2), -12 (sum 3)
    assert order_by_points([-12, -11, -1]) == [-1, -11, -12]
    # -20 (sum 2), -10 (sum 1)
    assert order_by_points([-20, -10]) == [-10, -20]

def test_mixed_signs():
    """Test a mix of positive and negative integers."""
    # 1 (sum 1), 11 (sum 2), -1 (sum 1), -11 (sum 2), -12 (sum 3)
    # Sums: 1, 2, 1, 2, 3
    # Stable sort: [1, -1, 11, -11, -12]
    assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]

def test_zeros():
    """Test that zeros are handled correctly (sum of digits is 0)."""
    # 0 (sum 0), 1 (sum 1), 0 (sum 0)
    # Sorted: 0, 0, 1
    assert order_by_points([0, 1, 0]) == [0, 0, 1]

def test_large_numbers():
    """Test sorting with large integers."""
    # 999 (sum 27), 1000 (sum 1), 55 (sum 10)
    # Sorted: 1000, 55, 999
    assert order_by_points([999, 1000, 55]) == [1000, 55, 999]

def test_already_sorted():
    """Test that a list already sorted by digit sum remains unchanged."""
    # 1 (sum 1), 10 (sum 1), 2 (sum 2), 11 (sum 2)
    nums = [1, 10, 2, 11]
    assert order_by_points(nums) == [1, 10, 2, 11]

def test_reverse_sorted():
    """Test that a list reverse-sorted by digit sum is correctly sorted."""
    # 12 (sum 3), 11 (sum 2), 10 (sum 1)
    assert order_by_points([12, 11, 10]) == [10, 11, 12]