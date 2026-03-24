
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

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_mixed_numbers():
    assert order_by_points([1, -11, 2, -22]) == [1, -11, 2, -22]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_same_digit_sum():
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_same_digit_sum_negative():
    assert order_by_points([-10, -1, -100, -1000]) == [-1, -10, -100, -1000]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_large_numbers():
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 12345, 6789]

def test_negative_and_zero():
    assert order_by_points([-1, 0, -10, 1]) == [0, -1, -10, 1]

def test_complex_case():
    assert order_by_points([12, 3, 45, 6, 78, 9]) == [3, 6, 9, 12, 45, 78]

def test_complex_case_negative():
    assert order_by_points([-12, -3, -45, -6, -78, -9]) == [-3, -6, -9, -12, -45, -78]