
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

    return sorted(nums, key=lambda i: (sum_digits(nums[i]), i))


import pytest

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_duplicate_numbers_same_digit_sum():
    assert order_by_points([11, 2, 11]) == [2, 11, 11]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, 1, -10, 10]) == [-1, 1, -10, 10]

def test_order_by_points_large_numbers():
    assert order_by_points([12345, 6789, 1000]) == [1000, 12345, 6789]

def test_order_by_points_numbers_with_zero():
    assert order_by_points([10, 20, 1, 2]) == [1, 2, 10, 20]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([5, -5, 10, -10]) == [-5, 5, -10, 10]

def test_order_by_points_all_negative():
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_zero():
    assert order_by_points([0]) == [0]