
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
    """Tests that an empty list returns an empty list."""
    assert order_by_points([]) == []

@pytest.mark.parametrize("input_list, expected", [
    ([5], [5]),
    ([-5], [-5]),
])
def test_order_by_points_single_element(input_list, expected):
    """Tests that a list with one element returns the same list."""
    assert order_by_points(input_list) == expected

def test_order_by_points_basic_sorting():
    """Tests basic ascending order based on the sum of digits."""
    # 10 (sum 1), 2 (sum 2), 11 (sum 2)
    assert order_by_points([10, 2, 11]) == [10, 2, 11]

@pytest.mark.parametrize("input_list, expected", [
    ([1, 10, 100], [1, 10, 100]),
    ([2, 11, 20], [2, 11, 20]),
])
def test_order_by_points_stable_sort(input_list, expected):
    """Tests that ties in digit sums are broken by the original index (stable sort)."""
    assert order_by_points(input_list) == expected

def test_order_by_points_duplicates():
    """Tests that duplicate values preserve their original relative order."""
    # All have sum 2: 11 (idx 0), 2 (idx 1), 11 (idx 2)
    assert order_by_points([11, 2, 11]) == [11, 2, 11]

def test_order_by_points_negative_numbers():
    """Tests that negative numbers are handled by the sum of digits of their absolute value."""
    # -1 (sum 1), -11 (sum 2), -2 (sum 2)
    assert order_by_points([-1, -11, -2]) == [-1, -11, -2]

def test_order_by_points_mixed_numbers():
    """Tests a mix of positive, negative, and zero."""
    # Sums: 1:1, 11:2, -1:1, -11:2, -12:3, 0:0
    input_list = [1, 11, -1, -11, -12, 0]
    expected = [0, 1, -1, 11, -11, -12]
    assert order_by_points(input_list) == expected

def test_order_by_points_large_numbers():
    """Tests with larger integers."""
    # 999 (sum 27), 1000 (sum 1), 100 (sum 1)
    assert order_by_points([999, 1000, 100]) == [1000, 100, 999]

def test_order_by_points_requirement_logic():
    """Tests the logic described in the requirements: sum of digits, then original index."""
    # Input: [1, 11, -1, -11, -12]
    # Sums: 1:1, 11:2, -1:1, -11:2, -12:3
    # Sorted by sum (1, 1, 2, 2, 3) and index: [1, -1, 11, -11, -12]
    assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]

@pytest.mark.parametrize("invalid_input", [None, "string", 1.5])
def test_order_by_points_invalid_types(invalid_input):
    """Tests that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        order_by_points(invalid_input)