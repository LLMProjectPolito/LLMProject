
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

def test_basic():
    assert cycpattern_check("hello","ell") == True

def test_empty_first_word():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_wrong_type():
    """Test with a non-string input."""
    try:
        cycpattern_check(123, "abc")
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass
    try:
        cycpattern_check("abc", 456)
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass