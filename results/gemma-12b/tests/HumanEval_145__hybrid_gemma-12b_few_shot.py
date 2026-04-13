
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
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def sum_digits(n: int) -> int:
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


class TestOrderByPoints:
    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_basic_example(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_positive_numbers(self):
        assert order_by_points([12, 3, 4, 5]) == [3, 4, 5, 12]

    def test_negative_numbers(self):
        assert order_by_points([-12, -3, -4, -5]) == [-3, -4, -5, -12]

    def test_mixed_numbers(self):
        assert order_by_points([-12, 3, -4, 5]) == [-4, 3, 5, -12]

    def test_same_digit_sum(self):
        assert order_by_points([1, 10, 100]) == [1, 10, 100]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 1]) == [1, 1, 1]

    def test_large_numbers(self):
        assert order_by_points([1234, 567, 89]) == [89, 567, 1234]

    def test_zero(self):
        assert order_by_points([0, 1, -1]) == [0, -1, 1]

    def test_all_zeros(self):
        assert order_by_points([0, 0, 0]) == [0, 0, 0]

    def test_single_element(self):
        assert order_by_points([5]) == [5]

    def test_complex_example(self):
        assert order_by_points([23, 4, 15, 1, 2]) == [1, 2, 4, 15, 23]

    def test_negative_and_positive_same_digit_sum(self):
        assert order_by_points([-1, 1]) == [-1, 1]

    def test_negative_and_positive_same_digit_sum_different_index(self):
        assert order_by_points([1, -1]) == [1, -1]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
        ([], []),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([10, 1, 100, 1000], [1, 10, 100, 1000]),
        ([-10, -1, -100, -1000], [-1, -10, -100, -1000]),
        ([123, 45, 6, 789], [6, 45, 123, 789]),
        ([1, 1, 1, 1], [0, 1, 1, 1]),  # Test for identical numbers
        ([1, 10, 100, 1000, 10000], [1, 10, 100, 1000, 10000]),
        ([-1, -10, -100, -1000], [-1, -10, -100, -1000]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([1, -1, 2, -2], [1, -1, 2, -2]),  # Test with mixed positive and negative
    ],
)
def test_order_by_points_parametrized(nums, expected):
    """Tests the order_by_points function with various inputs."""
    assert order_by_points(nums) == expected

def test_order_by_points_negative_numbers():
    """Tests with only negative numbers."""
    assert order_by_points([-1, -2, -3, -4]) == [-1, -2, -3, -4]

def test_order_by_points_mixed_signs():
    """Tests with a mix of positive and negative numbers."""
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_order_by_points_large_numbers():
    """Tests with larger numbers to ensure digit sum calculation is correct."""
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 12345, 6789]

def test_order_by_points_same_digit_sum_index():
    """Tests cases where numbers have the same digit sum, ensuring original index is preserved."""
    assert order_by_points([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert order_by_points([4, 1, 3, 2]) == [4, 1, 3, 2]

def test_order_by_points_zero_and_positive():
    """Tests with zero and positive numbers."""
    assert order_by_points([0, 1, 2, 3]) == [0, 1, 2, 3]

def test_order_by_points_zero_and_negative():
    """Tests with zero and negative numbers."""
    assert order_by_points([0, -1, -2, -3]) == [0, -1, -2, -3]


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

class TestPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None