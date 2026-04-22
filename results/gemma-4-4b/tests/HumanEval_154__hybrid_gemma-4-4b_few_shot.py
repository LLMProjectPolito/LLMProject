
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

import pytest

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n = len(b)
    if n == 0:
        return True

    b_rotations = [b[i:] + b[:i] for i in range(n)]

    for rotation in b_rotations:
        if rotation in a:
            return True
    return False


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_example1():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_example2():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_example3():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_example4():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_example5():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcdef") == False

def test_cycpattern_check_b_equal_to_a():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_repeated_characters():
    assert cycpattern_check("aaaaa", "aaa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("xyz", "abc") == False

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None