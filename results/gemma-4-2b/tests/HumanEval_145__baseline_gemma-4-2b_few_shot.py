
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 2]) == 9
    assert get_max([10, 2, 5]) == 10

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-10, -2, -5]) == -2

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_positive():
    assert order_by_points([1, 11, 2, 3]) == [1, 2, 3, 11]
    assert order_by_points([1, 11, 2, 3, 12]) == [1, 2, 3, 11, 12]

def test_order_by_points_negative():
    assert order_by_points([-1, -11, 1, 11]) == [-1, -11, 1, 11]
    assert order_by_points([-1, -11, 1, 11, -12]) == [-1, -11, 1, 11, -12]

def test_order_by_points_mixed():
    assert order_by_points([1, -1, 11, -11, 2, -2]) == [1, -1, 2, -2, 11, -11]
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([10, -10, 1, -1]) == [1, -1, 10, -10]