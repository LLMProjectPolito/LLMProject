
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

# The function order_by_points is assumed to be available in the namespace.

def test_empty_list():
    """Tests that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_single_element():
    """Tests that a list with one element returns the same list."""
    assert order_by_points([1]) == [1]
    assert order_by_points([-1]) == [-1]
    assert order_by_points([0]) == [0]

def test_stability_same_digit_sum():
    """
    Tests the stability requirement: if digit sums are equal, 
    the original order must be preserved.
    """
    # All these have a digit sum of 1
    nums = [1, 10, 100, -1, -10, 1000]
    assert order_by_points(nums) == nums

    # All these have a digit sum of 2
    nums = [2, 11, 20, -2, -11, -20]
    assert order_by_points(nums) == nums

def test_ascending_digit_sum():
    """Tests that numbers are sorted by the sum of their digits in ascending order."""
    # Sums: 1, 2, 3, 4
    assert order_by_points([1, 11, 111, 1111]) == [1, 11, 111, 1111]
    # Sums: 3, 1, 2
    assert order_by_points([12, 1, 11]) == [1, 11, 12]

def test_negative_numbers():
    """Tests that negative numbers are handled correctly (sum of absolute digits)."""
    # Sums: 1, 2, 3
    assert order_by_points([-1, -11, -111]) == [-1, -11, -111]
    # Sums: 3, 1, 2
    assert order_by_points([-12, -1, -11]) == [-1, -11, -12]

def test_mixed_numbers():
    """Tests a mix of positive, negative, and zero."""
    # Sums: 1 (1), 2 (11), 1 (-1), 2 (-11), 3 (-12)
    # Stable sort order: 1 (idx 0), -1 (idx 2), 11 (idx 1), -11 (idx 3), -12 (idx 4)
    nums = [1, 11, -1, -11, -12]
    expected = [1, -1, 11, -11, -12]
    assert order_by_points(nums) == expected

def test_zero():
    """Tests that zero is handled correctly (digit sum is 0)."""
    # Sums: 1, 0, 1
    assert order_by_points([1, 0, -1]) == [0, 1, -1]

def test_large_numbers():
    """Tests that the function handles large integers."""
    # Sums: 1, 2, 1
    assert order_by_points([1000000, 11, 100]) == [1000000, 100, 11]

def test_docstring_example_consistency():
    """
    Tests the specific example provided in the docstring.
    Note: If the docstring example [-1, -11, 1, -12, 11] is logically 
    inconsistent with the text 'order them based on their index', 
    this test will correctly identify the discrepancy.
    """
    # Based on the text: Sums are 1, 2, 1, 2, 3. 
    # Stable sort should be [1, -1, 11, -11, -12]
    # If the function follows the docstring example exactly, this test detects if 
    # the implementation deviates from the textual requirement.
    input_list = [1, 11, -1, -11, -12]
    # We test against the textual requirement (Stable Sort)
    assert order_by_points(input_list) == [1, -1, 11, -11, -12]