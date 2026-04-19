
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

@pytest.mark.parametrize("nums, expected", [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([], []),
    ([0], [0]),
    ([5], [5]),
    ([-5], [-5]),
    ([10, 2, 11], [2, 10, 11]),
    ([11, 10, 2], [2, 11, 10]),
    ([-1, -11, -12], [-1, -11, -12]),
    ([-12, -11, -1], [-1, -11, -12]),
    ([0, -1, 1], [-1, 0, 1]),
    ([10, -11], [-11, 10]),
    ([10, -12], [10, -12]),
    ([-12, 10], [-12, 10]),
    ([100, 10, 1], [100, 10, 1]),
    ([1, 10, 100], [1, 10, 100]),
    ([-100, -10, -1], [-100, -10, -1]),
    ([-1, -10, -100], [-1, -10, -100]),
    ([-111, -11, -1], [-1, -11, -111]),
    ([-1, -11, -111], [-1, -11, -111]),
    ([-123, -11, -1], [-1, -11, -123]),
    ([123, 11, 1], [1, 11, 123]),
    ([1, 11, 123], [1, 11, 123]),
    ([10, 20, 30], [10, 20, 30]),
    ([30, 20, 10], [10, 20, 30]),
    ([-10, -20, -30], [-30, -20, -10]),
    ([-30, -20, -10], [-30, -20, -10]),
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected

def test_order_by_points_stability():
    # Test stability specifically: items with same sum should maintain relative order
    # Sums: 10->1, 1->1, 100->1, -12->1, 21->3, 12->3
    nums = [10, 1, 100, -12, 21, 12]
    # Expected: [10, 1, 100, -12, 21, 12]
    assert order_by_points(nums) == [10, 1, 100, -12, 21, 12]

def test_order_by_points_large_numbers():
    # Sums: 999->27, -999->-9+9+9=9, 1000->1, -1000->-1+0+0+0=-1
    nums = [999, -999, 1000, -1000]
    # Sorted sums: -1, 1, 9, 27
    assert order_by_points(nums) == [-1000, 1000, -999, 999]