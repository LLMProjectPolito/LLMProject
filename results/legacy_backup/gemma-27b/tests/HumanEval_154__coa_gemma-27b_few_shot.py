import pytest
import math


# Focus: Substring Presence
def test_substring_presence_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_substring_presence_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_substring_presence_rotation_true():
    assert cycpattern_check("abab", "baa") == True

# Focus: Rotation Handling
def test_cycpattern_check_rotation_present():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_no_rotation_present():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_rotation_at_end():
    assert cycpattern_check("abab", "baa") == True

# Focus: Edge Cases - Empty/Null Strings
def test_cycpattern_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_empty_b():
    assert cycpattern_check("abcd", "") == True

def test_cycpattern_both_empty():
    assert cycpattern_check("", "") == True