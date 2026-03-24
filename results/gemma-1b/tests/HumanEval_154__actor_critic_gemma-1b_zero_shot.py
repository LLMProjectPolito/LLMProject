
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
    if len(a) == 0 or len(b) == 0:
        return False

    if len(a) == 1 and len(b) == 1:
        return a.lower() in b.lower()

    if len(a) == 1:
        return b.lower() in a.lower()

    if len(b) == 1:
        return a.lower() in b.lower()

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
    assert cycpattern_check("", "") == False
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("b", "a") == False
    assert cycpattern_check("a", "a") == False

def test_cycpattern_check_different_lengths():
    assert cycpattern_check("abcd", "abc") == True
    assert cycpattern_check("abcd", "ab") == False
    assert cycpattern_check("abcd", "c") == False
    assert cycpattern_check("abcd", "d") == False

def test_cycpattern_check_rotation():
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("hello", "llo") == True
    assert cycpattern_check("hello", "lo") == True
    assert cycpattern_check("hello", "o") == True
    assert cycpattern_check("hello", "el") == True
    assert cycpattern_check("hello", "l") == True
    assert cycpattern_check("hello", "h") == True

def test_cycpattern_check_complex():
    assert cycpattern_check("abcdefg", "cdefg") == True
    assert cycpattern_check("abcdefg", "defg") == True
    assert cycpattern_check("abcdefg", "efg") == True
    assert cycpattern_check("abcdefg", "fgh") == True
    assert cycpattern_check("abcdefg", "gh") == True
    assert cycpattern_check("abcdefg", "g") == True
    assert cycpattern_check("abcdefg", "h") == False
    assert cycpattern_check("abcdefg", "i") == False