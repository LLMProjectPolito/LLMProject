import pytest
import math

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

def test_edge_case_empty_list():
    assert order_by_points([]) == []

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_negative_numbers():
    assert order_by_points([-1, -11, -12, 1, 11]) == [-1, -11, -12, 1, 11]

def test_mixed_positive_negative():
    assert order_by_points([-1, 1, -11, 11]) == [-1, -11, 1, 11]

def test_duplicate_sums():
    assert order_by_points([1, 11, 12, 21, 2]) == [1, 2, 11, 12, 21]