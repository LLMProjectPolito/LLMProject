
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

    return sorted(nums, key=lambda x: sum_digits(x))

def test_empty_list():
    assert order_by_points([]) == []

def test_positive_integers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_integers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_integers():
    assert order_by_points([-1, 1, -2, 2]) == [-1, 1, -2, 2]

def test_same_digit_sum():
    assert order_by_points([1, 11, 2, 22]) == [1, 11, 2, 22]

def test_with_zero():
    assert order_by_points([0, 1, 2, 3]) == [0, 1, 2, 3]

def test_large_number():
    assert order_by_points([12345, 123, 12, 1]) == [1, 12, 123, 12345]