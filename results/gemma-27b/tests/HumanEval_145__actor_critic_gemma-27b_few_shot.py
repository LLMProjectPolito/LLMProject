
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
        return sum(int(digit) for digit in str(abs(n)))

    return sorted(enumerate(nums), key=lambda x: (sum_digits(x[1]), x[0]))


### Tests (Pytest):
import pytest

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_duplicates():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_negative_and_positive():
    assert order_by_points([-1, 1, -10, 10]) == [-1, 1, -10, 10]

def test_order_by_points_large_numbers():
    assert order_by_points([12345, 6789, 100000, 54321]) == [100000, 12345, 54321, 6789]

def test_order_by_points_very_large_numbers():
    assert order_by_points([10**10, 10**11, 10**12]) == [10**10, 10**11, 10**12]

def test_order_by_points_mixed_signs_same_digit_sum():
    assert order_by_points([-1, 10, -100, 1000]) == [-1, 10, -100, 1000]

def test_order_by_points_diverse_numbers():
    assert order_by_points([5, 12, -3, 21, 1, -15, 8]) == [-3, 1, 5, 8, 12, 21, -15]