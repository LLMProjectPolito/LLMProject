
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
    if b in a or b in a[1:] or b in a[:-1]:
        return True
    else:
        return False

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abcd", "bcda") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("hello", "lohel") == True

def test_cycpattern_check_rotation_false():
    assert cycpattern_check("abcd", "acbd") == False
    assert cycpattern_check("abc", "bac") == False
    assert cycpattern_check("hello", "olleh") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("hello", "hello") == True

def test_cycpattern_check_long_strings():
    assert cycpattern_check("thisisalongstring", "longstr") == True
    assert cycpattern_check("thisisalongstring", "string") == True
    assert cycpattern_check("thisisalongstring", "stringlong") == False

def test_cycpattern_check_edge_cases():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("ab", "ba") == True
    assert cycpattern_check("ab", "ab") == True