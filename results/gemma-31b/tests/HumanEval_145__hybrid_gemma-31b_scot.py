
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
    """Ensure that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_single_element():
    """Ensure that a list with a single element returns the same list regardless of value."""
    assert order_by_points([42]) == [42]
    assert order_by_points([-42]) == [-42]
    assert order_by_points([0]) == [0]

def test_basic_sorting():
    """Test standard ascending and descending sort based on digit sums."""
    # Already sorted: Sums 1, 2, 3
    assert order_by_points([1, 11, 111]) == [1, 11, 111]
    # Reverse sorted: Sums 6, 3, 1 -> Expected: 1, 3, 6
    assert order_by_points([123, 21, 10]) == [10, 21, 123]

def test_stability():
    """
    Verify that the sort is stable: elements with the same digit sum 
    must maintain their original relative order.
    """
    # All these have a digit sum of 2. Order should be preserved.
    stable_list = [2, 11, 20, 101, -2, -11, -20]
    assert order_by_points(stable_list) == stable_list
    
    # Mix of sums: 10(1), 1(1), 11(2), 2(2)
    # Expected: [10, 1, 11, 2]
    assert order_by_points([10, 1, 11, 2]) == [10, 1, 11, 2]

def test_negative_numbers():
    """Verify that negative numbers are handled by the sum of their absolute digits."""
    # Sums: -1->1, -11->2, -12->3
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]
    # Sums: -12->3, -1->1, -11->2 -> Expected: -1, -11, -12
    assert order_by_points([-12, -1, -11]) == [-1, -11, -12]

def test_zeros():
    """Ensure zeros are handled correctly as the smallest possible digit sum (0)."""
    # Zeros should always come first.
    assert order_by_points([10, 0, 2, 0]) == [0, 0, 10, 2]
    assert order_by_points([10, 0, -1]) == [0, 10, -1]

def test_large_numbers():
    """Ensure functionality with large integers to verify digit summation logic."""
    # Sums: 1000000000 -> 1, 999 -> 27, 123 -> 6
    assert order_by_points([999, 1000000000, 123]) == [1000000000, 123, 999]

@pytest.mark.parametrize("input_list, expected_output", [
    # Stability checks (all elements have same sum)
    ([15, 24, 33], [15, 24, 33]),    # Sum 6
    ([100, 10, 1], [100, 10, 1]),    # Sum 1
    ([10, 100, 1000], [10, 100, 1000]), # Sum 1
    
    # Basic sorting
    ([9, 1, 8, 2], [1, 2, 8, 9]),    # Simple ascending
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), # Simple descending to ascending
    
    # Mixed signs and stability
    # Sums: 1(1), 11(2), -1(1), -11(2), -12(3)
    # Order: Sum 1 [1, -1], Sum 2 [11, -11], Sum 3 [-12]
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]),
    
    # Mixed with zeros
    ([-9, -1, 0], [0, -1, -9]),      # Sums: 9, 1, 0
    ([0, -0], [0, -0]),              # Zero edge case
])
def test_parametrized_scenarios(input_list, expected_output):
    """Run a comprehensive variety of test cases for regression and edge coverage."""
    assert order_by_points(input_list) == expected_output