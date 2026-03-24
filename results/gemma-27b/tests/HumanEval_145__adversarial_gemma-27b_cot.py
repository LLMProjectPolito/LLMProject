
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

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [1, -1, 2, -2, 3, -3]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_same_digit_sum_different_index():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_large_numbers():
    assert order_by_points([1000, 1, 100, 10]) == [1, 10, 100, 1000]

def test_numbers_with_zero():
    assert order_by_points([0, 10, 1, 100]) == [0, 1, 10, 100]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_negative_numbers_with_large_digit_sum():
    assert order_by_points([-123, -10, -1]) == [-1, -10, -123]

def test_mixed_large_and_small():
    assert order_by_points([1234, 1, -10, 0]) == [0, 1, -10, 1234]

def test_all_same_digit_sum():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]