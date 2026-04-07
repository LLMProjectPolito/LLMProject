
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
    If there are duplicate numbers, their original order is preserved.

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

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 11, -11, -12]) == [-1, 1, -11, 11, -12]

def test_same_digit_sum():
    assert order_by_points([10, 1, 19]) == [1, 10, 19]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_large_numbers():
    assert order_by_points([1000, 10, 1]) == [1, 10, 1000]

def test_all_same_digit_sum():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_large_negative_numbers():
    assert order_by_points([-1000, -10, -1]) == [-1, -10, -1000]

def test_large_numbers_overflow():
    assert order_by_points([9999999999, 1, 2]) == [1, 2, 9999999999]

def test_large_list():
    nums = list(range(100))
    expected = sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x))), nums.index(x)))
    assert order_by_points(nums) == expected

def test_large_list_with_duplicates():
    nums = [1, 1, 2, 2, 11, 11, 12, 12, 21, 21]
    expected = sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x))), nums.index(x)))
    assert order_by_points(nums) == expected