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

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_numbers():
    assert order_by_points([-1, 1, -2, 2, -3, 3]) == [-1, 1, -2, 2, -3, 3]

def test_duplicate_sums():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_duplicate_sums_with_index():
    assert order_by_points([1, 11, 111, -1, -11, -111]) == [-1, -11, -111, 1, 11, 111]

def test_large_numbers():
    assert order_by_points([123, 45, 6, 789, 1]) == [1, 6, 45, 123, 789]

def test_zero_numbers():
    assert order_by_points([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_mixed_zero_and_positive():
    assert order_by_points([0, 1, 0, 2, 0]) == [0, 0, 0, 1, 2]

def test_negative_zero_and_positive():
    assert order_by_points([-1, 0, 1, -2, 0]) == [-1, 0, 0, 1, -2]

def test_complex_case():
    assert order_by_points([10, 1, 100, 11, 2, 20]) == [1, 2, 10, 11, 20, 100]