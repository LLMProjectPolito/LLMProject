
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
    if not a or not b:
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False


def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_whassup():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_abab():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_efef():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_himenss():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_a_shorter_than_b():
    assert cycpattern_check("ab", "abc") == False

def test_cycpattern_check_long_strings_true():
    assert cycpattern_check("thisisalongstringwithpattern", "stringwith") == True

def test_cycpattern_check_long_strings_false():
    assert cycpattern_check("thisisalongstringwithoutpattern", "differentpattern") == False

def test_cycpattern_check_repeated_chars_true():
    assert cycpattern_check("aaaaaa", "aa") == True

def test_cycpattern_check_repeated_chars_false():
    assert cycpattern_check("aaaaaa", "aaaab") == False

def test_cycpattern_check_b_is_a():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "ell") == False