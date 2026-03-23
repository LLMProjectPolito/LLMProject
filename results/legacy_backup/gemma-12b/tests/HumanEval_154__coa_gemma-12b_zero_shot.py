import pytest
import math


# Focus: Boundary Values
def test_cycpattern_check_empty_string():
    assert cycpattern_check("", "") == False
    assert cycpattern_check("abc", "") == False
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_single_char_match():
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("abc", "a") == True
    assert cycpattern_check("abc", "b") == True
    assert cycpattern_check("abc", "c") == True
    assert cycpattern_check("a", "b") == False

def test_cycpattern_check_single_char_rotation():
    assert cycpattern_check("abc", "cba") == False
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "bca") == True

# Focus: Type Scenarios
def test_cycpattern_check_substring_present():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_substring_not_present():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_rotation_present():
    assert cycpattern_check("abab", "baa") == True

# Focus: Logic Branches
def test_cycpattern_check_substring_present():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_rotation_present():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("whassup", "psus") == False