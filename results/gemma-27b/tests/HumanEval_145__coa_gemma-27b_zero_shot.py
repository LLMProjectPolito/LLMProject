import pytest
import math


# Focus: Digit Sum Calculation
import pytest

def test_digit_sum_calculation_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_digit_sum_calculation_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_digit_sum_calculation_mixed_numbers():
    assert order_by_points([1, -11, 2, -22, 11]) == [1, -11, 2, -22, 11]

# Focus: Handling of Negative Numbers
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

def test_negative_numbers_basic():
    assert order_by_points([1, -1, -11, 11]) == [-1, -11, 1, 11]

def test_negative_numbers_with_zero():
    assert order_by_points([-1, 0, -11, 11]) == [-1, 0, -11, 11]

def test_negative_numbers_multiple():
    assert order_by_points([-12, -1, -11, 1, 11]) == [-12, -11, -1, 1, 11]

# Focus: Original Index Preservation
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

def test_original_index_preservation_same_sum():
    assert order_by_points([10, 1, 100, 1]) == [1, 10, 1, 100]

def test_original_index_preservation_with_negatives():
    assert order_by_points([10, -1, 100, -1]) == [-1, -1, 10, 100]

def test_original_index_preservation_complex():
    assert order_by_points([12, 21, 3, 13, 2, 1]) == [1, 2, 3, 12, 13, 21]