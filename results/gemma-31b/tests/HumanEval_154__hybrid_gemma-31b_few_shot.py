
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
    You are given 2 words. You need to return True if the second word or any of its rotations 
    is a substring in the first word.
    """
    if not b:
        return True
    if len(b) > len(a):
        return False
    
    # A string concatenated with itself contains all possible cyclic rotations of that string
    # Example: "abc" -> "abcabc" contains "abc", "bca", "cab"
    combined_b = b + b
    # We only care about rotations of length len(b)
    for i in range(len(b)):
        rotation = combined_b[i : i + len(b)]
        if rotation in a:
            return True
    return False

# --- Superior Pytest Suite ---

@pytest.mark.parametrize("a, b, expected", [
    ("abcd", "abd", False),
    ("hello", "ell", True),
    ("whassup", "psus", False),
    ("abab", "baa", True),
    ("efef", "eeff", False),
    ("himenss", "simen", True),
])
def test_cycpattern_docstring_examples(a, b, expected):
    """Tests the examples provided in the problem description."""
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b", [
    # Direct substrings
    ("programming", "gram"),
    ("pythonic", "thon"),
    ("abcdefg", "cde"),
    ("abcdefg", "efg"),
    ("abcdefg", "abc"),
    # Rotations
    ("i love eappl", "apple"),       # 'apple' -> 'eappl'
    ("the ldwor is round", "world"), # 'world' -> 'ldwor'
    ("mycabstring", "abc"),          # 'abc' -> 'cab'
    ("apple", "leap"),               # 'leap' -> 'eapl' (in apple)
    ("racecar", "carra"),            # 'carra' -> 'arrac' (in racecar)
    ("programming", "mingpro"),      # 'mingpro' -> 'progr...'
    # Full matches and full rotations
    ("abcdef", "abcdef"),
    ("abcdef", "defabc"),
    ("abcdef", "bcdefa"),
])
def test_cycpattern_positive_cases(a, b):
    """Tests cases where the result should be True (direct, rotated, and full matches)."""
    assert cycpattern_check(a, b) is True

@pytest.mark.parametrize("a, b", [
    ("abcdefg", "xyz"),      # Completely different characters
    ("abcdefg", "ace"),      # Characters exist but not contiguous
    ("hello", "olelh"),      # Rotation is incorrect
    ("short", "longerstring"), # b longer than a
    ("abc", "abcd"),         # b slightly longer than a
    ("abc", "z"),            # Single character mismatch
])
def test_cycpattern_negative_cases(a, b):
    """Tests cases where the result should be False."""
    assert cycpattern_check(a, b) is False

@pytest.mark.parametrize("a, b, expected", [
    ("anything", "", True),   # Empty pattern is always a substring
    ("", "something", False), # Empty source cannot contain non-empty pattern
    ("", "", True),           # Both empty
    ("a", "a", True),         # Single char match
    ("a", "b", False),        # Single char mismatch
])
def test_cycpattern_edge_cases(a, b, expected):
    """Tests empty strings and single-character boundaries."""
    assert cycpattern_check(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("aaaaa", "aa"),
    ("ababab", "ba"),
    ("ababab", "aba"),
    ("aaaaa", "aaa"),
])
def test_cycpattern_repeated_characters(a, b):
    """Tests strings consisting of repeated characters."""
    assert cycpattern_check(a, b) is True

def test_cycpattern_case_sensitivity():
    """Tests that the function is case sensitive."""
    assert cycpattern_check("Hello", "ell") is True
    assert cycpattern_check("Hello", "ELL") is False
    assert cycpattern_check("Hello", "Ohel") is False # 'O' vs 'o'
    assert cycpattern_check("Hello", "ellh") is False # 'h' vs 'H'