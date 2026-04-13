
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    An empty string `b` is considered a substring of any string `a`, so the function returns True in that case.
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    Raises TypeError if a is empty.
    """
    if not a:
        raise TypeError("Input string 'a' cannot be empty.")
    if not b:
        return True

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False

import pytest

@pytest.mark.parametrize("a, b, expected", [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    ("abc", "abc", True), # a and b are identical
    ("aaaaa", "aa", True), # multiple occurrences
    ("abcde", "cdeab", True), # rotation at the end
    ("abc", "abcd", False), # b is longer than a
])
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_empty_a():
    with pytest.raises(TypeError):
        cycpattern_check("", "abc")