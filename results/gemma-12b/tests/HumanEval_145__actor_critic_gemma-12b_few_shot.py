
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

    # Store original indices alongside the numbers
    indexed_nums = [(num, i) for i, num in enumerate(nums)]

    # Sort based on digit sum and original index
    sorted_indexed_nums = sorted(indexed_nums, key=lambda x: (sum_digits(x[0]), x[1]))

    # Extract the sorted numbers
    return [num for num, _ in sorted_indexed_nums]


def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_with_empty_string():
    assert order_by_points([0, 1, ""]) == [0, 1, ""]

def test_order_by_points_with_leading_zeros():
    assert order_by_points([01, 02, 1, 2]) == [01, 02, 1, 2]

def test_order_by_points_large_numbers():
    assert order_by_points([1234, 4321, 100]) == [100, 1234, 4321]

def test_order_by_points_very_large_numbers():
    assert order_by_points([2147483647, 1, 10]) == [1, 10, 2147483647]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, 1, 11]) == [-1, -11, 1, 11]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 11, -11]) == [-1, 1, -11, 11]

def test_order_by_points_same_digit_sum():
    assert order_by_points([12, 21, 3]) == [3, 12, 21]