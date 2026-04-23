
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

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


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_generate_integers_suite1():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == [2]
    assert generate_integers(5, 5) == []
    assert generate_integers(100, 200) == list(range(100, 201, 2))
    assert generate_integers(1, 100) == list(range(2, 101, 2))
    assert generate_integers(200, 100) == list(range(2, 101, 2))
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(1, 3) == [2]
    assert generate_integers(2, 6) == [2, 4, 6]
    assert generate_integers(-2, 2) == [-2, 0, 2]
    assert generate_integers(0, 0) == [0]
    assert generate_integers(0, 2) == [0, 2]
    assert generate_integers(2, 0) == [2, 0]


def test_generate_integers_suite2():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == [2]
    assert generate_integers(5, 5) == []
    assert generate_integers(100, 200) == list(range(100, 201, 2))
    assert generate_integers(1, 100) == list(range(2, 101, 2))
    assert generate_integers(200, 100) == list(range(2, 101, 2))
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(1, 3) == [2]
    assert generate_integers(2, 6) == [2, 4, 6]
    assert generate_integers(-2, 2) == [-2, 0, 2]
    assert generate_integers(0, 0) == [0]
    assert generate_integers(0, 2) == [0, 2]
    assert generate_integers(2, 0) == [2, 0]


def test_palindrome_suite1():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('madam') == True
    assert is_palindrome('racecar') == True

def test_palindrome_suite2():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('madam') == True
    assert is_palindrome('racecar') == True



def test_get_max_suite1():
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) is None
    assert get_max([5, 1, 9, 2]) == 9
    assert get_max([-1, -5, -2]) == -1
    assert get_max([1]) == 1


def test_get_max_suite2():
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) is None
    assert get_max([5, 1, 9, 2]) == 9
    assert get_max([-1, -5, -2]) == -1
    assert get_max([1]) == 1