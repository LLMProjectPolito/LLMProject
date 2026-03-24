import pytest
from your_module import cycpattern_check  # Replace your_module

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_string():
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False
    assert cycpattern_check("", "") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "abcabc") == True
    assert cycpattern_check("abcabc", "abc") == True

def test_cycpattern_check_rotation_present():
    assert cycpattern_check("abcdef", "defabc") == True
    assert cycpattern_check("abcdef", "bcdefa") == True
    assert cycpattern_check("abcdef", "cdefab") == True
    assert cycpattern_check("abcdef", "defabc") == True
    assert cycpattern_check("abcdef", "efabcd") == True
    assert cycpattern_check("abcdef", "fabcde") == True

def test_cycpattern_check_substring_present():
    assert cycpattern_check("abcdef", "abc") == True
    assert cycpattern_check("abcdef", "bcd") == True
    assert cycpattern_check("abcdef", "cde") == True
    assert cycpattern_check("abcdef", "def") == True
    assert cycpattern_check("abcdef", "ef") == True
    assert cycpattern_check("abcdef", "f") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abcdef", "xyz") == False
    assert cycpattern_check("abcdef", "abcz") == False
    assert cycpattern_check("abcdef", "defg") == False

def test_cycpattern_check_long_strings():
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10
    assert cycpattern_check(long_string, "xyz") == False
    assert cycpattern_check(long_string, "abcdef") == True
    assert cycpattern_check(long_string, "uvwxyz") == True
    assert cycpattern_check(long_string, "abcdefghijklmnopqrstuvwxyz") == True

def test_cycpattern_check_special_characters():
    assert cycpattern_check("!@#$%^", "$%#@!") == True
    assert cycpattern_check("!@#$%^", "!@#$") == True
    assert cycpattern_check("!@#$%^", "%^!") == True
    assert cycpattern_check("!@#$%^", "abc") == False

def test_cycpattern_check_unicode_characters():
    assert cycpattern_check("你好世界", "世界你好") == True
    assert cycpattern_check("你好世界", "你好") == True
    assert cycpattern_check("你好世界", "世界") == True
    assert cycpattern_check("你好世界", "abc") == False