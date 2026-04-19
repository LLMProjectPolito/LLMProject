
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
    # --- Docstring Examples ---
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),      # Rotation 'aba' is in 'abab'
    ("efef", "eeff", False),
    ("himenss", "simen", True), # Rotation 'imens' is in 'himenss'
    
    # --- Basic Identity and Substring Cases ---
    ("abcdef", "abc", True),      # Exact substring
    ("abcdef", "def", True),      # Exact substring at end
    ("abcdef", "bcd", True),      # Exact substring in middle
    ("apple", "apple", True),     # Identical strings
    ("apple", "banana", False),   # Completely different strings
    
    # --- Rotation Logic (Corrected) ---
    ("abcdef", "fde", True),      # Rotation 'def' is in 'abcdef'
    ("abcdef", "cab", True),      # Rotation 'abc' is in 'abcdef'
    ("abcdef", "efa", False),     # Rotations: efa, fae, aef. None in 'abcdef'
    ("abcdef", "fabc", False),    # Rotations: fabc, abcf, bcfa, cfab. None in 'abcdef'
    ("abcdef", "cdefa", False),   # Rotations: cdefa, defac, efacd, facde, acdef. None in 'abcdef'
    ("abcde", "eab", False),      # Rotations: eab, abe, bea. None in 'abcde'
    ("abcde", "dea", False),      # Rotations: dea, ead, ade. None in 'abcde'
    ("abcde", "deabc", True),     # Rotation 'abcde' is in 'abcde'
    ("substringsearch", "archs", True), # Rotation 'sarch' is in 'substringsearch'
    ("apple", "pleap", True),     # Rotation 'apple' is in 'apple'
    ("apple", "pplea", True),     # Rotation 'apple' is in 'apple'
    ("apple", "leapp", True),     # Rotation 'apple' is in 'apple'
    ("apple", "aelpp", False),    # Not a rotation of any substring
    ("watermelon", "emter", True), # Rotation 'terme' is in 'watermelon'
    ("watermelon", "rterm", False), # Not a rotation of any substring
    
    # --- Edge Cases: Lengths ---
    ("abc", "abcd", False),       # b longer than a
    ("a", "a", True),             # Single character match
    ("a", "b", False),            # Single character mismatch
    ("aaaaa", "aa", True),        # Repeating characters
    ("ababab", "bab", True),      # Repeating pattern
    
    # --- Edge Cases: Empty Strings ---
    ("", "a", False),             # a empty, b not
    ("a", "", True),              # b empty (empty string is always a substring)
    ("", "", True),               # both empty
    
    # --- Case Sensitivity and Special Characters ---
    ("Hello World", "World", True),  # Exact match
    ("Hello World", "dlroW", False), # Reverse is not rotation
    ("Hello World", "loWor", False), # Rotations of 'loWor' not in 'Hello World'
    ("123456", "612", False),        # Rotations: 612, 126, 261. None in '123456'
    ("123456", "561", False),        # Rotations: 561, 615, 156. None in '123456'
    ("123456", "234", True),         # Exact match
    ("!@#$%", "%!@", False),         # Rotations: %!@, !@%, @%!. None in '!@#$%'
    ("!@#$%", "@#$%", True),         # Exact match
    ("the quick brown fox", "ick qu", True),
    ("the quick brown fox", "uick q", True),
])
def test_cycpattern_check_variants(a, b, expected):
    """Comprehensive test suite for cycpattern_check covering rotations, edge cases, and types."""
    assert cycpattern_check(a, b) == expected

def test_case_sensitivity():
    """Verify that the check is strictly case sensitive."""
    assert cycpattern_check("Hello", "ell") == True
    assert cycpattern_check("Hello", "ELL") == False
    assert cycpattern_check("Hello", "oHel") == True # Rotation of 'Hello'

def test_special_character_rotations():
    """Test rotations specifically with special character strings."""
    # !@#$%^ contains !@#$ and @#$%
    # Rotation of ^!@#$ is !@#$^ (not in a)
    assert cycpattern_check("!@#$%^", "^!@#$") == False
    # Rotation of $%^!@ is !@$%^ (not in a)
    assert cycpattern_check("!@#$%^", "$%^!@") == False