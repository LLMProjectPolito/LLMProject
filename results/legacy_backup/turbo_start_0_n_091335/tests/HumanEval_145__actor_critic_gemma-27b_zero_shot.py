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

    return sorted(enumerate(nums), key=lambda x: (sum_digits(x[1]), x[0]))

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_mixed_signs():
    assert order_by_points([1, -1, 11, -11, -12]) == [-1, 1, -11, 11, -12]

def test_same_digit_sum():
    assert order_by_points([10, 1, 19]) == [1, 10, 19]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_large_numbers():
    assert order_by_points([1000, 10, 1]) == [1, 10, 1000]

def test_all_same_digit_sum():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 11, 11]) == [1, 1, 11, 11]

def test_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_large_negative_numbers():
    assert order_by_points([-1000, -10, -1]) == [-1, -10, -1000]

def test_large_list():
    nums = list(range(-10, 20))
    expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert order_by_points(nums) == expected

def test_potential_overflow():
    assert order_by_points([999999999, 1, 2]) == [1, 2, 999999999]

def test_leading_zeros():
    assert order_by_points([001, 1, 10]) == [001, 1, 10]

def test_duplicate_same_digit_sum():
    assert order_by_points([1, 10, 1, 10]) == [1, 1, 10, 10]