
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
    if b in a or b in a[1:] or b in a[:-1]:
        return True
    else:
        return False

def test_cycpattern_check_positive():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("himenss","simen") == True
    assert cycpattern_check("abcabc","abc") == True
    assert cycpattern_check("abcabc","bca") == True
    assert cycpattern_check("abcabc","cab") == True

def test_cycpattern_check_negative():
    assert cycpattern_check("abcd","abc") == False
    assert cycpattern_check("abcd","efgh") == False
    assert cycpattern_check("hello","world") == False
    assert cycpattern_check("whassup","hello") == False
    assert cycpattern_check("abab","cdef") == False
    assert cycpattern_check("himenss","hello") == False
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True
    assert cycpattern_check("abc", "d") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True

def test_cycpattern_check_long_strings():
    assert cycpattern_check("abcdefgh", "cdef") == True
    assert cycpattern_check("abcdefgh", "fgh") == True
    assert cycpattern_check("abcdefgh", "ghi") == False
    assert cycpattern_check("abcdefgh", "abcdefgh") == True