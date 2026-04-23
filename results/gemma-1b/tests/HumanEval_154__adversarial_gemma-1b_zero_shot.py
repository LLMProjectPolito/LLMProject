
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
        return a.lower() in b.lower()

    if len(b) == 1:
        return b.lower() in a.lower()

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
    assert cycpattern_check("a", "") == False
    assert cycpattern_check("", "a") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("b", "a") == False
    assert cycpattern_check("b", "b") == True

def test_cycpattern_check_longer_words():
    assert cycpattern_check("abcdefg", "cdefg") == True
    assert cycpattern_check("abcdefg", "defg") == True
    assert cycpattern_check("abcdefg", "efg") == True
    assert cycpattern_check("abcdefg", "fgh") == True
    assert cycpattern_check("abcdefg", "gh") == True
    assert cycpattern_check("abcdefg", "edg") == True
    assert cycpattern_check("abcdefg", "g") == True
    assert cycpattern_check("abcdefg", "h") == False
    assert cycpattern_check("abcdefg", "i") == False
    assert cycpattern_check("abcdefg", "j") == False
    assert cycpattern_check("abcdefg", "k") == False
    assert cycpattern_check("abcdefg", "l") == False
    assert cycpattern_check("abcdefg", "m") == False
    assert cycpattern_check("abcdefg", "n") == False
    assert cycpattern_check("abcdefg", "o") == False
    assert cycpattern_check("abcdefg", "p") == False
    assert cycpattern_check("abcdefg", "q") == False
    assert cycpattern_check("abcdefg", "r") == False
    assert cycpattern_check("abcdefg", "s") == False
    assert cycpattern_check("abcdefg", "t") == False
    assert cycpattern_check("abcdefg", "u") == False
    assert cycpattern_check("abcdefg", "v") == False
    assert cycpattern_check("abcdefg", "w") == False
    assert cycpattern_check("abcdefg", "x") == False
    assert cycpattern_check("abcdefg", "y") == False
    assert cycpattern_check("abcdefg", "z") == False