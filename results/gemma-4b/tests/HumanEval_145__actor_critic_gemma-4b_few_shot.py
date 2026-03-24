
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
    if not nums:
        return []

    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))
import pytest

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single():
    assert order_by_points([5]) == [5]

def test_order_by_points_duplicates():
    assert order_by_points([1, 11, 1, 11]) == [1, 1, 11, 11]

def test_order_by_points_negative():
    assert order_by_points([-1, -11, -1, -11]) == [-1, -1, -11, -11]

def test_order_by_points_mixed():
    assert order_by_points([-1, 1, -11, 11]) == [-1, 1, -11, 11]

def test_order_by_points_zero():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 6, 789]) == [6, 45, 123, 789]