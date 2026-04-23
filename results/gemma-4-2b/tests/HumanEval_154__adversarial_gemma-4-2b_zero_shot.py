
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

def test_empty_string():
    assert cycpattern_check("", "") == False

def test_empty_a():
    assert cycpattern_check("", "abc") == False

def test_empty_b():
    assert cycpattern_check("abc", "") == False

def test_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_rotation_false():
    assert cycpattern_check("efef", "eeff") == False

def test_complex_true():
    assert cycpattern_check("himenss", "simen") == True

def test_complex_false():
    assert cycpattern_check("abcdefg", "xyz") == False

def test_same_string_true():
    assert cycpattern_check("abc", "abc") == True

def test_long_string_true():
    assert cycpattern_check("thisisalongstring", "longstring") == True

def test_long_string_false():
    assert cycpattern_check("thisisalongstring", "short") == False

def test_single_char_true():
    assert cycpattern_check("abc", "a") == True

def test_single_char_false():
    assert cycpattern_check("abc", "b") == True

def test_single_char_true_rotation():
    assert cycpattern_check("abc", "c") == True

def test_single_char_false_rotation():
    assert cycpattern_check("abc", "d") == False