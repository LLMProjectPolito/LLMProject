
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

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_one_empty_string():
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_same_strings():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_rotation_valid():
    assert cycpattern_check("abcd", "abd") == True

def test_cycpattern_check_rotation_invalid():
    assert cycpattern_check("abcd", "dcb") == False

def test_cycpattern_check_longer_words():
    assert cycpattern_check("abcdefg", "def") == True

def test_cycpattern_check_complex_case():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abc", "xyz") == False