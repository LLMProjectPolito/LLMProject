
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
    
    # Basic matches
    ("apple", "ple", True),
    ("apple", "app", True),
    ("banana", "nan", True),
    ("watermelon", "ter", True),
    ("abcdefg", "bcdef", True),
    ("abcdefg", "bcdefg", True),
    ("abcdefg", "abc", True),
    
    # Rotated matches
    ("apple", "lep", True),
    ("banana", "ann", True),
    ("apple", "leapp", True),
    ("apple", "pleap", True),
    ("Hello", "ellH", True),
    ("abc", "cab", True),
    ("abc", "bca", True),
    ("racecar", "arrac", True),
    
    # Negative cases
    ("apple", "apl", False),
    ("python", "typh", False),
    ("abcdef", "fabc", False),
    ("abcdefg", "gabc", False),
    ("abcdefg", "gade", False),
    ("abcdefg", "fab", False),
    ("abcdefg", "fgabc", False),
    ("abcdefg", "cba", False),
    ("ababab", "baab", False),
    
    # Edge Cases: Lengths
    ("abc", "abcd", False),
    ("abcd", "abcde", False),
    ("a", "a", True),
    ("a", "b", False),
    
    # Edge Cases: Empty strings
    ("", "a", False),
    ("a", "", True),
    ("", "", True),
    
    # Repetitive characters
    ("aaaaa", "aa", True),
    ("aaaaa", "aaa", True),
    ("ababab", "bab", True),
    ("ababab", "aba", True),
    ("efefef", "fefe", True),
    
    # Case sensitivity
    ("Hello", "ell", True),
    ("Hello", "ELL", False),
    ("Hello", "Ohel", False),
    ("Hello", "ohel", False),
    ("Hello", "loHe", False),
    
    # Special characters and numbers
    ("123456", "612", False),
    ("123456", "234", True),
    ("!@#$%", "%!@", False),
    ("!@#$%^", "^!@#", False),
])
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_long_strings():
    # Test with longer strings to ensure robustness
    a = "abcdefghijklmnopqrstuvwxyz"
    # Rotations of "zabc": "zabc", "abcz", "bcza", "czab". None are in a.
    assert cycpattern_check(a, "zabc") == False
    # Rotations of "xyzab": "xyzab", "yzabx", "zabxy", "abxyz", "bxyza". None are in a.
    assert cycpattern_check(a, "xyzab") == False
    # "bcde" is a substring of a
    assert cycpattern_check(a, "bcde") == True

def test_cycpattern_check_full_rotation():
    # b is a full rotation of a
    assert cycpattern_check("abcde", "deabc") == True
    assert cycpattern_check("abcde", "cdeab") == True
    assert cycpattern_check("abcde", "bcdea") == True

def test_cycpattern_check_single_char():
    assert cycpattern_check("hello", "h") == True
    assert cycpattern_check("hello", "z") == False
    assert cycpattern_check("a", "a") == True