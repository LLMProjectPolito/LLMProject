
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
    n = len(b)
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_cycpattern_check_empty_strings():
    assert cycpattern_check("", "") == False
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_same_strings():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("aaaa", "aaaa") == True

def test_cycpattern_check_substring_at_start():
    assert cycpattern_check("abcdef", "abc") == True

def test_cycpattern_check_substring_at_end():
    assert cycpattern_check("abcdef", "def") == True

def test_cycpattern_check_substring_in_middle():
    assert cycpattern_check("abcdef", "cde") == True

def test_cycpattern_check_rotation_needed():
    assert cycpattern_check("waterbottle", "erbottlewat") == True

def test_cycpattern_check_long_strings():
    assert cycpattern_check("thisisalongstring", "longstring") == True
    assert cycpattern_check("thisisalongstring", "stringthisis") == True
    assert cycpattern_check("thisisalongstring", "isalongstrin") == True
    assert cycpattern_check("thisisalongstring", "notpresent") == False

def test_cycpattern_check_edge_cases():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("aa", "a") == True
    assert cycpattern_check("aa", "aa") == True
    assert cycpattern_check("abcabc", "bca") == True
    assert cycpattern_check("abcabc", "cab") == True
    assert cycpattern_check("abcabc", "abc") == True