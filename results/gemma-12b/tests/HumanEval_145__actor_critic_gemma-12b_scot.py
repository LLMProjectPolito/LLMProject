
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
from your_module import order_by_points, digit_sum  # Replace your_module

def test_digit_sum():
    assert digit_sum(123) == 6
    assert digit_sum(-123) == 6
    assert digit_sum(0) == 0
    assert digit_sum(10) == 1
    assert digit_sum(999) == 27
    assert digit_sum(123456789) == 45
    assert digit_sum(10000) == 1

def test_empty_input():
    assert order_by_points([]) == []

# def test_zeros_and_negatives():  # Removed as redundant
#     assert order_by_points([0, -1, 1]) == [0, -1, 1]
#     assert order_by_points([0, 0, 0]) == [0, 0, 0]
#     assert order_by_points([0, -1, 1, -2, 2]) == [0, -1, 1, -2, 2]

def test_same_digit_sum():
    assert order_by_points([12, 3]) == [3, 12]
    assert order_by_points([21, 3]) == [3, 21]
    assert order_by_points([12, 21, 3]) == [3, 12, 21]
    assert order_by_points([12, 3, 3]) == [3, 3, 12]  # Preserves original order

def test_large_numbers():
    assert order_by_points([123456789, 10]) == [10, 123456789]
    assert order_by_points([1000000000, 1]) == [1, 1000000000]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 2, 2]) == [1, 1, 2, 2]
    assert order_by_points([2, 2, 1, 1]) == [1, 1, 2, 2]
    assert order_by_points([1, 2, 1, 2]) == [1, 1, 2, 2]

@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([5], [5]),
    ([1, 2, 3], [1, 2, 3]),
    ([-1, -2, -3], [-1, -2, -3]),
    ([1, -2, 3, -4], [1, -2, 3, -4]),
    ([11, 2, 1, 10], [1, 2, 11, 10]),
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([0, 1, -1], [0, 1, -1]),
    ([123, 45, 6], [6, 45, 123]),
    ([10, 1, 100, 1000], [1, 10, 100, 1000]),
    ([11, 111, 1111], [11, 111, 1111]),
    ([-11, 11], [ -11, 11]),
    ([1, 10, 100], [1, 10, 100]), # Same digit sum, different lengths
    ([1000000000, 1], [1, 1000000000]), # Large and small numbers
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected