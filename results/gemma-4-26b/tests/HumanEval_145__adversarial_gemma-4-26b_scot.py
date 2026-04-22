
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

def test_empty_list():
    """Ensures an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_single_element():
    """Ensures a single element list returns the same list."""
    assert order_by_points([5]) == [5]
    assert order_by_points([-7]) == [-7]

def test_ascending_digit_sum():
    """Tests basic ascending sort by digit sum."""
    # Sums: 1, 2, 3
    assert order_by_points([1, 11, 111]) == [1, 11, 111]
    # Sums: 3, 2, 1
    assert order_by_points([111, 11, 1]) == [1, 11, 111]

def test_stability_tie_breaker():
    """
    Crucial: Tests that if digit sums are equal, 
    the original index order is preserved.
    """
    # All have sum 1. Original order: 10, 1, 100
    assert order_by_points([10, 1, 100]) == [10, 1, 100]
    # All have sum 2. Original order: 11, 2, 20, 200
    assert order_by_points([11, 2, 20, 200]) == [11, 2, 20, 200]

def test_negative_numbers():
    """
    Tests that negative numbers are handled. 
    Standard interpretation: sum of digits of -12 is 1+2=3.
    """
    # Sums: -1 -> 1, -11 -> 2, -2 -> 2
    # Sorted by sum: 1, 2, 2. 
    # Tie-breaker for sum 2: -11 (idx 1) comes before -2 (idx 2)
    assert order_by_points([-1, -11, -2]) == [-1, -11, -2]

def test_mixed_integers_requirement():
    """
    Tests the specific logic described in the prompt text:
    'sorts... in ascending order according to the sum of their digits.
    if there are several items with similar sum... order them based on their index'
    """
    # Input: [1, 11, -1, -11, -12]
    # Digit Sums:
    # 1  -> 1 (idx 0)
    # 11 -> 2 (idx 1)
    # -1 -> 1 (idx 2)
    # -11-> 2 (idx 3)
    # -12-> 3 (idx 4)
    #
    # Sorted by (Sum, Index):
    # (1, 0) -> 1
    # (1, 2) -> -1
    # (2, 1) -> 11
    # (2, 3) -> -11
    # (3, 4) -> -12
    expected = [1, -1, 11, -11, -12]
    assert order_by_points([1, 11, -1, -11, -12]) == expected

def test_zero_handling():
    """Tests that zero is handled correctly (sum of digits is 0)."""
    # Sums: 0, 1, 1
    # Indices: 0, 1, 2
    assert order_by_points([0, 1, -1]) == [0, 1, -1]

def test_large_integers():
    """Tests that the function handles large integers correctly."""
    # Sums: 1000000000 -> 1, 1 -> 1, 11 -> 2
    assert order_by_points([11, 1000000000, 1]) == [1000000000, 1, 11]

@pytest.mark.parametrize("input_list, expected", [
    ([10, 20, 30], [10, 20, 30]),  # Sums: 1, 2, 3
    ([30, 20, 10], [10, 20, 30]),  # Sums: 3, 2, 1
    ([1, 1, 1], [1, 1, 1]),        # All same
    ([12, 21, 30], [12, 21, 30]),  # Sums: 3, 3, 3 (stable)
    ([40, 13, 22], [40, 13, 22]),  # Sums: 4, 4, 4 (stable)
])
def test_parameterized_scenarios(input_list, expected):
    """Comprehensive parameterized testing for various integer combinations."""
    assert order_by_points(input_list) == expected