import pytest
from your_module import cycpattern_check  # Replace your_module

def test_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_no_rotation_false():
    assert cycpattern_check("whassup", "psus") == False

def test_longer_pattern_false():
    assert cycpattern_check("efef", "eeff") == False

def test_rotation_with_same_length():
    assert cycpattern_check("simen", "simen") == True

def test_rotation_with_same_length_false():
    assert cycpattern_check("simen", "enis") == False

def test_empty_pattern():
    assert cycpattern_check("hello", "") == False

def test_empty_text():
    assert cycpattern_check("", "ell") == False

def test_both_empty():
    assert cycpattern_check("", "") == False

def test_pattern_longer_than_text():
    assert cycpattern_check("abc", "abcdef") == False

def test_pattern_is_text():
    assert cycpattern_check("abc", "abc") == True

def test_pattern_is_rotation_of_text():
    assert cycpattern_check("abc", "bca") == True

def test_pattern_with_repeated_chars():
    assert cycpattern_check("aaaa", "aa") == True

def test_pattern_with_repeated_chars_false():
    assert cycpattern_check("aaaa", "aaa") == False

def test_pattern_with_repeated_chars_false2():
    assert cycpattern_check("aaaa", "bbbb") == False

def test_text_with_repeated_chars():
    assert cycpattern_check("ababab", "bab") == True

def test_text_with_repeated_chars_false():
    assert cycpattern_check("ababab", "aba") == False

def test_text_with_repeated_chars_false2():
    assert cycpattern_check("ababab", "abc") == False

def test_case_sensitive():
    assert cycpattern_check("Hello", "ell") == False  # Explicitly checks for case sensitivity

def test_unicode_characters():
    assert cycpattern_check("你好世界", "你好") == True

def test_unicode_rotation():
    assert cycpattern_check("你好世界", "界你好世") == True

def test_unicode_mixed_characters():
    assert cycpattern_check("hello你好", "你好hel") == True

def test_special_characters_pattern():
    assert cycpattern_check("!@#$%^", "@#$%^") == True

def test_special_characters_text():
    assert cycpattern_check("!@#$", "!") == True

def test_pattern_with_numbers():
    assert cycpattern_check("12345", "345") == True

def test_substring_not_rotation():
    assert cycpattern_check("abcdef", "cde") == False

def test_prefix_not_rotation():
    assert cycpattern_check("abcdef", "abc") == False

def test_long_string():
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10
    assert cycpattern_check(long_string, "xyz") == True

def test_long_string_no_match():
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10
    assert cycpattern_check(long_string, "abcde") == False