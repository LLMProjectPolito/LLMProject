
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

# The function is assumed to be imported from the source module
# from solution import order_by_points

def test_order_by_points_provided_example():
    """Tests the specific example provided in the docstring."""
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    """Tests that an empty list returns an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Tests a list with a single element."""
    assert order_by_points([42]) == [42]
    assert order_by_points([-42]) == [-42]

def test_order_by_points_stability():
    """
    Tests that the sort is stable. 
    If sums are equal, original relative order must be preserved.
    """
    # 11 (sum 2), 20 (sum 2), 101 (sum 2)
    # All have the same sum, should remain in original order.
    assert order_by_points([11, 20, 101]) == [11, 20, 101]
    
    # -12 (sum 1), 1 (sum 1), 10 (sum 1)
    # All have sum 1, should remain in original order.
    assert order_by_points([-12, 1, 10]) == [-12, 1, 10]
    assert order_by_points([1, 10, -12]) == [1, 10, -12]

def test_order_by_points_negative_logic():
    """
    Deep dive into the negative digit sum logic:
    -10 -> -1 + 0 = -1
    -20 -> -2 + 0 = -2
    -11 -> -1 + 1 = 0
    """
    # Sums: -2, -1, 0
    assert order_by_points([-20, -10, -11]) == [-20, -10, -11]
    # Sums: 0, -1, -2
    assert order_by_points([-11, -10, -20]) == [-20, -10, -11]

def test_order_by_points_large_numbers():
    """Tests numbers with many digits to ensure summation is robust."""
    # 1000 (sum 1), 999 (sum 27)
    assert order_by_points([999, 1000]) == [1000, 999]
    # -1000 (sum -1), -999 (sum -9+9+9 = 9)
    assert order_by_points([-999, -1000]) == [-1000, -999]

def test_order_by_points_zeros():
    """Tests how the function handles zero."""
    # 0 (sum 0), 11 (sum 2), -11 (sum 0)
    # Stability: 0 comes before -11
    assert order_by_points([0, 11, -11]) == [0, -11, 11]

@pytest.mark.parametrize("input_list, expected", [
    ([10, 20, 30], [10, 20, 30]),          # Simple ascending sums (1, 2, 3)
    ([30, 20, 10], [10, 20, 30]),          # Simple descending sums (3, 2, 1)
    ([-1, -2, -3], [-3, -2, -1]),          # Negative sums (-1, -2, -3)
    ([-1, 1, -11, 11], [-1, -11, 1, 11]),  # Mixed: sums -1, 1, 0, 2 -> sorted: -1, 0, 1, 2
])
def test_order_by_points_parametrized(input_list, expected):
    """General test cases for various combinations."""
    assert order_by_points(input_list) == expected