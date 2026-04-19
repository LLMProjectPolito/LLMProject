
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
    # Both strings have exactly 3 unique characters ('a', 'b', 'c').
    # "abacaba" is lexicographically smaller than "abc" because 'a' < 'c' at the third index.
    assert find_max(["abc", "abacaba"]) == "abacaba"

def test_find_max_tie_lexicographical():
    assert find_max(["pale", "leap", "apple"]) == "apple"

def test_find_max_case_sensitivity():
    # Both strings have 4 unique characters; 'Apple' comes before 'apple' lexicographically (ASCII 'A' < 'a')
    assert find_max(["apple", "Apple"]) == "Apple"