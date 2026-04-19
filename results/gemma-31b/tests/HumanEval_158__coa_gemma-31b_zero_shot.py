
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

def test_find_max_single_element():
    assert find_max(["python"]) == "python"

def test_find_max_empty_strings():
    assert find_max(["", ""]) == ""

# Focus: Tie-breaking Logic
def test_tie_break_lexicographical_order():
    # Both "bat" and "cat" have 3 unique characters; "bat" comes first lexicographically
    assert find_max(["cat", "bat"]) == "bat"

def test_tie_break_same_unique_count_different_length():
    # Both have 1 unique character; "aaaaa" comes first lexicographically
    assert find_max(["bbbbb", "aaaaa"]) == "aaaaa"

def test_tie_break_multiple_candidates():
    # "abc", "abd", and "abe" all have 3 unique characters; "abc" is the lexicographical minimum
    assert find_max(["abe", "abd", "abc"]) == "abc"

# Focus: Unique Character Scenarios
def test_unique_character_counts():
    # Different number of unique characters
    assert find_max(["apple", "banana", "cherry"]) == "cherry"  # cherry: 5, apple: 4, banana: 3
    # All words have 1 unique character, return lexicographically first
    assert find_max(["zzzz", "aaaa", "bbbb"]) == "aaaa"

def test_unique_character_ties():
    # Same number of unique characters, different lengths
    assert find_max(["aabbcc", "abc"]) == "aabbcc"  # Both have 3, "aabbcc" < "abc"
    # Same number of unique characters, same length
    assert find_max(["cat", "bat", "rat"]) == "bat"  # All have 3, "bat" is smallest