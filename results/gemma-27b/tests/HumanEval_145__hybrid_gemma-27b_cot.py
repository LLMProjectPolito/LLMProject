
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

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [1, -1, 2, -2, 3, -3]

def test_same_digit_sum_different_index():
    assert order_by_points([11, 2, 1, 20]) == [1, 2, 11, 20]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_larger_numbers():
    assert order_by_points([123, 45, 6, 789, 10]) == [6, 10, 45, 123, 789]

def test_negative_larger_numbers():
    assert order_by_points([-123, -45, -6, -789, -10]) == [-6, -10, -45, -123, -789]

def test_mixed_larger_numbers():
    assert order_by_points([123, -45, 6, -789, 10]) == [6, 10, -45, 123, -789]

def test_zeroes():
    assert order_by_points([0, 10, 00, 1]) == [0, 00, 1, 10]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_duplicate_numbers_with_different_sums():
    assert order_by_points([11, 2, 11, 2]) == [2, 2, 11, 11]

def test_large_list():
    nums = list(range(100))
    expected = sorted(nums, key=lambda x: sum(int(digit) for digit in str(abs(x))) )
    assert order_by_points(nums) == expected

def test_same_digit_sum_different_index_2():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_large_numbers_2():
    assert order_by_points([1000, 1, 100, 10]) == [1, 10, 100, 1000]

def test_numbers_with_zero_2():
    assert order_by_points([0, 10, 1, 100]) == [0, 1, 10, 100]

def test_negative_numbers_with_large_digit_sum():
    assert order_by_points([-19, -1, -10]) == [-1, -10, -19]

def test_complex_case():
    assert order_by_points([123, 45, 6, 789, 1, -10, -1]) == [-1, -10, 6, 1, 45, 123, 789]

def test_all_same_digit_sum_2():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_large_negative_numbers():
    assert order_by_points([-1000, -1, -100, -10]) == [-1, -10, -100, -1000]