
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

    return sorted(enumerate(nums), key=lambda x: (sum_digits(x[1]), x[0]))[0].map(lambda item: item[1]) if nums else []

class TestOrderByPoints:

    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_single_element(self):
        assert order_by_points([5]) == [5]

    def test_positive_numbers(self):
        assert order_by_points([1, 11, 2, 22, 3]) == [1, 2, 3, 11, 22]

    def test_negative_numbers(self):
        assert order_by_points([-1, -11, -2, -22, -3]) == [-3, -2, -1, -11, -22]

    def test_mixed_positive_negative(self):
        assert order_by_points([1, -1, 11, -11, 2, -2]) == [1, -1, 2, -2, 11, -11]

    def test_same_digit_sum(self):
        assert order_by_points([10, 19, 28, 37]) == [10, 19, 28, 37]

    def test_same_digit_sum_with_index_ordering(self):
        assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

    def test_large_numbers(self):
        assert order_by_points([123, 45, 6, 789]) == [6, 45, 123, 789]
    
    def test_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]
    
    def test_all_zeros(self):
        assert order_by_points([0, 0, 0]) == [0, 0, 0]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 2, 2]) == [1, 1, 2, 2]

    def test_negative_numbers_with_same_digit_sum(self):
        assert order_by_points([-10, -1, -11]) == [-10, -1, -11]