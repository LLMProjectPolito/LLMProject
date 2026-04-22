
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

# The function signature to be tested
# def order_by_points(nums: list[int]) -> list[int]:
#     ...

class TestOrderByPoints:
    """
    Test suite for order_by_points.
    Specification:
    1. Sort by sum of digits (ascending).
    2. Tie-breaker: Original index in the list (ascending).
    """

    def test_empty_list(self):
        """Requirement: Should return an empty list when input is empty."""
        assert order_by_points([]) == []

    def test_single_element(self):
        """Requirement: A single element list should remain unchanged."""
        assert order_by_points([42]) == [42]

    def test_ascending_digit_sum(self):
        """Requirement: Basic ascending order based on digit sums."""
        # Sums: 10->1, 2->2, 11->2, 30->3
        # Expected: [10, 2, 11, 30]
        # Note: 2 and 11 both sum to 2, so 2 comes first due to index.
        input_list = [11, 2, 30, 10]
        expected = [10, 11, 2, 30] 
        # Wait, let's re-calc: 10(1), 11(2), 2(2), 30(3). 
        # Correct order: 10, 11, 2, 30
        assert order_by_points(input_list) == [10, 11, 2, 30]

    def test_stable_sort_tie_breaker(self):
        """
        Requirement: If sums are equal, order by original index.
        This tests the 'stability' of the sort.
        """
        # All these have digit sum of 1
        input_list = [100, 1, 10, 0] 
        # Indices: 100(0), 1(1), 10(2), 0(3)
        # Since all sums are 1, order must be exactly the original order.
        assert order_by_points(input_list) == [100, 1, 10, 0]

    def test_negative_numbers_digit_sum(self):
        """
        Requirement: Handle negative numbers. 
        Standard interpretation: sum of digits of the absolute value.
        """
        # -12 -> sum 3
        # -1  -> sum 1
        # 11  -> sum 2
        # -11 -> sum 2
        input_list = [-12, -1, 11, -11]
        # Sums: -1(1), -11(2), 11(2), -12(3)
        # Tie-breaker for sum 2: -11 (idx 3) vs 11 (idx 2) -> 11 comes first
        expected = [-1, 11, -11, -12]
        assert order_by_points(input_list) == expected

    def test_zeros(self):
        """Requirement: Handle multiple zeros."""
        assert order_by_points([0, 0, 0]) == [0, 0, 0]

    def test_large_numbers(self):
        """Requirement: Handle large integers without overflow or errors."""
        input_list = [1000000, 1]
        # Sums: 1, 1. Index order: 1000000, 1
        assert order_by_points(input_list) == [1000000, 1]

    def test_provided_example_discrepancy(self):
        """
        CRITICAL: This test checks the example provided in the docstring.
        If the implementation follows the TEXT, this test will FAIL.
        If the implementation follows the EXAMPLE, this test will PASS.
        As a QA, I am asserting the TEXTUAL specification is the truth.
        """
        input_list = [1, 11, -1, -11, -12]
        # Calculation based on text:
        # 1: sum 1, idx 0
        # 11: sum 2, idx 1
        # -1: sum 1, idx 2
        # -11: sum 2, idx 3
        # -12: sum 3, idx 4
        # Sorted by (sum, idx): (1,0), (1,2), (2,1), (2,3), (3,4)
        # Result: [1, -1, 11, -11, -12]
        expected = [1, -1, 11, -11, -12]
        assert order_by_points(input_list) == expected

@pytest.mark.parametrize("input_val, expected_val", [
    ([5, 5, 5], [5, 5, 5]),
    ([12, 21, 3], [3, 12, 21]), # Sums: 3, 3, 3 -> index order
    ([9, 10, 1], [10, 1, 9]),   # Sums: 1, 1, 9 -> index order for 10, 1
])
def test_parameterized_edge_cases(input_val, expected_val):
    """Quick check for various small edge cases."""
    assert order_by_points(input_val) == expected_val