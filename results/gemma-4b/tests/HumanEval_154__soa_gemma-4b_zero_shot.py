
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
    if b in a or any(rotation in a for rotation in rotate(b)):
        return True
    else:
        return False

def rotate(s):
    return s[1:] + s[0]

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

def test_cycpattern_check_rotations():
    assert cycpattern_check("abcde", "cdea") == True
    assert cycpattern_check("abcde", "eabcd") == True
    assert cycpattern_check("abcde", "bcdea") == True
    assert cycpattern_check("abcde", "deabc") == True
    assert cycpattern_check("abcde", "abced") == False

def test_cycpattern_check_longer_strings():
    assert cycpattern_check("thisisalongstring", "string") == True
    assert cycpattern_check("thisisalongstring", "longstr") == True
    assert cycpattern_check("thisisalongstring", "stringt") == False
    assert cycpattern_check("thisisalongstring", "stringi") == False

def test_cycpattern_check_overlapping():
    assert cycpattern_check("aaaaa", "aaa") == True
    assert cycpattern_check("aaaaa", "aa") == True
    assert cycpattern_check("aaaaa", "a") == True
    assert cycpattern_check("aaaaa", "aaaa") == True

def test_cycpattern_check_special_characters():
    assert cycpattern_check("!@#$%^", "!@#") == True
    assert cycpattern_check("!@#$%^", "^%$#!") == True
    assert cycpattern_check("!@#$%^", "abc") == False

def test_cycpattern_check_numbers():
    assert cycpattern_check("12345", "234") == True
    assert cycpattern_check("12345", "54321") == True
    assert cycpattern_check("12345", "123") == True
    assert cycpattern_check("12345", "1234") == False