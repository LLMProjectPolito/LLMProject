
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
    if not b:
        return False
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abcd", "") == False

def test_cycpattern_check_rotation_is_entire_string():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_no_rotation_found():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_rotation_found():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_rotation_found_2():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_rotation_found_3():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_long_string_true():
    assert cycpattern_check("thisisalongstringwithalongrotation", "alongrotation") == True

def test_cycpattern_check_long_string_false():
    assert cycpattern_check("thisisalongstringwithalongrotation", "notfound") == False