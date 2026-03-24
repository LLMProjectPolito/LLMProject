
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
from your_module import order_by_points  # Replace your_module

@pytest.mark.parametrize("nums, expected", [
    ([], []),  # Test with an empty list
    ([5], [5]),  # Test with a single positive number
    ([1, 2, 3], [1, 2, 3]),  # Test with a sorted list of positive numbers
    ([-1, -2, -3], [-1, -2, -3]),  # Test with a sorted list of negative numbers
    ([1, -2, 3, -4], [1, -2, 3, -4]),  # Test with a mix of positive and negative numbers
    ([11, 2, 1, 10], [1, 2, 11, 10]),  # Test with different digit sums
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),  # Test with a mix of positive and negative numbers and different digit sums
    ([0, 1, -1], [0, 1, -1]),  # Test with zero and positive/negative numbers
    ([123, 45, 6], [6, 45, 123]),  # Test with different digit sums
    ([111, 222, 333], [111, 222, 333]),  # Test with equal digit sums
    ([10, -10, 1, -1], [1, -1, 10, -10]),  # Test with digit sums of 1
    ([10, 1, 100], [1, 10, 100]),  # Test with equal digit sums but different numbers
    ([-1, -10, -100], [-1, -10, -100]),  # Test with only negative numbers and equal digit sums
    ([0, 0, 1, -1], [0, 0, 1, -1]),  # Test with multiple zeroes
    ([123456789, 10], [10, 123456789]),  # Test with large numbers
    ([1, 2, 3], [1, 2, 3]), # Test already sorted list - should not modify
    ([3, 2, 1], [1, 2, 3]), # Test already sorted list - should modify
    ([11, 22, 33], [11, 22, 33]), # Test with duplicate numbers with same digit sum
    ([1, -1], [1, -1]), # Test with numbers that have the same digit sum but different signs
    ([0, 0, 0], [0, 0, 0]), # Test with all zeroes
    ([0, 1], [0, 1]), # Test with zero and a positive number
    ([-1, 0], [0, -1]), # Test with zero and a negative number
])
def test_order_by_points(nums, expected):
    """Test cases for order_by_points function."""
    assert order_by_points(nums) == expected