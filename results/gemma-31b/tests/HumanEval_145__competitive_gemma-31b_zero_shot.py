
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

def test_provided_example():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([42]) == [42]
    assert order_by_points([-42]) == [-42]
    assert order_by_points([0]) == [0]

def test_stable_sort():
    # All have sum of digits = 1
    # 10: 1+0=1, 1: 1, 100: 1+0+0=1
    assert order_by_points([10, 1, 100]) == [10, 1, 100]
    # -1: -1, -10: -1+0=-1, -100: -1+0+0=-1
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_negative_numbers_logic():
    # -1: -1
    # -11: -1 + 1 = 0
    # -21: -2 + 1 = -1
    # -12: -1 + 2 = 1
    # Sorted sums: -1, -1, 0, 1
    # Stable order: -1, -21, -11, -12
    assert order_by_points([-1, -11, -21, -12]) == [-1, -21, -11, -12]

def test_mixed_signs():
    # -10: -1 + 0 = -1
    # 1: 1
    # -1: -1
    # 0: 0
    # Sums: -1, 1, -1, 0
    # Sorted sums: -1, -1, 0, 1
    # Stable order: -10, -1, 0, 1
    assert order_by_points([-10, 1, -1, 0]) == [-10, -1, 0, 1]

def test_large_numbers():
    # 123: 1+2+3 = 6
    # 321: 3+2+1 = 6
    # 111: 1+1+1 = 3
    # 999: 9+9+9 = 27
    assert order_by_points([123, 321, 111, 999]) == [111, 123, 321, 999]

def test_large_negative_numbers():
    # -123: -1+2+3 = 4
    # -321: -3+2+1 = 0
    # -111: -1+1+1 = 1
    # -999: -9+9+9 = 9
    # Sorted sums: 0, 1, 4, 9
    assert order_by_points([-123, -321, -111, -999]) == [-321, -111, -123, -999]

def test_all_positive():
    assert order_by_points([10, 20, 30]) == [10, 20, 30]
    assert order_by_points([30, 20, 10]) == [10, 20, 30]

def test_all_negative():
    # -10: -1, -20: -2, -30: -3
    # Sorted: -30, -20, -10
    assert order_by_points([-10, -20, -30]) == [-30, -20, -10]