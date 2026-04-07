
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

# Positive and Negative Numbers
def test_positive_and_negative():
    assert order_by_points([1, 2, 3, -1, -2, -3]) == [1, -1, 2, -2, 3, -3]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_zero():
    assert order_by_points([0, 1, -1]) == [0, 1, -1]

def test_multiple_zeros():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_negative_and_zero():
    assert order_by_points([-1, 0, -10]) == [-1, 0, -10]

# Edge Cases
def test_all_negative_numbers():
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

def test_large_negative_numbers():
    assert order_by_points([-1000, -1, -100, -10]) == [-1, -10, -100, -1000]

# Large Numbers
def test_large_numbers():
    assert order_by_points([1000, 1, 100, 10]) == [1, 10, 100, 1000]

def test_very_large_number():
    assert order_by_points([1234567890, 1]) == [1, 1234567890]

# Digit Sum Tiebreaker
def test_digit_sum_tiebreaker():
    assert order_by_points([19, 10]) == [10, 19]
    assert order_by_points([28, 19]) == [19, 28]

def test_digit_sum_tiebreaker_more_cases():
    assert order_by_points([11, 2, 20]) == [2, 11, 20]
    assert order_by_points([10, 1, 19]) == [1, 10, 19]
    assert order_by_points([1, 10, 19, 28]) == [1, 10, 19, 28]

# Mixed Cases
def test_mixed_positive_negative_large_numbers():
    assert order_by_points([123, 45, 6, 789, 1, -10, -1]) == [1, -1, 6, -10, 45, 123, 789]