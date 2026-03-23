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

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element_positive():
    assert order_by_points([5]) == [5]

def test_single_element_negative():
    assert order_by_points([-5]) == [-5]

def test_duplicate_sums_different_indices():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_duplicate_sums_same_indices():
    assert order_by_points([1, 11, -1, -11]) == [1, 11, -1, -11]