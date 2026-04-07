
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

    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_numbers():
    assert order_by_points([1, -2, 3, -4, 5]) == [1, -2, 3, -4, 5]

def test_same_digit_sum():
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_zeroes():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_large_numbers():
    assert order_by_points([12345, 6789, 100000]) == [6789, 12345, 100000]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_more_mixed_numbers():
    assert order_by_points([5, 2, 8, 1, 9, 4]) == [1, 2, 4, 5, 8, 9]

def test_large_numbers_overflow():
    assert order_by_points([2**31 - 1, 2**31 - 2, 1]) == [1, 2**31 - 2, 2**31 - 1]

def test_mixed_positive_negative_zero_duplicates():
    assert order_by_points([1, -1, 0, 1, -1, 0]) == [0, 0, -1, -1, 1, 1]

def test_leading_zeros():
    assert order_by_points([10, 2, 1]) == [1, 2, 10]

def test_only_duplicates():
    assert order_by_points([5, 5, 5]) == [5, 5, 5]