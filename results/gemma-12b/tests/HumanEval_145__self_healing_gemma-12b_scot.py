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

    def test_positive_numbers(self):
        assert order_by_points([1, 2, 3]) == [1, 2, 3]

    def test_negative_numbers(self):
        assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

    def test_mixed_numbers(self):
        assert order_by_points([1, -2, 3, -4]) == [1, -2, 3, -4]

    def test_example_1(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_similar_digit_sums(self):
        assert order_by_points([12, 21, 3]) == [3, 12, 21]

    def test_zero(self):
        assert order_by_points([0, 1, -1]) == [0, 1, -1]

    def test_large_numbers(self):
        assert order_by_points([123, 45, 6]) == [6, 45, 123]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 1]) == [1, 1, 1]

    def test_negative_and_positive_with_same_digit_sum(self):
        assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]