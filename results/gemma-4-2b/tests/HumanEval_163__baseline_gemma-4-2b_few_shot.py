
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1]) == 1

def test_get_max_empty():
    assert get_max([]) is None

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == [2]
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_large_range():
    assert generate_integers(100, 120) == [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120]

def test_generate_integers_single_element():
    assert generate_integers(2, 2) == []
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 3) == []