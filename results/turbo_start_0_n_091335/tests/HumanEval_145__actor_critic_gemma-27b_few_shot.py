def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    The function uses abs(n) to calculate the digit sum, meaning that
    -1 and 1 will have the same digit sum.

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

def test_order_by_points_zero():
    assert order_by_points([0, 1, -1]) == [0, -1, 1]

def test_order_by_points_duplicates():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_negative_and_positive():
    assert order_by_points([-1, 1, -10, 10]) == [-1, 1, -10, 10]

def test_order_by_points_large_numbers():
    assert order_by_points([12345, 6789, 100000, 54321]) == [100000, 12345, 54321, 6789]

def test_order_by_points_same_digit_sum():
    # Combined test for same digit sum and original index ordering
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]
    assert order_by_points([-1, 10, -100, 1000]) == [-1, 10, -100, 1000]

def test_order_by_points_large_negative_numbers():
    assert order_by_points([-123456789, 123456789]) == [-123456789, 123456789]