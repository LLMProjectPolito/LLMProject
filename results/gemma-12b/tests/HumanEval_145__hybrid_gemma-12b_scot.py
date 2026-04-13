
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

@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
    ([1, -2, 3, -4, 5], [1, -2, 3, -4, 5]),
    ([11, 2, 1, 22], [1, 2, 11, 22]),
    ([0], [0]),
    ([123, 45, 6], [6, 45, 123]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([5, 55, 555], [5, 55, 555]),
    ([10, 1, 100], [1, 10, 100]),
    ([101, 11, 1], [1, 11, 101]),
    ([12, 11, 10], [10, 11, 12]),
    ([1, 10, 100, 1000], [1, 10, 100, 1000]),
    ([1, 10, 100, 1000, 1], [1, 10, 100, 1000, 1]),
])
def test_order_by_points_various_scenarios(nums, expected):
    """Tests the order_by_points function with various scenarios."""
    assert order_by_points(nums) == expected

def test_same_digit_sum():
    """Test with numbers having the same digit sum to ensure original order is preserved."""
    nums = [1, 10, 100]
    expected = [1, 10, 100]
    assert order_by_points(nums) == expected

def test_single_element():
    """Test with a list containing only one element."""
    nums = [5]
    expected = [5]
    assert order_by_points(nums) == expected

def test_all_same_digit_sum():
    """Test where all numbers have the same digit sum."""
    nums = [11, 20, 101]
    expected = [11, 20, 101]
    assert order_by_points(nums) == expected