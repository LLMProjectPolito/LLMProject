
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


# Focus: Boundary Values
def test_find_max_empty_list():
    assert find_max([]) == None

def test_find_max_empty_strings():
    assert find_max(["", ""]) == ""

def test_find_max_single_char_tie():
    assert find_max(["b", "a"]) == "a"

# Focus: Tie-breaking Logic
def test_find_max_tie_break_lexicographical():
    # Both "bat" and "cat" have 3 unique characters. "bat" comes first lexicographically.
    assert find_max(["cat", "bat"]) == "bat"
    # Both "apple" and "apply" have 4 unique characters. "apple" comes first lexicographically.
    assert find_max(["apply", "apple"]) == "apple"

def test_find_max_tie_break_anagrams():
    # "listen" and "silent" have the same unique characters (6). "listen" comes first lexicographically.
    assert find_max(["silent", "listen"]) == "listen"

def test_find_max_tie_break_multiple_options():
    # "beach" (5), "zebra" (5), and "apple" (4). "beach" comes before "zebra".
    assert find_max(["zebra", "beach", "apple"]) == "beach"

# Focus: String Composition
def test_string_composition_lexicographical_tie():
    # Both "apple" and "pear" have 4 unique characters; "apple" comes first lexicographically
    assert find_max(["apple", "pear"]) == "apple"
    # All have 3 unique characters; "bat" is lexicographically smallest
    assert find_max(["cat", "dog", "bat"]) == "bat"

def test_string_composition_length_vs_uniqueness():
    # "aaaaa" is longer but has only 1 unique char; "abc" is shorter but has 3
    assert find_max(["aaaaa", "abc"]) == "abc"
    # "bb" has 1 unique char; "a" has 1 unique char; "a" is lexicographically smaller
    assert find_max(["bb", "a"]) == "a"

def test_string_composition_empty_and_special():
    # Testing empty strings and strings with single unique characters
    assert find_max(["", "a"]) == "a"
    assert find_max(["", ""]) == ""