
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

    indexed_nums = list(enumerate(nums))
    return [num for _, num in sorted(indexed_nums, key=lambda x: (sum_digits(x[1]), x[0]))]

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 11, -11]) == [-1, 1, -11, 11]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_same_digit_sum():
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_large_numbers():
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 12345, 6789]

def test_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_all_zeros():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_negative_and_zero():
    assert order_by_points([-1, 0, -10]) == [-1, 0, -10]

def test_large_negative_numbers():
    assert order_by_points([-12345, -6789, -10, -1]) == [-1, -10, -12345, -6789]

def test_large_digit_sum():
    assert order_by_points([99999, 1, 9]) == [1, 9, 99999]

def test_max_min_integer():
    assert order_by_points([2**31 - 1, -2**31]) == [-2**31, 2**31 - 1]

def test_complex_tie_breaking():
    assert order_by_points([1, 1, 10, 10]) == [1, 1, 10, 10]

def test_large_list():
    nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
    expected = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    assert order_by_points(nums) == expected