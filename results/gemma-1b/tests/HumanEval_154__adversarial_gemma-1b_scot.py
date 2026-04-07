
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
    if len(a) < len(b):
        return False

    for i in range(1, len(b) + 1):
        rotated_b = b[i-1:] + b[:i-1]
        if rotated_b in a:
            return True

    return False

def test_cycpattern_check_empty():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_one_word():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abcd", "xyz") == False

def test_cycpattern_check_rotation_match():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_rotation_no_match():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_multiple_rotations():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match_rotation():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_longer_string():
    assert cycpattern_check("abcdefg", "def") == True

def test_cycpattern_check_different_lengths():
    assert cycpattern_check("abc", "abcd") == False