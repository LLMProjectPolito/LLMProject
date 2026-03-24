
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
    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return [x[1] for x in sorted(enumerate(nums), key=lambda x: (sum_digits(x[1]), x[0]))]

import pytest

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_all_same_sum():
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_all_negative():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_large_numbers():
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 6789, 12345]

def test_order_by_points_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_order_by_points_complex():
    assert order_by_points([21, 12, 3, 1, 2, 10, 11]) == [1, 2, 3, 10, 11, 12, 21]

def test_order_by_points_duplicate_same_sum():
    assert order_by_points([1, 10, 1, 10]) == [1, 1, 10, 10]

def test_order_by_points_large_number_limit():
    assert order_by_points([999999999, 1, 2]) == [1, 2, 999999999]

def test_order_by_points_all_negative_same_sum():
    assert order_by_points([-1, -10, -100, -1000]) == [-1, -10, -100, -1000]