
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

@pytest.fixture
def test_order_by_points_empty_list():
    return []

def test_order_by_points_empty_list(test_order_by_points_empty_list):
    assert order_by_points(test_order_by_points_empty_list) == []

def test_order_by_points_positive_numbers(test_order_by_points_empty_list):
    assert order_by_points([1, 11, 2, 22, 3]) == [1, 2, 3, 11, 22]

def test_order_by_points_negative_numbers(test_order_by_points_empty_list):
    assert order_by_points([-1, -11, -2, -22, -3]) == [-3, -2, -1, -11, -22]

def test_order_by_points_mixed_numbers(test_order_by_points_empty_list):
    assert order_by_points([1, -1, 11, -11, 2, -2]) == [-1, 1, -11, 11, -2, 2]

def test_order_by_points_same_digit_sum(test_order_by_points_empty_list):
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_duplicate_numbers(test_order_by_points_empty_list):
    assert order_by_points([1, 1, 2, 2]) == [1, 1, 2, 2]

def test_order_by_points_large_numbers(test_order_by_points_empty_list):
    assert order_by_points([123, 45, 6, 789]) == [6, 45, 123, 789]

def test_order_by_points_zero(test_order_by_points_empty_list):
    assert order_by_points([0, 1, -1, 10]) == [0, -1, 1, 10]

def test_order_by_points_all_negative(test_order_by_points_empty_list):
    assert order_by_points([-10, -1, -100, -1000]) == [-1, -10, -100, -1000]