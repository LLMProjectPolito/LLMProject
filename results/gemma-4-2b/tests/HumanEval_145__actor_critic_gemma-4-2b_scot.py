
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

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 3]) == [1, 2, 3, 11]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 11, -11, 2, -2]) == [1, -1, 2, -2, -11, 11]

def test_same_digit_sum():
    assert order_by_points([1, 10, 2, 20]) == [1, 2, 10, 20]

def test_single_element():
    assert order_by_points([5]) == [5]

def test_large_numbers():
    assert order_by_points([12345, 67890, 11111]) == [11111, 12345, 67890]

def test_zero():
    assert order_by_points([0, 1, 2]) == [0, 1, 2]

def test_leading_zeros():
    assert order_by_points([10, 100, 1000]) == [10, 100, 1000]

def test_only_negative_numbers():
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

def test_large_number_of_zeros():
    assert order_by_points([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_only_negative_numbers_varying_digit_sums():
    assert order_by_points([-12, -1, -11, -10]) == [-12, -11, -1, -10]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 2, 2, 3]) == [1, 1, 2, 2, 3]