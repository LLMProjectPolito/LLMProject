
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

def sum_digits(n):
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

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
    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))

class TestOrderByPoints:
    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_positive_numbers(self):
        assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

    def test_negative_numbers(self):
        assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

    def test_mixed_numbers(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_same_digit_sum(self):
        assert order_by_points([12, 21, 3]) == [3, 12, 21]

    def test_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]

    def test_large_numbers(self):
        assert order_by_points([123, 321, 111]) == [111, 123, 321]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 1]) == [1, 1, 1]

    def test_negative_and_positive_same_digit_sum(self):
        assert order_by_points([-1, 1]) == [-1, 1]

    def test_complex_case(self):
        assert order_by_points([10, 2, 1, 20, 3]) == [1, 2, 10, 20, 3]