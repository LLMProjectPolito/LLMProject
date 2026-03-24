
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
        return s * (-1 if n < 0 else 1)

    return sorted(nums, key=lambda x: digit_sum(x))

class TestOrderbyPoints:
    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_positive_numbers(self):
        assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_negative_numbers(self):
        assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

    def test_mixed_numbers(self):
        assert order_by_points([1, -2, 3, -4, 5]) == [-2, -4, 1, 3, 5]

    def test_same_digit_sum(self):
        assert order_by_points([1, 11, 2, 20]) == [1, 2, 11, 20]

    def test_single_element(self):
        assert order_by_points([5]) == [5]

    def test_large_numbers(self):
        assert order_by_points([123, 45, 678]) == [45, 123, 678]

    def test_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 2, 2]) == [1, 1, 2, 2]

    def test_negative_with_zero(self):
        assert order_by_points([-1, 0, 1]) == [-1, 0, 1]