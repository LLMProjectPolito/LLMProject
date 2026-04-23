
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
    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))

def test_order_by_points():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert order_by_points([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert order_by_points([10, 1, 100, 11]) == [1, 10, 100, 11]
    assert order_by_points([-1, 1, -11, 11]) == [-1, -11, 1, 11]
    assert order_by_points([121, 11, 2, 20]) == [2, 11, 20, 121]
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert order_by_points([-1, -1, -1, -1]) == [-1, -1, -1, -1]
    assert order_by_points([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert order_by_points([1000, 10, 1]) == [1, 10, 1000]
    assert order_by_points([12, 21, 1, 2]) == [1, 2, 12, 21]
    assert order_by_points([-12, 21, -1, 2]) == [-1, -12, 2, 21]