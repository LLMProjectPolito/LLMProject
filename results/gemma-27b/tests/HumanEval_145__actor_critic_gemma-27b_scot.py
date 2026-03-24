
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

    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))


def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_and_negative_numbers():
    assert order_by_points([1, 11, 2, 22, -1, -11, -2, -22]) == [1, 2, -1, -2, 11, 22, -11, -22]

def test_same_digit_sum():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_large_digit_sums():
    assert order_by_points([99999, 1, 999]) == [1, 999, 99999]

def test_mix_large_and_small_same_digit_sum():
    assert order_by_points([19, 10, 100, 1]) == [1, 10, 19, 100]

def test_zeroes():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 11, 11]) == [1, 1, 11, 11]

def test_large_list():
    nums = [i % 20 for i in range(30)]  # Create a list of 30 numbers with varying digit sums and duplicates
    sorted_nums = order_by_points(nums)
    assert len(sorted_nums) == 30

def test_very_large_numbers():
    assert order_by_points([10**10, 1, 10**9]) == [1, 10**9, 10**10]