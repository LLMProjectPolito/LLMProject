
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


def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]

def test_mixed_numbers():
    assert order_by_points([1, -1, 2, -2, 3]) == [-1, -2, 1, 2, 3]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 2, 2, 3]) == [1, 1, 2, 2, 3]

def test_complex_numbers():
    assert order_by_points([11, 22, 33, 44, 55]) == [11, 22, 33, 44, 55]

def test_complex_numbers_with_negative():
    assert order_by_points([-11, -22, -33, -44, -55]) == [-55, -44, -33, -22, -11]

def test_mixed_positive_negative_complex():
    assert order_by_points([1, -1, 11, -11, 121]) == [1, -1, 11, -11, 121]

def test_large_numbers():
    assert order_by_points([100, 101, 102]) == [100, 101, 102]

def test_zero():
    assert order_by_points([0, 1, 2]) == [0, 1, 2]

def test_all_same_sum():
    assert order_by_points([1, 11, 111]) == [1, 11, 111]