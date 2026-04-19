
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

@pytest.mark.parametrize("a, b, expected", [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    ("abcdef", "def", True),
    ("abcdef", "fde", False),
    ("abcdef", "fab", False),
    ("abcdef", "efa", True),
    ("apple", "pleap", True),
    ("apple", "leapp", True),
    ("apple", "apple", True),
    ("banana", "anan", True),
    ("banana", "nana", True),
    ("banana", "aanb", False),
    ("", "a", False),
    ("a", "", True),
    ("", "", True),
    ("short", "longerthanashortstring", False),
    ("single", "s", True),
    ("single", "e", True),
    ("single", "z", False),
    ("caseSensitive", "sensitive", True),
    ("caseSensitive", "Sitivecase", False), # Case mismatch
])
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_rotation_logic():
    # "abc" rotations: "abc", "bca", "cab"
    assert cycpattern_check("xyzabcy", "abc") is True
    assert cycpattern_check("xyzbca y", "abc") is True
    assert cycpattern_check("xyzcab y", "abc") is True
    assert cycpattern_check("xyzacb y", "abc") is False

def test_cycpattern_check_overlap():
    # Test where rotation creates a substring that overlaps in the original string
    assert cycpattern_check("aaaaa", "aa") is True
    assert cycpattern_check("ababab", "bab") is True