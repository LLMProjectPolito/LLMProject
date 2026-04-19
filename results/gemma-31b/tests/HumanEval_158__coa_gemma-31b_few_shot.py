
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

def test_find_max_empty_string():
    assert find_max([""]) == ""

def test_find_max_lexicographical_tie():
    # Both have 1 unique character; "a" comes before "b" lexicographically
    assert find_max(["b", "a"]) == "a"

# Focus: Logic Branches
def test_find_max_clear_winner():
    # Branch: One word has a strictly greater number of unique characters
    assert find_max(["apple", "banana", "cherry"]) == "cherry"

def test_find_max_lexicographical_tie():
    # Branch: Multiple words have the same maximum unique characters; tie-break by lexicographical order
    assert find_max(["zebra", "beach", "apple"]) == "beach"

def test_find_max_unique_count_tie_different_lengths():
    # Branch: Words with different lengths but identical unique character counts
    assert find_max(["aaaaa", "bb", "ccc"]) == "aaaaa"

# Focus: Type Scenarios
def test_find_max_empty_list():
    assert find_max([]) == None

def test_find_max_empty_strings():
    assert find_max(["", ""]) == ""

def test_find_max_numeric_strings():
    assert find_max(["123", "456"]) == "123"