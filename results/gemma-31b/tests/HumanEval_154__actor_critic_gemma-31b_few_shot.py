
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

def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its 
    rotations is a substring in the first word.
    """
    if not b:
        return True
    if len(b) > len(a):
        return False
    
    # A string containing all rotations of b is b + b (minus the last character to avoid duplicates)
    # However, for substring checking, b + b contains every possible rotation of length len(b)
    combined = b + b
    for i in range(len(b)):
        rotation = combined[i : i + len(b)]
        if rotation in a:
            return True
    return False

def test_cycpattern_provided_examples():
    """Tests the examples provided in the docstring."""
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_rotations():
    """Tests cases where only a rotation of the second word is a substring."""
    # "waterbottle" contains "bottle" (rotation of "tlebot")
    assert cycpattern_check("waterbottle", "tlebot") == True 
    # "racecar" contains "ace" (rotation of "cea")
    assert cycpattern_check("racecar", "cea") == True
    # "abcdef" contains "abc" (rotation of "cab")
    assert cycpattern_check("abcdef", "cab") == True
    # "abcdef" contains "adef" (rotation of "fade")
    assert cycpattern_check("abcdef", "fade") == True
    # "abcdef" does NOT contain any rotation of "bfa" (bfa, fab, abf)
    assert cycpattern_check("abcdef", "bfa") == False

def test_cycpattern_length_edge_cases():
    """Tests cases involving string lengths."""
    # b is longer than a (should always be False)
    assert cycpattern_check("short", "longerstring") == False
    # a and b are identical
    assert cycpattern_check("equal", "equal") == True
    # a and b are rotations of each other
    assert cycpattern_check("abcde", "deabc") == True

def test_cycpattern_empty_and_single():
    """Tests empty strings and single character strings."""
    # Empty b is typically considered a substring of any string
    assert cycpattern_check("anything", "") == True
    # Empty a, non-empty b
    assert cycpattern_check("", "something") == False
    # Both empty
    assert cycpattern_check("", "") == True
    # Single characters
    assert cycpattern_check("a", "a") == True
    assert cycpattern_check("a", "b") == False

def test_cycpattern_case_sensitivity():
    """Tests that the function is case sensitive."""
    assert cycpattern_check("Hello", "ell") == True
    assert cycpattern_check("Hello", "ELL") == False

def test_cycpattern_special_characters():
    """Tests strings containing whitespace and special characters."""
    # Rotation of "orld hel" is "hello world"
    assert cycpattern_check("hello world", "orld hel") == True
    # Rotation of " !a" is "a! "
    assert cycpattern_check("test a! ", " !a") == True
    # No rotation of "xyz" in "x y z"
    assert cycpattern_check("x y z", "xyz") == False

def test_cycpattern_repetitive_characters():
    """Tests strings with highly repetitive characters to check for off-by-one errors."""
    assert cycpattern_check("aaaaa", "aa") == True
    assert cycpattern_check("aaaaa", "aaa") == True
    assert cycpattern_check("aa", "aaa") == False
    assert cycpattern_check("ababab", "bab") == True

@pytest.mark.parametrize("a, b, expected", [
    ("abcdef", "defabc", True),    # Full rotation match
    ("mississippi", "ippis", True), # "ippis" is rotation of "sippi"
    ("banana", "nan", True),       # Simple substring
    ("banana", "ann", True),       # Rotation of "nan"
    ("xyz", "yxz", False),         # Not a rotation/substring
])
def test_cycpattern_parametrized(a, b, expected):
    """Parametrized tests for various combinations."""
    assert cycpattern_check(a, b) == expected