
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
        n = abs(n)
        while n:
            s += n % 10
            n //= 10
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


class TestOrderByPoints:

    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_single_element(self):
        assert order_by_points([5]) == [5]

    def test_positive_numbers(self):
        assert order_by_points([1, 11, 2, 22, 3]) == [1, 2, 3, 11, 22]

    def test_negative_numbers(self):
        assert order_by_points([-1, -11, -2, -22, -3]) == [-3, -2, -1, -11, -22]

    def test_mixed_positive_and_negative(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_same_digit_sum(self):
        assert order_by_points([10, 19, 28]) == [10, 19, 28]

    def test_zero(self):
        assert order_by_points([0, 1, 2]) == [0, 1, 2]

    def test_large_numbers(self):
        assert order_by_points([12345, 1234, 123]) == [123, 1234, 12345]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 2, 2]) == [1, 1, 2, 2]

    def test_all_negative(self):
        assert order_by_points([-1, -1, -2, -2]) == [-1, -1, -2, -2]

    def test_edge_case_large_negative_number(self):
        assert order_by_points([-1000000]) == [-1000000]

    def test_edge_case_large_positive_number(self):
        assert order_by_points([1000000]) == [1000000]