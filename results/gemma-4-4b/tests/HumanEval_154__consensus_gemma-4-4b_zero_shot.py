
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
from typing import List

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n = len(b)
    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
        ("abc", "bc", True),
        ("abc", "cba", False),
        ("abc", "abc", True),
        ("abc", "ac", True),
        ("abc", "bca", False),
        ("abc", "cab", False),
        ("abc", "a", True),
        ("abc", "c", True),
        ("abc", "", False),
        ("", "abc", False),
        ("", "", True),
        ("aaaa", "aaa", True),
        ("aaaa", "a", True),
        ("aaaa", "aa", True),
        ("aaaa", "aaa", True),
        ("aaaa", "aaaa", True),
        ("aaaa", "aaaaa", False),
        ("xyz", "yzx", True),
        ("xyz", "zyx", True),
        ("xyz", "xzy", True),
    ],
)
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected