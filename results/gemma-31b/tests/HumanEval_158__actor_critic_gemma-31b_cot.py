
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

import pytest

def test_find_max_basic():
    """Test basic functionality with clear winners."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["a", "ab", "abc"]) == "abc"
    assert find_max(["hello", "world"]) == "world"  # hello: 4 (h,e,l,o), world: 5 (w,o,r,l,d)

def test_find_max_lexicographical_tie():
    """Test that lexicographical order is the tie-breaker for same unique character counts."""
    # All have 4 unique characters: enam, game, name. "enam" is first alphabetically.
    assert find_max(["name", "enam", "game"]) == "enam"
    # All have 3 unique characters: abc, bca, cab. "abc" is first.
    assert find_max(["cab", "bca", "abc"]) == "abc"
    # "apple" (a,p,l,e = 4) vs "pear" (p,e,a,r = 4). "apple" < "pear".
    assert find_max(["apple", "pear"]) == "apple"
    # All have 1 unique character. "aaaaaaa" < "bb" < "cc".
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    # All have 1 unique character. "xx" < "yy" < "zz".
    assert find_max(["zz", "yy", "xx"]) == "xx"

def test_find_max_empty_inputs():
    """Test behavior with empty lists and empty strings."""
    # Enforce a specific contract: return None for an empty list.
    assert find_max([]) is None
    # List containing empty strings: "" has 0 unique characters.
    assert find_max(["", "a"]) == "a"
    # Tie-break between empty strings.
    assert find_max(["", ""]) == ""

def test_find_max_whitespace():
    """Test that whitespace characters are counted as unique characters and sorted correctly."""
    # " a" (2 unique: ' ', 'a') vs "a" (1 unique: 'a').
    assert find_max([" a", "a"]) == " a"
    # " a" (2 unique) vs "a " (2 unique). " a" comes first lexicographically.
    assert find_max([" a", "a "]) == " a"
    # Tab (\t) vs Space ( ). Both 1 unique. Tab (ASCII 9) < Space (ASCII 32).
    assert find_max([" ", "\t"]) == "\t"

def test_find_max_case_sensitivity():
    """Test that case sensitivity is handled (usually 'A' != 'a')."""
    # "Aa" has 2 unique characters, "a" has 1.
    assert find_max(["Aa", "a"]) == "Aa"
    # "Apple" (A,p,l,e = 4) vs "apple" (a,p,l,e = 4). "Apple" < "apple" (Uppercase comes first in ASCII).
    assert find_max(["apple", "Apple"]) == "Apple"

def test_find_max_special_characters():
    """Test single elements and non-alphabetic characters."""
    assert find_max(["single"]) == "single"
    assert find_max(["123", "111", "222"]) == "123"
    assert find_max(["!@#", "$%^"]) == "!@#" # Both 3 unique, "!@#" < "$%^"