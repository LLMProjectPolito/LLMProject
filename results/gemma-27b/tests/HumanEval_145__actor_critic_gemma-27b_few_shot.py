
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
        s = sum(int(digit) for digit in str(abs(n)))
        return s

    indexed_nums = list(enumerate(nums))  # Store original indices
    return [num for _, num in sorted(indexed_nums, key=lambda x: (sum_digits(x[1]), x[0]))]

import pytest

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_negative_and_positive():
    assert order_by_points([-10, 1, 10, -1]) == [-10, -1, 1, 10]

def test_order_by_points_large_numbers():
    assert order_by_points([12345, 123, 12, 1]) == [1, 12, 123, 12345]

def test_order_by_points_all_same_digit_sum():
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_mixed_signs_same_digit_sum_preserves_order():
    assert order_by_points([-11, 2, -20, 11]) == [-11, 2, 11, -20]

def test_order_by_points_with_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_order_by_points_complex_case():
    assert order_by_points([5, -5, 12, -12, 1, 11, -11, 2, -20, 20]) == [-20, -12, -11, -5, 1, 2, 5, 11, 12, 20]