
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

# The function order_by_points is already defined in the environment.
# We are writing the test suite for it.

class TestOrderByPoints:
    """
    Comprehensive test suite for order_by_points function.
    The function sorts integers by the sum of their digits (abs value) 
    and maintains original order for ties (stable sort).
    """

    def test_empty_list(self):
        """Should return an empty list when input is empty."""
        assert order_by_points([]) == []

    def test_single_element(self):
        """Should return the same list when it contains only one element."""
        assert order_by_points([10]) == [10]
        assert order_by_points([-5]) == [-5]
        assert order_by_points([0]) == [0]

    def test_basic_sorting(self):
        """Should sort numbers by the sum of their digits in ascending order."""
        # Sums: 1(1), 2(2), 3(3)
        assert order_by_points([1, 2, 3]) == [1, 2, 3]
        # Sums: 3(3), 2(2), 1(1)
        assert order_by_points([3, 2, 1]) == [1, 2, 3]
        # Sums: 10(1), 20(2), 30(3)
        assert order_by_points([30, 10, 20]) == [10, 20, 30]

    def test_stability_positive(self):
        """Should maintain original order for positive numbers with the same digit sum."""
        # 10 (sum 1), 1 (sum 1), 100 (sum 1)
        # Original order: 10, 1, 100
        assert order_by_points([10, 1, 100]) == [10, 1, 100]
        # Original order: 1, 10, 100
        assert order_by_points([1, 10, 100]) == [1, 10, 100]

    def test_stability_negative(self):
        """Should maintain original order for negative numbers with the same digit sum."""
        # -11 (sum 2), -2 (sum 2), -20 (sum 2)
        assert order_by_points([-11, -2, -20]) == [-11, -2, -20]

    def test_stability_mixed(self):
        """Should maintain original order for mixed-sign numbers with the same digit sum."""
        # 1 (sum 1), -1 (sum 1), 10 (sum 1), -10 (sum 1)
        assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]
        assert order_by_points([-10, 10, -1, 1]) == [-10, 10, -1, 1]

    def test_negative_digit_sums(self):
        """Should treat negative numbers by the sum of their absolute digits."""
        # -12 (sum 3), -11 (sum 2), -1 (sum 1)
        # Sorted sums: 1, 2, 3 -> Expected: -1, -11, -12
        assert order_by_points([-12, -11, -1]) == [-1, -11, -12]

    def test_large_numbers(self):
        """Should handle large integers correctly."""
        # 999 (sum 27), 1000 (sum 1), 55 (sum 10)
        # Sorted sums: 1, 10, 27 -> Expected: 1000, 55, 999
        assert order_by_points([999, 1000, 55]) == [1000, 55, 999]

    def test_zero_handling(self):
        """Should handle zero correctly as the lowest possible digit sum."""
        # 0 (sum 0), 1 (sum 1), -1 (sum 1)
        assert order_by_points([1, 0, -1]) == [0, 1, -1]

    @pytest.mark.parametrize("input_list, expected_output", [
        ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]),
        ([10, 20, 30, 40], [10, 20, 30, 40]),
        ([40, 30, 20, 10], [10, 20, 30, 40]),
        ([-100, -10, -1], [-100, -10, -1]),
    ])
    def test_parametrized_cases(self, input_list, expected_output):
        """Test various scenarios using parametrization."""
        assert order_by_points(input_list) == expected_output