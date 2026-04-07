
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

    # Create a list of tuples (index, number)
    indexed_nums = list(enumerate(nums))

    # Sort based on sum of digits and then original index
    sorted_nums = sorted(indexed_nums, key=lambda x: (sum_digits(x[1]), x[0]))

    # Extract the sorted numbers
    return [num for index, num in sorted_nums]


def test_order_by_points_basic():
    """Tests a basic scenario with positive and negative numbers."""
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    """Tests the case where the input list is empty."""
    assert order_by_points([]) == []

def test_order_by_points_duplicates():
    """Tests the case where there are duplicate numbers with different digit sums."""
    assert order_by_points([1, 1, 2]) == [1, 1, 2]

def test_order_by_points_negative_numbers():
    """Tests a scenario with multiple negative numbers and varying digit sums."""
    assert order_by_points([-1, -10, -11, -12]) == [-1, -10, -11, -12]

def test_order_by_points_same_digit_sum():
    """Tests the case where numbers have the same digit sum, verifying original index order."""
    assert order_by_points([10, 1, 11]) == [1, 10, 11]

def test_order_by_points_larger_numbers():
    """Tests the case with larger numbers to ensure digit sum calculation is correct."""
    assert order_by_points([123, 45, 6, 789]) == [6, 45, 123, 789]

def test_order_by_points_with_zero():
    """Tests the case with zero in the input list."""
    assert order_by_points([0, 1, -1]) == [0, 1, -1]

def test_order_by_points_single_element():
    """Tests the case with a single element in the input list."""
    assert order_by_points([5]) == [5]

def test_order_by_points_large_numbers():
    """Tests with very large numbers to check for potential overflow issues in sum_digits."""
    assert order_by_points([123456789, 987654321, 1]) == [1, 123456789, 987654321]

def test_order_by_points_mixed_positive_negative():
    """Tests a mix of positive and negative numbers with varying digit sums."""
    assert order_by_points([5, -5, 15, -15]) == [-5, 5, -15, 15]

def test_order_by_points_duplicates_same_sum():
    """Tests duplicates with the same digit sum to ensure index-based sorting."""
    assert order_by_points([20, 2, 200]) == [2, 20, 200]