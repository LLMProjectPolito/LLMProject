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
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('test') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_whitespace():
    assert is_palindrome('  ') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_negative():
    assert order_by_points([-1, -11, 1, -12, 11]) == [-1, -11, 1, -12, 11]

def test_order_by_points_mixed():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_duplicate_sums():
    assert order_by_points([1, 11, 2, 21]) == [1, 2, 11, 21]

def test_order_by_points_large_numbers():
    assert order_by_points([12, 21, 1, 11]) == [1, 11, 12, 21]

def test_order_by_points_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_order_by_points_negative_zero():
    assert order_by_points([-1, 0, 1]) == [-1, 0, 1]