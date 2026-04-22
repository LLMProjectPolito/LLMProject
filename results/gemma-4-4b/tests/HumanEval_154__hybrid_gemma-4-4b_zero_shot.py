
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
    n = len(a)
    m = len(b)

    if m > n:
        return False
    
    for i in range(m):
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
        ("abc", "abc", True),
        ("abc", "bca", True),
        ("abc", "cab", True),
        ("abc", "acb", True),
        ("abc", "def", False),
        ("abc", "", False),
        ("", "abc", False),
        ("", "", True),
        ("aaaaa", "aaa", True),
        ("aaaaa", "aab", False),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
        ("ab", "ab", True),
        ("abcde", "cde", True),
        ("abcde", "edc", True),
        ("abcde", "abc", True),
        ("abcde", "eab", False),
        ("racecar", "race", True),
        ("racecar", "car", True),
        ("racecar", "ace", False),
        ("test", "tse", True),
        ("test", "est", True),
        ("test", "set", False),
        ("longerstring", "ing", True),
        ("longerstring", "gni", True),
        ("longerstring", "gnl", False),
        ("aaa", "aa", True),
        ("aaa", "aaa", True),
        ("aaa", "aab", False),
    ],
)
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (str(i) * 5, str(i) * 3, True) for i in range(1, 6)
    ],
)
def test_long_strings(a, b, expected):
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
      ("aaaaaaaaaa", "aaaaaaa", True),
      ("aaaaaaaaaa", "b", False),
      ("aaaaaaaaaa", "aaaaaaaaaa", True)
    ]
)
def test_many_repeats(a, b, expected):
    assert cycpattern_check(a, b) == expected