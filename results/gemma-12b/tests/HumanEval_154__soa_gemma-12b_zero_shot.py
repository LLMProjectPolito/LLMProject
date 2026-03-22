import pytest
from your_module import cycpattern_check  # Replace your_module

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_rotation_false():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_longer_pattern_false():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_rotation_true_complex():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_pattern():
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_empty_text():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_identical_strings():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_pattern_longer_than_text():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_pattern_is_substring():
    assert cycpattern_check("this is a test", "is a") == True

def test_cycpattern_check_pattern_with_spaces():
    assert cycpattern_check("hello world", "world") == True

def test_cycpattern_check_pattern_with_special_characters():
    assert cycpattern_check("abc!@#", "!@#") == True

def test_cycpattern_check_pattern_with_unicode():
    assert cycpattern_check("你好世界", "世界") == True

def test_cycpattern_check_text_with_unicode():
    assert cycpattern_check("你好世界", "你好") == True

def test_cycpattern_check_unicode_and_ascii():
    assert cycpattern_check("hello你好", "你好") == True

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "hello") == False

def test_cycpattern_check_overlapping_pattern():
    assert cycpattern_check("aaaa", "aa") == True

def test_cycpattern_check_complex_rotation():
    assert cycpattern_check("abcdef", "defabc") == True

def test_cycpattern_check_long_string_true():
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10
    assert cycpattern_check(long_string, "uvwxyz") == True

def test_cycpattern_check_long_string_false():
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10
    assert cycpattern_check(long_string, "zyxwvu") == False