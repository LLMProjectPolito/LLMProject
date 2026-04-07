
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

def test_cycpattern_check_rotations():
    assert cycpattern_check("abcd", "bcda") == True
    assert cycpattern_check("abcd", "dabc") == True
    assert cycpattern_check("abcd", "cdab") == True
    assert cycpattern_check("abcd", "abdc") == False

def test_cycpattern_check_longer_strings():
    assert cycpattern_check("thisisalongstring", "islo") == True
    assert cycpattern_check("thisisalongstring", "longstr") == True
    assert cycpattern_check("thisisalongstring", "string") == True
    assert cycpattern_check("thisisalongstring", "ngstrin") == True
    assert cycpattern_check("thisisalongstring", "ginstr") == False

def test_cycpattern_check_overlapping():
    assert cycpattern_check("aaaaa", "aaa") == True
    assert cycpattern_check("aaaaa", "aa") == True
    assert cycpattern_check("aaaaa", "a") == True
    assert cycpattern_check("aaaaa", "aaaa") == True

def test_cycpattern_check_special_characters():
    assert cycpattern_check("!@#$%^", "!@#") == True
    assert cycpattern_check("!@#$%^", "$%^!") == True
    assert cycpattern_check("!@#$%^", "^%$#!") == True
    assert cycpattern_check("!@#$%^", "#$%^!") == False