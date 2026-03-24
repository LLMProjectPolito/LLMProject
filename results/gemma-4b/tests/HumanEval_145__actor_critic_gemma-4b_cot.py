
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


def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_positive_numbers():
    assert order_by_points([1, 11, 2, 3, 4]) == [1, 2, 3, 4, 11]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -2, -3, -4]) == [-1, -2, -3, -4, -11]

def test_order_by_points_mixed_numbers():
    assert order_by_points([1, -1, 11, -11, 2, -2]) == [-1, -2, 1, -11, 2, 11]

def test_order_by_points_duplicate_sums():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 678, 9]) == [9, 45, 123, 678]

def test_order_by_points_zero_sum():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_order_by_points_negative_zero_sum():
    assert order_by_points([-1, 0, -2]) == [-1, -2, 0]

def test_order_by_points_with_zeros():
    assert order_by_points([10, 20, 30, 1, 2, 3]) == [1, 2, 3, 10, 20, 30]

def test_order_by_points_complex_sums():
    assert order_by_points([12, 21, 3, 101, 11]) == [3, 11, 12, 21, 101]