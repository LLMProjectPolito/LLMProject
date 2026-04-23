
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

def test_order_by_points_empty():
    """Test that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test that a list with one element returns the same list."""
    assert order_by_points([42]) == [42]

def test_order_by_points_stability():
    """
    Test that if digit sums are equal, the original order is preserved.
    Sums: 11 -> 2, 2 -> 2, 20 -> 2, 101 -> 2
    Original order: 11, 2, 20, 101
    """
    input_list = [11, 2, 20, 101]
    assert order_by_points(input_list) == [11, 2, 20, 101]

def test_order_by_points_negatives():
    """
    Test that negative numbers are sorted by the sum of their absolute digits.
    -12 (sum 3), -1 (sum 1), -11 (sum 2)
    Expected: [-1, -11, -12]
    """
    input_list = [-12, -1, -11]
    assert order_by_points(input_list) == [-1, -11, -12]

def test_order_by_points_zero():
    """Test that zero is handled correctly (sum of digits is 0)."""
    assert order_by_points([10, 0, 1]) == [0, 1, 10]

def test_order_by_points_mixed_complex():
    """
    Test a complex mix of positive and negative integers.
    Input: [1, 11, -1, -11, -12]
    Sums:
    1  -> 1 (idx 0)
    11 -> 2 (idx 1)
    -1 -> 1 (idx 2)
    -11 -> 2 (idx 3)
    -12 -> 3 (idx 4)
    
    Sorted by sum (ascending) and then index (stable):
    Sum 1: 1 (idx 0), -1 (idx 2)
    Sum 2: 11 (idx 1), -11 (idx 3)
    Sum 3: -12 (idx 4)
    Result: [1, -1, 11, -11, -12]
    """
    input_list = [1, 11, -1, -11, -12]
    expected = [1, -1, 11, -11, -12]
    assert order_by_points(input_list) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([100, 10, 1], [1, 10, 100]),  # All sum to 1, check stability
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), # Simple ascending
    ([12, 21, 3], [3, 12, 21]), # Sums: 3, 3, 3. Check stability.
])
def test_order_by_points_parametrized(input_list, expected):
    """Parametrized tests for various scenarios."""
    assert order_by_points(input_list) == expected