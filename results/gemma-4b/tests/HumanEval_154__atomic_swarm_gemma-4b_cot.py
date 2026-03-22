import pytest
import math

def test_basic():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_empty_string():
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "") == True

import pytest

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not isinstance(a, str) or not isinstance(b, str):
        return False
    if not a or not b:
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False
    
@pytest.mark.parametrize(
    "a, b",
    [
        ("abcd", "abd"),
        ("hello", "ell"),
        ("whassup", "psus"),
        ("abab", "baa"),
        ("efef", "eeff"),
        ("himenss","simen"),
        ("", "abc"),
        ("abc", ""),
        (123, "abc"),
        ("abc", 123)
    ],
)
def test_cycpattern_check(a, b):
    assert cycpattern_check(a, b) == False