
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

@pytest.mark.parametrize("nums, expected", [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([], []),
    ([0], [0]),
    ([42], [42]),
    ([-42], [-42]),
    ([0, 0, 0], [0, 0, 0]),
])
def test_order_by_points_basic_and_edge_cases(nums, expected):
    """Test basic docstring examples and simple edge cases (empty, single, zeros)."""
    assert order_by_points(nums) == expected

def test_order_by_points_all_positive():
    """Test lists containing only positive integers, including stability."""
    # 10 (1), 11 (2), 2 (2), 100 (1) -> Stable sort: 10, 100, 11, 2
    assert order_by_points([10, 11, 2, 100]) == [10, 100, 11, 2]
    # 3 (3), 2 (2), 1 (1) -> Sorted: 1, 2, 3
    assert order_by_points([3, 2, 1]) == [1, 2, 3]

def test_order_by_points_all_negative():
    """
    Test lists containing only negative integers.
    Logic: first digit negative, others positive.
    -1 (-1), -11 (0), -12 (1), -20 (-2) -> Sorted: -20, -1, -11, -12
    """
    assert order_by_points([-1, -11, -12, -20]) == [-20, -1, -11, -12]
    # -111 (-1+1+1=1), -11 (-1+1=0), -1 (-1) -> Sorted: -1, -11, -111
    assert order_by_points([-111, -11, -1]) == [-1, -11, -111]

def test_order_by_points_mixed_signs():
    """Test lists with a mix of positive, negative, and zero."""
    # -1 (-1), 0 (0), 1 (1)
    assert order_by_points([1, 0, -1]) == [-1, 0, 1]
    # 10 (1), -10 (-1), 20 (2), -20 (-2) -> Sorted: -20, -10, 10, 20
    assert order_by_points([10, -10, 20, -20]) == [-20, -10, 10, 20]
    # Complex mix: [10, -1, 0, 11, -11, 2]
    # Sums: [1, -1, 0, 2, 0, 2] -> Sorted: -1, 0, 0, 1, 2, 2
    # Stable order: -1, 0, -11, 10, 11, 2
    assert order_by_points([10, -1, 0, 11, -11, 2]) == [-1, 0, -11, 10, 11, 2]

def test_order_by_points_stability():
    """
    Verify that the sort is stable. If digit sums are equal, 
    the original order must be preserved.
    """
    # All sum to 1: 1, 10, 100, -12 (-1+2=1)
    assert order_by_points([1, 10, 100, -12]) == [1, 10, 100, -12]
    assert order_by_points([-12, 100, 10, 1]) == [-12, 100, 10, 1]
    
    # All sum to -1: -1, -10, -100
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]
    assert order_by_points([-100, -10, -1]) == [-100, -10, -1]
    
    # All sum to 0: 0, -11, -101 (-1+0+1=0)
    assert order_by_points([0, -11, -101]) == [0, -11, -101]
    assert order_by_points([-101, -11, 0]) == [-101, -11, 0]

def test_order_by_points_large_numbers():
    """Test with larger integers to ensure digit summation logic holds."""
    # 12345 (sum 15), -12345 (sum -1+2+3+4+5 = 13), 999 (sum 27), -999 (sum -9+9+9 = 9)
    input_list = [12345, -12345, 999, -999]
    # Expected order by sums: -999 (9), -12345 (13), 12345 (15), 999 (27)
    assert order_by_points(input_list) == [-999, -12345, 12345, 999]

@pytest.mark.parametrize("nums, expected", [
    ([123, 321], [123, 321]),           # sum 6, 6 (stable)
    ([-123, -321], [-321, -123]),       # sum 4, 0 -> sorted 0, 4
    ([9, -9], [-9, 9]),                 # sum 9, -9 -> sorted -9, 9
    ([19, -19], [-19, 19]),             # sum 10, 8 -> sorted 8, 10
    ([-19, 19], [-19, 19]),             # sum 8, 10 -> sorted 8, 10
])
def test_order_by_points_parameterized_cases(nums, expected):
    """Additional specific edge cases and pair comparisons."""
    assert order_by_points(nums) == expected