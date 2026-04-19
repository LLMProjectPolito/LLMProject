
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
import math

def test_find_max_identical_unique_sets_lexicographical_tie():
    """
    Test case where multiple strings have the same number of unique characters
    and the same set of unique characters, forcing a tie-break via 
    lexicographical order.
    """
    # All strings have exactly 3 unique characters: {'a', 'b', 'c'}
    # Lexicographical order: "aabbcc" < "abccba" < "abc"
    words = ["aabbcc", "abccba", "abc"]
    assert find_max(words) == "aabbcc"

def test_find_max_case_sensitive_tie_breaker():
    # "apple" has 4 unique chars: {a, p, l, e}
    # "Apply" has 4 unique chars: {A, p, l, y}
    # "banana" has 3 unique chars: {b, a, n}
    # Both "apple" and "Apply" tie for max unique chars (4).
    # Lexicographically, "Apply" < "apple" because 'A' (65) < 'a' (97).
    assert find_max(["apple", "Apply", "banana"]) == "Apply"

def test_find_max_case_and_lexicographical_tie():
    """
    Test the tie-breaker where multiple words have the same max unique characters.
    'Apple' and 'apple' both have 4 unique characters {A/a, p, l, e}.
    Lexicographically, 'Apple' (ASCII 65) comes before 'apple' (ASCII 97).
    'Banana' has only 3 unique characters {B, a, n}.
    """
    words = ["apple", "Banana", "Apple"]
    assert find_max(words) == "Apple"