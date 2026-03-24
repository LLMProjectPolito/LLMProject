
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
    if not b:
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

def test_cycpattern_check_whassup():
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

def test_cycpattern_check_pattern_longer_than_string():
    assert cycpattern_check("abc", "abcdefg") == False

def test_cycpattern_check_pattern_contains_chars_not_in_string():
    assert cycpattern_check("abc", "axc") == False

def test_cycpattern_check_string_contains_pattern_multiple_times():
    assert cycpattern_check("ababab", "abab") == False

def test_cycpattern_check_single_char_match():
    assert cycpattern_check("a", "a") == True

def test_cycpattern_check_single_char_no_match():
    assert cycpattern_check("a", "b") == False

def test_cycpattern_check_repeated_chars_true():
    assert cycpattern_check("aaaa", "aa") == True

def test_cycpattern_check_repeated_chars_false():
    assert cycpattern_check("aaaa", "aba") == False

def test_cycpattern_check_repeated_chars_true_complex():
    assert cycpattern_check("abababab", "abab") == True

def test_cycpattern_check_repeated_chars_false_complex():
    assert cycpattern_check("abababab", "abaa") == False