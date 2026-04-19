
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

def test_find_max_lexicographical_tie_with_varying_lengths():
    # All words have exactly 3 unique characters {a, b, c}.
    # Lexicographically: "abbc" < "abc" < "abcc"
    # "abbc" is smaller than "abc" because at index 2, 'b' < 'c'.
    # "abc" is smaller than "abcc" because it is a prefix of "abcc".
    assert find_max(["abc", "abbc", "abcc"]) == "abbc"

def test_find_max_tie_break_with_different_lengths():
    # All three words have 3 unique characters.
    # Lexicographically, "aabbcc" < "abc" < "xyz".
    assert find_max(["abc", "aabbcc", "xyz"]) == "aabbcc"

def test_find_max_case_sensitivity():
    # Both words have 4 unique characters.
    # "Apple" comes before "apple" lexicographically due to ASCII values ('A' < 'a').
    assert find_max(["apple", "Apple"]) == "Apple"