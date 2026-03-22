import pytest
import math

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b in a or any(rotation in a for rotation in rotate(b)):
        return True
    else:
        return False

def rotate(s):
    return s[1:] + s[0]

@pytest.mark.parametrize("a, b", [
    ("abcd", "abd"),
    ("hello", "ell"),
    ("whassup", "psus"),
    ("abab", "baa"),
    ("efef", "eeff"),
    ("himenss","simen"),
    ("abc", "cba"),
    ("abc", "bca"),
    ("abc", "cab"),
    ("abc", "acb"),
    ("aaaa", "aa"),
    ("aaaa", "aaa"),
    ("aaaa", "aaaa"),
    ("abcde", "cdeab")
])
def test_cycpattern_check(a, b):
    assert cycpattern_check(a, b) == True

def test_empty_b():
    assert cycpattern_check("abcd", "") == True