import pytest
from your_module import cycpattern_check  # Replace your_module

def test_positive_case():
    assert cycpattern_check("hello", "ell") == True

def test_negative_case():
    assert cycpattern_check("whassup", "psus") == False

def test_rotation_case():
    assert cycpattern_check("abab", "baa") == True

def test_empty_a():
    assert cycpattern_check("", "abc") == False

def test_empty_b():
    assert cycpattern_check("abc", "") == False

def test_both_empty():
    assert cycpattern_check("", "") == False

def test_identical_strings():
    assert cycpattern_check("abc", "abc") == True

def test_b_longer_than_a():
    assert cycpattern_check("abc", "abcdef") == False

def test_overlapping_rotations():
    assert cycpattern_check("abcabc", "bca") == True

def test_no_match_long_strings():
    assert cycpattern_check("abcdefghijk", "xyz") == False

def test_case_sensitive():
    assert cycpattern_check("Hello", "ell") == False

def test_rotation_substring_check():
    assert cycpattern_check("abcdef", "abc") == True
    assert cycpattern_check("abcdef", "def") == True
    assert cycpattern_check("abcdef", "ghi") == False

def test_single_char_match():
    assert cycpattern_check("abc", "a") == True

def test_single_char_no_match():
    assert cycpattern_check("abc", "d") == False

def test_unicode_characters():
    assert cycpattern_check("你好世界", "世界") == True
    assert cycpattern_check("你好世界", "界你") == True

def test_special_characters():
    assert cycpattern_check("a!b@c", "b@c!") == True
    assert cycpattern_check("a!b@c", "c@b!") == True

def test_long_string_positive():
    long_a = "abcdefghijk" * 10
    long_b = "ghijkabcdef"
    assert cycpattern_check(long_a, long_b) == True