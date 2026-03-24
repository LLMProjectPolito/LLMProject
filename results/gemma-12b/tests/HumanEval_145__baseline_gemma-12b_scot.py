
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
# The test suite needs to cover various scenarios:
# - Empty list
# - List with positive numbers
# - List with negative numbers
# - List with mixed positive and negative numbers
# - List with numbers having the same digit sum
# - List with single element
# - List with duplicate numbers

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Checks if the function handles an empty list correctly.
# - test_positive_numbers: Checks sorting with positive numbers.
# - test_negative_numbers: Checks sorting with negative numbers.
# - test_mixed_numbers: Checks sorting with a mix of positive and negative numbers.
# - test_same_digit_sum: Checks sorting when numbers have the same digit sum.
# - test_single_element: Checks sorting with a single element.
# - test_duplicate_numbers: Checks sorting with duplicate numbers.

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

    return sorted(nums, key=lambda x: sum_digits(x))


class TestOrderByPoints:
    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_positive_numbers(self):
        assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_negative_numbers(self):
        assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

    def test_mixed_numbers(self):
        assert order_by_points([1, -2, 3, -4, 5]) == [-2, 1, 3, -4, 5]

    def test_same_digit_sum(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_single_element(self):
        assert order_by_points([5]) == [5]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_complex_case(self):
        assert order_by_points([12, 21, 1, 3, 5, 10, 2]) == [1, 2, 3, 5, 10, 12, 21]

    def test_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]