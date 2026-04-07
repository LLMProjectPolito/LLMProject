
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
        for digit in str(abs(n)):
            s += int(digit)
        return s

    indexed_nums = list(enumerate(nums))  # Store original indices
    return [num for _, num in sorted(indexed_nums, key=lambda item: (sum_digits(item[1]), item[0]))]

def test_empty_list():
    assert order_by_points([]) == []

def test_example_1():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_similar_digit_sums():
    assert order_by_points([12, 21, 3]) == [3, 12, 21]

def test_large_numbers():
    assert order_by_points([123, 321, 111]) == [111, 123, 321]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1]) == [1, 1, 1]

def test_negative_and_positive_with_same_digit_sum():
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_complex_numbers():
    assert order_by_points([11, 2, 1, 10, -1]) == [-1, 1, 2, 10, 11]

def test_edge_case_duplicate_same_digit_sum():
    assert order_by_points([1, 1, 2]) == [1, 1, 2]

def test_large_number_edge_case():
    assert order_by_points([12345, 54321, 11111]) == [11111, 12345, 54321]

def test_diverse_numbers():
    assert order_by_points([-5, 10, 2, -1, 100, -20]) == [-20, -5, -1, 2, 10, 100]

def test_zero():
    assert order_by_points([0, 1, -1]) == [0, -1, 1]

def test_single_element_list():
    assert order_by_points([5]) == [5]

def test_all_negative_numbers():
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

def test_duplicate_numbers_with_different_digit_sums():
    assert order_by_points([1, 10, 100]) == [1, 10, 100]