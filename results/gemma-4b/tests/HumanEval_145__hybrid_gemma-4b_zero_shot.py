
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


def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_positive_numbers():
    assert order_by_points([1, 11, 2, 20, 3]) == [1, 2, 3, 11, 20]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -2, -20, -3]) == [-1, -2, -3, -11, -20]

def test_order_by_points_mixed_numbers():
    assert order_by_points([1, -1, 11, -11, 2, -2, 20, -20, 3, -3]) == [-1, -2, -3, 1, 2, 3, 10, 11, 20, -11, -20]

def test_order_by_points_duplicate_sums():
    assert order_by_points([1, 11, 2, 20, 10]) == [1, 10, 11, 2, 20]

def test_order_by_points_with_zero():
    assert order_by_points([0, 1, 10, 11, 2]) == [0, 1, 2, 10, 11]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 6, 789, 1]) == [1, 6, 45, 123, 789]

def test_order_by_points_negative_and_positive():
    assert order_by_points([-12, 1, -1, 11, 2]) == [-1, -12, 1, 2, 11]

def test_order_by_points_all_same_sum():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_negative_and_zero():
    assert order_by_points([-1, 0, -10, 1]) == [-1, 0, -10, 1]

def test_order_by_points_complex_case():
    assert order_by_points([-12, 1, -11, 10, 2, -2, 20, -20, 3, -3, 11]) == [-1, -2, -3, 1, 2, 3, 10, 11, 20, -11, -20]