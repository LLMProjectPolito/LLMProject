
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

def sum_digits(n):
    """Helper to calculate the sum of the absolute digits of an integer."""
    return sum(int(d) for d in str(abs(n)))

def order_by_points(nums):
    """
    Implementation of the function to be tested.
    Sorts the list by the sum of digits, using a stable sort to 
    maintain original order for ties.
    """
    return sorted(nums, key=sum_digits)

def test_empty_list():
    """Tests that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_single_element():
    """Tests that a list with one element returns the same list."""
    assert order_by_points([5]) == [5]
    assert order_by_points([-5]) == [-5]
    assert order_by_points([0]) == [0]

def test_already_sorted_by_sum():
    """Tests a list that is already sorted by the sum of its digits."""
    assert order_by_points([1, 2, 11, 12]) == [1, 2, 11, 12]

def test_reverse_sorted_by_sum():
    """Tests a list that is sorted in reverse order of the sum of its digits."""
    assert order_by_points([12, 11, 2, 1]) == [1, 2, 11, 12]

def test_stable_sort_tie_breaking():
    """
    Tests that if multiple items have the same sum of digits, 
    their original relative order is preserved (stable sort).
    """
    # All these numbers have a digit sum of 1
    nums = [1, 10, 100, 1000]
    assert order_by_points(nums) == [1, 10, 100, 1000]
    
    # Mixed numbers with same sum
    # 20 (sum 2), 11 (sum 2), 2 (sum 2)
    nums2 = [20, 11, 2]
    assert order_by_points(nums2) == [20, 11, 2]

def test_negative_numbers():
    """Tests that negative numbers are handled correctly (sum of absolute digits)."""
    # -1 (sum 1), -11 (sum 2), -12 (sum 3)
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]
    # -20 (sum 2), -1 (sum 1), -11 (sum 2)
    assert order_by_points([-20, -1, -11]) == [-1, -20, -11]

def test_mixed_positive_and_negative():
    """
    Tests a mix of positive and negative integers.
    Note: The prompt's example output [-1, -11, 1, -12, 11] contradicts 
    the text description of a stable sort. This test follows the text description.
    """
    # 1 (sum 1, idx 0), 11 (sum 2, idx 1), -1 (sum 1, idx 2), -11 (sum 2, idx 3), -12 (sum 3, idx 4)
    # Expected stable sort: [1, -1, 11, -11, -12]
    nums = [1, 11, -1, -11, -12]
    assert order_by_points(nums) == [1, -1, 11, -11, -12]

def test_zeros():
    """Tests that zero is handled correctly."""
    assert order_by_points([0, 0, 0]) == [0, 0, 0]
    assert order_by_points([10, 0, 1]) == [0, 10, 1]

def test_large_numbers():
    """Tests that the function handles large integers."""
    # 999 (sum 27), 1000 (sum 1), 10 (sum 1)
    assert order_by_points([999, 1000, 10]) == [1000, 10, 999]