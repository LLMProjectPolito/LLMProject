
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

@pytest.mark.parametrize("nums, expected", [
    # All these numbers have a digit sum of 1.
    # The function should maintain their original relative order (stable sort).
    ([100, -10, 1, -1, 10], [100, -10, 1, -1, 10]),
    # Tests stability and handling of zero/negatives (Sum 0 comes first, others sum to 1)
    ([10, -10, 1, -1, 0], [0, 10, -10, 1, -1]),
    # Tests stability (original index) for identical sums, including zero and negative integers
    # Sums: -12(3), -3(3), 12(3), 3(3), 0(0)
    ([-12, -3, 12, 3, 0], [0, -12, -3, 12, 3]),
])
def test_order_by_points_stability_and_negatives(nums, expected):
    assert order_by_points(nums) == expected