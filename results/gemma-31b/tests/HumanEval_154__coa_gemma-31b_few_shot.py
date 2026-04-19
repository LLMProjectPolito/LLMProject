
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
import math


# Focus: Boundary Values
import pytest

def test_cycpattern_check_empty_and_single():
    assert cycpattern_check("", "") == True
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False
    assert cycpattern_check("", "a") == False

def test_cycpattern_check_length_boundaries():
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abc", "abc") == True
    assert cycpattern_check("abc", "cab") == True
    assert cycpattern_check("abc", "bca") == True

# Focus: Rotation Scenarios
def test_rotation_substring_exists():
    # "simen" rotated to "imens" is a substring of "himenss"
    assert cycpattern_check("himenss", "simen") == True
    # "baa" rotated to "aba" is a substring of "abab"
    assert cycpattern_check("abab", "baa") == True

def test_rotation_substring_not_exists():
    # "psus" rotations (susp, usps, spsu) are not in "whassup"
    assert cycpattern_check("whassup", "psus") == False
    # "eeff" rotations (effe, ffee, feef) are not in "efef"
    assert cycpattern_check("efef", "eeff") == False

def test_full_word_rotation():
    # "abcd" rotated to "cdab" is a substring of "abcdcdab"
    assert cycpattern_check("abcdcdab", "cdab") == True
    # "apple" rotated to "leapp" is a substring of "appleleapp"
    assert cycpattern_check("appleleapp", "leapp") == True

# Focus: Substring Logic
def test_cycpattern_substring_basic():
    assert cycpattern_check("hello", "ell") is True
    assert cycpattern_check("himenss", "simen") is True

def test_cycpattern_substring_rotation():
    assert cycpattern_check("abab", "baa") is True
    assert cycpattern_check("abcd", "cdab") is True

def test_cycpattern_substring_negative():
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("efef", "eeff") is False