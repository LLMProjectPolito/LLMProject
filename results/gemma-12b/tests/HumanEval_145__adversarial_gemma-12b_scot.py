
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

def digit_sum(n):
    """Helper function to calculate the sum of digits of an integer."""
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    if n < 0:
        return -s
    return s

@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
    ([1, -2, 3, -4, 5], [1, -2, 3, -4, 5]),
    ([12, 11, 2], [2, 11, 12]),
    ([1, 1, 1], [1, 1, 1]),
    ([123, 45, 6], [6, 45, 123]),
    ([0], [0]),
    ([10, 1, 100], [1, 10, 100]),
    ([22, 11, 3], [3, 11, 22]),
    ([1, 10, 100, 1000], [1, 10, 100, 1000]),
    ([-1, -10, -100], [-1, -10, -100]),
    ([1, -1, 10, -10], [1, -1, 10, -10])
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected