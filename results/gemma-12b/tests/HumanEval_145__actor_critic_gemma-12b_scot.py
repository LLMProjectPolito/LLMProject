
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

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))

class TestOrderByPoints:
    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_mixed_numbers(self):
        assert order_by_points([1, -2, 3, -4, 5]) == [-2, -4, 1, 3, 5]

    def test_duplicate_digit_sums(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]

    def test_large_numbers(self):
        assert order_by_points([123, 45, 6, 789]) == [6, 45, 123, 789]

    def test_all_same_digit_sum(self):
        assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

    def test_same_digit_sum_different_signs(self):
        assert order_by_points([1, -1]) == [1, -1]

    def test_negative_numbers_only(self):
        assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

    def test_large_numbers_overflow(self):
        assert order_by_points([1234567890, 987654321, -1234567890]) == [-1234567890, 987654321, 1234567890]