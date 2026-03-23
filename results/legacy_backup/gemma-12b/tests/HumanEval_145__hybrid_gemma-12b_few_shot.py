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
        assert order_by_points([23, 1, 45, 6, 78, 9]) == [1, 6, 9, 23, 45, 78]

    def test_negative_and_positive_same_digit_sum(self):
        assert order_by_points([-1, 1]) == [-1, 1]

    def test_negative_and_positive_same_digit_sum_different_index(self):
        assert order_by_points([1, -1]) == [1, -1]


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("radar", True),
        ("hello", False),
        ("A man, a plan, a canal: Panama", True),
        ("Racecar", True),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("Madam, I'm Adam", True),
        ("12321", True),
        ("12345", False),
    ]
)
def test_palindrome_basic(s, expected):
    assert is_palindrome(s) == expected


def test_palindrome_empty():
    assert is_palindrome('') == True


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], 3),
        ([-1, -2, -3], -1),
        ([5], 5),
        ([1, 5, 2, 8, 3], 8),
        ([1, 1, 1], 1),
    ]
)
def test_max_positive(arr, expected):
    assert get_max(arr) == expected


def test_max_empty():
    assert get_max([]) is None