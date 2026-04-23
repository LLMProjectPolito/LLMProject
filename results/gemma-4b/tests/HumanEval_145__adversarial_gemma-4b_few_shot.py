
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
    s = ''.join(filter(str.isalnum, s)).lower()
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
    if not nums:
        return []

    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('') == True


def test_is_palindrome_edge_cases():
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('aba') == True
    assert is_palindrome('abcba') == True
    assert is_palindrome('abc') == False


def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-3, -2, -1]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4
    assert get_max([1, -2, 3, -4]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_negative():
    assert order_by_points([-1, -11, 1, -12, 11]) == [-1, -11, 1, -12, 11]

def test_order_by_points_mixed():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_duplicates():
    assert order_by_points([1, 11, -1, -11, 11]) == [-1, -11, 1, 11, 11]

def test_order_by_points_complex():
    assert order_by_points([12, 21, 3, 1, 11, 121]) == [3, 1, 11, 12, 21, 121]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 1, 12, 1234]) == [1, 45, 12, 123, 1234]

def test_order_by_points_zero():
    assert order_by_points([0, 1, 10, 100]) == [0, 1, 10, 100]