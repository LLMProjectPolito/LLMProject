
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
    def digit_sum(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(enumerate(nums), key=lambda x: (digit_sum(x[1]), x[0]))


def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_mixed_numbers():
    assert order_by_points([1, -11, 2, -22]) == [1, -11, 2, -22]

def test_same_digit_sum():
    assert order_by_points([1, 10, 19, 28]) == [1, 10, 19, 28]
    assert order_by_points([11, 2, 20]) == [2, 11, 20]

def test_zero():
    assert order_by_points([0, 1, -1]) == [0, 1, -1]
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_large_numbers():
    assert order_by_points([1234, 567, 89]) == [89, 567, 1234]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_large_digit_sums():
    assert order_by_points([9999, 1, 2]) == [1, 2, 9999]

def test_same_digit_sum_original_order():
    assert order_by_points([10, 1, 19]) == [1, 10, 19]

def test_duplicate_digit_sums():
    assert order_by_points([11, 1, 10]) == [1, 10, 11]

def test_very_large_numbers():
    assert order_by_points([1234567890, 987654321, 1111111111]) == [987654321, 1111111111, 1234567890]