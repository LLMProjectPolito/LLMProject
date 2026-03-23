import pytest
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
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

    def digit_sum(n):
        s = 0
        for digit in str(n):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))

def order_by_points(nums: List[int]) -> List[int]:
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

    def digit_sum(n):
        s = 0
        for digit in str(n):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))

def test_order_by_points():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
    assert order_by_points([-1, -11, 1, 11]) == [-1, -11, 1, 11]
    assert order_by_points([10, 20, 30]) == [10, 20, 30]
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert order_by_points([11, 2, 12]) == [2, 11, 12]
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    print("All tests passed")