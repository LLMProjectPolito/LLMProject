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
    if not nums:
        return []

    decorated = [(sum_digits(num), i, num) for i, num in enumerate(nums)]
    decorated.sort()
    return [num for _, _, num in decorated]


class TestOrderByPoints:
    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_positive_numbers(self):
        assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

    def test_negative_numbers(self):
        assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

    def test_mixed_numbers(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_numbers_with_same_digit_sum(self):
        assert order_by_points([12, 21, 3]) == [3, 12, 21]

    def test_numbers_with_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]

    def test_large_numbers(self):
        assert order_by_points([123, 321, 45]) == [45, 123, 321]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 1]) == [1, 1, 1]

    def test_single_number(self):
        assert order_by_points([5]) == [5]

    def test_negative_and_positive_same_digit_sum(self):
        assert order_by_points([-10, 10, 1]) == [-10, 10, 1]

    def test_complex_case(self):
        assert order_by_points([101, 2, 11, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 2, 3, 4, 5, 6, 7, 8, 9, 11, 101]