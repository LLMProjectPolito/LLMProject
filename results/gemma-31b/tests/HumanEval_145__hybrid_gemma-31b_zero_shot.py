
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

def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    For negative numbers, the first digit is treated as negative and the remaining digits 
    are treated as positive (e.g., -123 -> -1 + 2 + 3 = 4).
    If there are several items with the same sum of digits, they are ordered based on their 
    index in the original list (stable sort).
    """
    def get_sum_of_digits(n):
        s = str(n)
        if n >= 0:
            return sum(int(d) for d in s)
        else:
            # For negative numbers: first digit is negative, rest are positive
            digits = s[1:]
            return -int(digits[0]) + sum(int(d) for d in digits[1:])

    # Python's sorted() is stable, preserving original order for ties.
    return sorted(nums, key=get_sum_of_digits)

class TestOrderByPoints:
    """
    Superior test suite merging comprehensive edge cases, stability checks, 
    and specific negative number logic.
    """

    def test_empty_and_single_elements(self):
        """Should handle empty lists and single-element lists correctly."""
        assert order_by_points([]) == []
        assert order_by_points([42]) == [42]
        assert order_by_points([-42]) == [-42]
        assert order_by_points([0]) == [0]

    def test_basic_positive_sorting(self):
        """Should sort positive numbers by digit sum in ascending order."""
        # Sums: 10(1), 20(2), 11(2), 3(3) -> Stable sort preserves 20 before 11
        assert order_by_points([10, 20, 11, 3]) == [10, 20, 11, 3]
        # Sums: 3(3), 11(2), 20(2), 10(1) -> 10, 11, 20, 3
        assert order_by_points([3, 11, 20, 10]) == [10, 11, 20, 3]

    def test_basic_negative_sorting(self):
        """Should sort negative numbers using the specific first-digit-negative rule."""
        # -1: -1
        # -10: -1 + 0 = -1
        # -11: -1 + 1 = 0
        # -20: -2 + 0 = -2
        # Sorted sums: -2, -1, -1, 0 -> Stable: -20, -1, -10, -11
        assert order_by_points([-1, -10, -11, -20]) == [-20, -1, -10, -11]

    def test_mixed_numbers(self):
        """Should correctly sort a mix of positive, negative, and zero."""
        # 0: 0
        # -5: -5
        # 5: 5
        # -11: 0
        # 11: 2
        # Sorted sums: -5, 0, 0, 2, 5 -> Stable: -5, 0, -11, 11, 5
        assert order_by_points([0, -5, 5, -11, 11]) == [-5, 0, -11, 11, 5]

    def test_stability(self):
        """Verify that the sort is stable (maintains original relative order for ties)."""
        # All these have a sum of 1:
        # 1: 1, 10: 1, 100: 1, -12: (-1+2)=1, -23: (-2+3)=1
        nums = [1, 10, 100, -12, -23]
        assert order_by_points(nums) == nums

    def test_large_integers(self):
        """Should handle very large integers correctly."""
        # 999: 27
        # -999: -9 + 9 + 9 = 9
        # 1000: 1
        # -1000: -1 + 0 + 0 + 0 = -1
        assert order_by_points([999, -999, 1000, -1000]) == [-1000, 1000, -999, 999]

    def test_complex_case(self):
        """Comprehensive test case with mixed signs and overlapping sums."""
        # Input: [1, 11, -1, -11, -12]
        # Sums: 1(1), 11(2), -1(-1), -11(0), -12(1)
        # Sorted sums: -1, 0, 1, 1, 2
        # Expected: [-1, -11, 1, -12, 11]
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    @pytest.mark.parametrize("input_list, expected", [
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([-1, -2, -3], [-3, -2, -1]),
        ([-3, -2, -1], [-3, -2, -1]),
        ([10, -11, 0], [-11, 0, 10]), # sums: 1, 0, 0 -> stable: -11, 0, 10
        ([10, 20, 30], [10, 20, 30]),
        ([30, 20, 10], [10, 20, 30]),
    ])
    def test_parametrized_cases(self, input_list, expected):
        """Run multiple small cases through parametrization."""
        assert order_by_points(input_list) == expected