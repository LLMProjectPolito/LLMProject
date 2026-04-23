
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
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

test_cases = [
    ([], []),
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
    ([1, -2, 3, -4, 5], [1, -2, 3, -4, 5]),
    ([12, 11, 10], [10, 11, 12]),
    ([0], [0]),
    ([5, 55, 555], [5, 55, 555]),
    ([123, 45, 6], [6, 45, 123]),
    ([99, 9, 999], [9, 99, 999]),
    ([10, 1, 100], [1, 10, 100]),
    ([11, 2, 3], [2, 3, 11]),
    ([1, 1, 1], [1, 1, 1]),
    ([12, 12, 12], [12, 12, 12]),
    ([12, 1, 12], [1, 12, 12]),
    ([101, 11, 1], [1, 11, 101]),
    ([-10, -1, -100], [-1, -10, -100]),
]

@pytest.mark.parametrize("nums, expected", test_cases)
def test_order_by_points(nums, expected):
    """Tests the order_by_points function with various scenarios."""
    assert order_by_points(nums) == expected