
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

def test_comprehensive_sorting():
    assert order_by_points([1, -1, 2, -2, 0, 10, -10, 11, -11, 100]) == [0, 1, -1, 2, -2, 10, -10, 11, -11, 100]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_duplicates_same_sum():
    assert order_by_points([1, 10, 19]) == [1, 10, 19]

def test_large_numbers():
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 12345, 6789]

def test_negative_and_zero():
    assert order_by_points([-1, 0, -10]) == [-1, 0, -10]

def test_complex_case():
    assert order_by_points([23, 1, -2, 10, -11, 5]) == [-2, 1, 5, 10, 23, -11]

def test_larger_complex_case():
    assert order_by_points([12, 21, 3, 10, -1, -11, 111, 20, -2, -20]) == [-1, -2, -11, -20, 3, 10, 12, 20, 21, 111]

def test_very_large_numbers():
    assert order_by_points([123456789, 987654321, 1, 10]) == [1, 10, 123456789, 987654321]

def test_negative_only():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_large_list():
    large_list = list(range(100))
    expected_list = sorted(large_list, key=lambda x: (sum(int(digit) for digit in str(abs(x))), large_list.index(x)))
    assert order_by_points(large_list) == expected_list