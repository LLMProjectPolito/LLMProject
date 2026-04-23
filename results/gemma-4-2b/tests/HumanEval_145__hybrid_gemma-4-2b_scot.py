
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

    return sorted(nums, key=lambda x: digit_sum(x))


def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 12]) == [1, 2, 11, 12]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -12]) == [-1, -11, -2, -12]

def test_mixed_numbers():
    assert order_by_points([-1, -11, 1, -12, 11]) == [-1, -11, 1, -12, 11]

def test_single_element():
    assert order_by_points([5]) == [5]

def test_duplicate_digits():
    assert order_by_points([11, 22, 33]) == [11, 22, 33]

def test_large_numbers():
    assert order_by_points([12345, 54321, 123]) == [123, 12345, 54321]

def test_leading_zeros():
    assert order_by_points([10, 100, 1000]) == [10, 100, 1000]

def test_negative_and_positive_mixed():
    assert order_by_points([-1, 1, -11, 11]) == [-1, 1, -11, 11]

def test_order_by_points_edge_cases():
    assert order_by_points([]) == []
    assert order_by_points([1]) == [1]
    assert order_by_points([1, 11]) == [1, 11]
    assert order_by_points([1, 11, -1]) == [1, -1, 11]
    assert order_by_points([1, 11, -1, -11]) == [1, -1, 11, -11]
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([10, 1, 11, 12]) == [1, 10, 11, 12]
    assert order_by_points([-1, 1, -10, 10]) == [-1, 1, -10, 10]
    assert order_by_points([1, 11, 1, 111, 1111]) == [1, 1, 11, 111, 1111]
    assert order_by_points([1111, 1, 11, 1]) == [1, 11, 1111, 1]
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert order_by_points([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert order_by_points([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]
    assert order_by_points([-1, -10, -100, -1000]) == [-1, -10, -100, -1000]
    assert order_by_points([0]) == [0]
    assert order_by_points([12, 21, 30, 11]) == [11, 12, 21, 30]
    assert order_by_points([11, 1, 111]) == [1, 11, 111]
    assert order_by_points([1, 11, 111, 1111]) == [1, 11, 111, 1111]
    assert order_by_points([1111, 1, 11, 1]) == [1, 11, 1111, 1]
    assert order_by_points([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    assert order_by_points([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    assert order_by_points([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def test_order_by_points_duplicates():
    assert order_by_points([1, 11, 11, 11]) == [1, 11, 11, 11]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -100, -1000]) == [-1, -10, -100, -1000]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([-1, 1, -10, 10]) == [-1, 1, -10, 10]