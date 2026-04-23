
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

def digit_sum(n):
    """Calculates the sum of the digits of a number."""
    n = abs(n)  # Handle negative numbers
    s = 0
    for digit in str(n):
        s += int(digit)
    return s

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_mixed_positive_and_negative():
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [1, -1, 2, -2, 3, -3]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_same_digit_sum_order():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_large_numbers():
    assert order_by_points([1000, 1, 100, 10]) == [1, 10, 100, 1000]

def test_numbers_with_zero():
    assert order_by_points([0, 10, 1, 100]) == [0, 1, 10, 100]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_negative_numbers_with_large_digit_sum():
    assert order_by_points([-123, -10, -1]) == [-1, -10, -123]

def test_mixed_large_and_small():
    assert order_by_points([100, 1, -10, -1]) == [-1, 1, -10, 100]

def test_all_zeros():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_same_digit_sum():
    assert order_by_points([19, 28, 37]) == [19, 28, 37]

def test_large_digit_sums():
    assert order_by_points([999, 1]) == [1, 999]

def test_floating_point_numbers():
    assert order_by_points([1.1, 2.2, 3.3]) == [1.1, 2.2, 3.3]

def test_mixed_floats_and_ints():
    assert order_by_points([1, 1.1, 2, 2.2]) == [1, 1.1, 2, 2.2]

def test_negative_and_positive_same_digit_sum():
    assert order_by_points([-10, 1]) == [-10, 1]

def test_larger_negative_numbers():
    assert order_by_points([-99, -1, 10]) == [-1, -99, 10]

def test_non_numeric_input():
    with pytest.raises(TypeError):
        order_by_points([1, "a", 2])

def test_mixed_types():
    with pytest.raises(TypeError):
        order_by_points([1, True, 2.5])