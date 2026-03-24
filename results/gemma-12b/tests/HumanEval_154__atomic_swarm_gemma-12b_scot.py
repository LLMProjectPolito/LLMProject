
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

def test_cycpattern_check_positive():
    assert cycpattern_check("hello","ell") == True

def test_empty_first_word():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_wrong_type():
    """Test with non-string inputs."""
    assert cycpattern_check(123, "abc") == False
    assert cycpattern_check("abc", 456) == False
    assert cycpattern_check(123, 456) == False