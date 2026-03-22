import pytest
import math


# Focus: Boundary Values
def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char_boundary():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("aa", "a") == True
    assert cycpattern_check("aa", "aa") == True
    assert cycpattern_check("aa", "ab") == False

def test_cycpattern_check_rotation_boundary():
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "bca") == True
    assert cycpattern_check("abc", "acb") == False
    assert cycpattern_check("abab", "baab") == True
    assert cycpattern_check("abab", "abab") == True
    assert cycpattern_check("abab", "baba") == True
    assert cycpattern_check("abab", "abba") == False

# Focus: Type Scenarios
def test_cycpattern_check_string_types():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == False
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "cba") == True

# Focus: Logic Branches
def test_cycpattern_check_substring_present():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_rotation_present():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_substring_not_present():
    assert cycpattern_check("abcd", "abd") == False