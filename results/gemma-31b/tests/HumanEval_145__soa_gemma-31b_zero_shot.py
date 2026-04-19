
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

def test_order_by_points_basic():
    """Test the function with the provided example cases."""
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test with a single element list."""
    assert order_by_points([10]) == [10]
    assert order_by_points([-10]) == [-10]
    assert order_by_points([0]) == [0]

def test_order_by_points_stability():
    """
    Test that the sort is stable (maintains original order for items with the same sum).
    Sums: 100 -> 1, 10 -> 1, 1 -> 1
    """
    assert order_by_points([100, 10, 1]) == [100, 10, 1]
    assert order_by_points([1, 10, 100]) == [1, 10, 100]

def test_order_by_points_negative_logic():
    """
    Test the specific digit sum logic for negative numbers.
    -20: -2 + 0 = -2
    -10: -1 + 0 = -1
    -11: -1 + 1 = 0
    -12: -1 + 2 = 1
    """
    # Sums: -2, -1, 0, 1
    assert order_by_points([-12, -11, -10, -20]) == [-20, -10, -11, -12]

def test_order_by_points_mixed_signs():
    """Test sorting with a mix of positive and negative integers."""
    # 5: sum 5
    # -5: sum -5
    # 11: sum 2
    # -11: sum 0
    # 0: sum 0
    # Sums: -5, 0, 0, 2, 5
    # Stable order for sum 0: -11 (idx 3), 0 (idx 4)
    nums = [5, 11, -5, -11, 0]
    # Expected: -5 (sum -5), -11 (sum 0), 0 (sum 0), 11 (sum 2), 5 (sum 5)
    assert order_by_points(nums) == [-5, -11, 0, 11, 5]

def test_order_by_points_large_numbers():
    """Test with larger integers to ensure digit summation works."""
    # 123: 1+2+3 = 6
    # 321: 3+2+1 = 6
    # -123: -1+2+3 = 4
    # -321: -3+2+1 = 0
    nums = [123, 321, -123, -321]
    # Sums: 6, 6, 4, 0
    # Sorted: -321 (0), -123 (4), 123 (6), 321 (6)
    assert order_by_points(nums) == [-321, -123, 123, 321]

@pytest.mark.parametrize("input_list, expected_output", [
    ([0, 0, 0], [0, 0, 0]),
    ([10, 20, 30], [10, 20, 30]),
    ([-10, -20, -30], [-30, -20, -10]),
    ([1, -1, 1, -1], [-1, -1, 1, 1]),
])
def test_order_by_points_parametrized(input_list, expected_output):
    """Parametrized tests for various edge cases."""
    assert order_by_points(input_list) == expected_output