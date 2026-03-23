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
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "acb") == True

def test_cycpattern_check_rotation_false():
    assert cycpattern_check("abcd", "cdab") == False
    assert cycpattern_check("abc", "bac") == False
    assert cycpattern_check("abc", "cba") == False
    assert cycpattern_check("abc", "abc") == False

def test_cycpattern_check_longer_strings():
    assert cycpattern_check("thisisalongstring", "string") == True
    assert cycpattern_check("thisisalongstring", "longstr") == True
    assert cycpattern_check("thisisalongstring", "stringt") == True
    assert cycpattern_check("thisisalongstring", "stringi") == False
    assert cycpattern_check("thisisalongstring", "sstring") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "cab") == True