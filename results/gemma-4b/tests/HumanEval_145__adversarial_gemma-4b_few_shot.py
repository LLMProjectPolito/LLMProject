
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

    indexed_nums = list(enumerate(nums))

    indexed_nums.sort(key=lambda x: sum(int(digit) for digit in str(abs(x[1]))), reverse=True)

    return [num for _, num in indexed_nums]


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('test') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-1, -2, 3]) == 3

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4
    assert get_max([1, -2, 3, -4]) == 3

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_negative():
    assert order_by_points([-1, 11, -11, 1]) == [-1, -11, 1, 11]

def test_order_by_points_mixed():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([12, 21, 3, 11]) == [3, 11, 12, 21]
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]
    assert order_by_points([1000, 100, 10, 1]) == [1, 10, 100, 1000]
    assert order_by_points([1, 11, 2, 21]) == [1, 2, 11, 21]
    assert order_by_points([1, 11, 2, 21, 11]) == [1, 2, 11, 11, 21]