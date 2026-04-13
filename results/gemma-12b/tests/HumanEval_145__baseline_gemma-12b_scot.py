
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

# STEP 1: REASONING
# The function `order_by_points` sorts a list of integers based on the sum of their digits.
# If two numbers have the same digit sum, their original order is preserved.
# The test suite needs to cover:
# 1. Empty list input.
# 2. List with positive numbers.
# 3. List with negative numbers.
# 4. List with mixed positive and negative numbers.
# 5. Numbers with different digit sums.
# 6. Numbers with the same digit sums (to verify original order preservation).
# 7. Single element list.
# 8. List with zero.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Checks the function's behavior with an empty list.
# - test_positive_numbers: Checks sorting with positive numbers only.
# - test_negative_numbers: Checks sorting with negative numbers only.
# - test_mixed_numbers: Checks sorting with a mix of positive and negative numbers.
# - test_different_digit_sums: Checks sorting with numbers having distinct digit sums.
# - test_same_digit_sums: Checks that original order is preserved when digit sums are equal.
# - test_single_element_list: Checks the function with a single element.
# - test_list_with_zero: Checks the function with zero in the list.

# STEP 3: CODE
import pytest

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
    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


class TestOrderByPoints:
    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_positive_numbers(self):
        assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_negative_numbers(self):
        assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

    def test_mixed_numbers(self):
        assert order_by_points([1, -2, 3, -4, 5]) == [-2, -4, 1, 3, 5]

    def test_different_digit_sums(self):
        assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

    def test_same_digit_sums(self):
        assert order_by_points([1, 11, 2, 22, 3]) == [1, 11, 2, 22, 3]

    def test_single_element_list(self):
        assert order_by_points([5]) == [5]

    def test_list_with_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]

    def test_example_1(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]