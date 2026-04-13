
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
    if not a or not b:
        return False

    if len(b) > len(a):
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False


def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_whassup_psus():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_abab_baa():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_efef_eeff():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_himenss_simen():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_a_equals_b():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcdef") == False

def test_cycpattern_check_a_shorter_than_b_not_rotation():
    assert cycpattern_check("ab", "abc") == False

def test_cycpattern_check_b_longer_than_a_and_rotation():
    assert cycpattern_check("abcdef", "defabc") == True

def test_cycpattern_check_overlapping_patterns():
    assert cycpattern_check("ababab", "bababa") == True

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "ell") == False  # Case-sensitive

def test_cycpattern_check_case_insensitive():
    assert cycpattern_check("Hello", "ell") == False #Case-sensitive

def test_cycpattern_check_unicode_characters():
    assert cycpattern_check("你好世界", "世界") == True
    assert cycpattern_check("你好世界", "你好") == True
    assert cycpattern_check("你好世界", "世界你好") == True
    assert cycpattern_check("你好世界", "世界你") == False