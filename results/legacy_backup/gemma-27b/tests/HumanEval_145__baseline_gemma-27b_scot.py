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

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_positive_numbers():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_negative_numbers():
    assert order_by_points([-1, -10, -100, -1000]) == [-1, -10, -100, -1000]

def test_mixed_numbers():
    assert order_by_points([1, -10, 100, -1000]) == [1, -10, 100, -1000]

def test_same_digit_sum():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_large_numbers():
    assert order_by_points([12345, 6789, 100000]) == [100000, 12345, 6789]

def test_zeroes():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_single_element():
    assert order_by_points([5]) == [5]