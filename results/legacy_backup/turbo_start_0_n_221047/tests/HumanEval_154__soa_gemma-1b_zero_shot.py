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
        a, b = b, a

    for i in range(1, len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("a", "") == False
    assert cycpattern_check("", "a") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("b", "a") == False
    assert cycpattern_check("a", "c") == False

def test_cycpattern_check_different_lengths():
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abc", "bc") == False
    assert cycpattern_check("abc", "c") == False
    assert cycpattern_check("abc", "ab") == False