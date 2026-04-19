
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
    ([10, -10, 1, -1, 0], [-10, -1, 0, 10, 1]),
    ([100, -10, 0, 1, -1], [0, 100, -10, 1, -1]),
    ([10, -10, 0, -1, 1], [-10, -1, 0, 10, 1]),
])
def test_order_by_points(input_list, expected_output):
    """
    Tests the order_by_points function for:
    1. Correct handling of negative numbers (first digit negative, others positive).
    2. Stability (maintaining original index for ties in digit sums).
    3. Interaction between zero, negative, and positive integers.
    """
    assert order_by_points(input_list) == expected_output