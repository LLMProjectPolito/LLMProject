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

def test_empty_list():
    assert order_by_points([]) == []

def test_basic_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_numbers():
    assert order_by_points([1, -2, 3, -4, 5]) == [1, -2, 3, -4, 5]

def test_same_digit_sum():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_zero():
    assert order_by_points([0, 1, 2]) == [0, 1, 2]

def test_large_numbers():
    assert order_by_points([12345, 6789, 100000]) == [100000, 12345, 6789]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 2, 2]) == [1, 1, 2, 2]

def test_more_complex_case():
    assert order_by_points([23, 1, 4, 12, 5, 3]) == [1, 3, 4, 5, 12, 23]

def test_negative_and_same_digit_sum():
    assert order_by_points([-11, -1, 1, 11]) == [-11, -1, 1, 11]