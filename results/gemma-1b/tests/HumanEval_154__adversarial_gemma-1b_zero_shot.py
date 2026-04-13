
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
    s1 = a
    s2 = b
    s3 = s1
    s4 = s2
    s5 = s3

    if len(s1) >= len(s2):
        for i in range(len(s2)):
            rotated_s2 = s2[i:] + s2[:i]
            if rotated_s2 in s1:
                return True
    else:
        for i in range(len(s1)):
            rotated_s1 = s1[i:] + s1[:i]
            if rotated_s1 in s2:
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
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("a", "ab") == False

def test_cycpattern_check_longer_words():
    assert cycpattern_check("abcdefg", "def") == True
    assert cycpattern_check("abcdefg", "fed") == True
    assert cycpattern_check("abcdefg", "fgh") == True
    assert cycpattern_check("abcdefg", "g") == True
    assert cycpattern_check("abcdefg", "abc") == False