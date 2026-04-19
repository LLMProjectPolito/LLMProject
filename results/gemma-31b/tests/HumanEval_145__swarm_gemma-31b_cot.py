
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

@pytest.mark.parametrize("input_list, expected_output", [
    # Stability, negatives, and zero boundary
    ([10, -10, 1, -1, 0], [-10, -1, 0, 10, 1]),
    # Complex negative digit sum logic and stability
    ([10, -10, 0, -21, 3], [-10, -21, 0, 10, 3]),
    # Negative numbers (first digit negative), zero, and stability
    ([-10, 0, 1, -11, 10], [-10, 0, -11, 1, 10]),
])
def test_order_by_points_stability_and_negatives(input_list, expected_output):
    """
    Tests that order_by_points correctly sorts by the sum of digits,
    handles negative numbers (where the first digit is negative),
    and maintains stability for items with the same digit sum.
    """
    assert order_by_points(input_list) == expected_output