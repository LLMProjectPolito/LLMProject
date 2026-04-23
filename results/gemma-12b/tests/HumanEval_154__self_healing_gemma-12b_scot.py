
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

def test_cycpattern_check_rotation():
    assert cycpattern_check("abcde", "cdea") == True
    assert cycpattern_check("abcde", "deab") == True
    assert cycpattern_check("abcde", "eabc") == True
    assert cycpattern_check("abcde", "bcde") == True
    assert cycpattern_check("abcde", "bcdea") == False

def test_cycpattern_check_substring_at_start():
    assert cycpattern_check("abcdef", "abc") == True

def test_cycpattern_check_substring_at_end():
    assert cycpattern_check("abcdef", "def") == True

def test_cycpattern_check_substring_in_middle():
    assert cycpattern_check("abcdef", "cde") == True

def test_cycpattern_check_long_strings():
    assert cycpattern_check("thisisalongstring", "longstr") == True
    assert cycpattern_check("thisisalongstring", "strlong") == True
    assert cycpattern_check("thisisalongstring", "stringlong") == True
    assert cycpattern_check("thisisalongstring", "longstringt") == False

def test_cycpattern_check_special_characters():
    assert cycpattern_check("!@#$%^", "@#$%") == True
    assert cycpattern_check("!@#$%^", "$%^!") == True
    assert cycpattern_check("!@#$%^", "!@#$") == False

def test_cycpattern_check_numbers():
    assert cycpattern_check("12345", "234") == True
    assert cycpattern_check("12345", "3451") == False
    assert cycpattern_check("12345", "5123") == True