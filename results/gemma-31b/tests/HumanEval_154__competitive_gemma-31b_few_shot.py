
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
    # Provided examples
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
    
    # Edge cases: Empty strings
    ("", "a", False),
    ("a", "", True),
    ("", "", True),
    
    # Edge cases: Lengths
    ("abc", "abcd", False),
    ("abcd", "abc", True),
    ("abc", "abc", True),
    
    # Rotations
    ("abcdef", "defabc", True),
    ("apple", "pleap", True),
    ("banana", "nanab", True),
    ("test", "stte", False),
    
    # Substring but not rotation
    ("abcdefg", "cde", True),
    ("abcdefg", "deg", False),
    
    # Case sensitivity and special characters
    ("Hello World", "loWor", True),
    ("Hello World", "lowor", False),
    ("123456", "5612", True),
    ("!@#$%^", "^!@#", True),
])
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected