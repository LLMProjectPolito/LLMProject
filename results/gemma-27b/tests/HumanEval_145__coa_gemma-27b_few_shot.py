
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
import math


# Focus: Digit Sum Calculation
import pytest

def test_digit_sum_calculation_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_digit_sum_calculation_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_digit_sum_calculation_mixed_numbers():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

# Focus: Empty/Null Input
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

def test_null_input():
    with pytest.raises(TypeError):
        order_by_points(None)

# Focus: Tie-breaking with Original Index
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

def test_tie_breaking_original_index_1():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_tie_breaking_original_index_2():
    assert order_by_points([11, 1, 10, 2]) == [1, 2, 10, 11]

def test_tie_breaking_original_index_3():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]