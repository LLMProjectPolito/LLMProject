
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

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b in a:
        return True
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("a", "") == False

def test_cycpattern_check_basic_cases():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "acb") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abc", "def") == False
    assert cycpattern_check("xyz", "uvw") == False

def test_cycpattern_check_longer_strings():
    assert cycpattern_check("thisisalongstring", "isalong") == True
    assert cycpattern_check("thisisalongstring", "longstring") == True
    assert cycpattern_check("thisisalongstring", "string") == True
    assert cycpattern_check("thisisalongstring", "longstringis") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True
    assert cycpattern_check("abc", "d") == False

def test_cycpattern_check_duplicate_chars():
    assert cycpattern_check("aaaa", "aaa") == True
    assert cycpattern_check("aaaa", "a") == True
    assert cycpattern_check("aaaa", "aa") == True
    assert cycpattern_check("aaaa", "aaaa") == True
    assert cycpattern_check("aaaa", "aba") == False