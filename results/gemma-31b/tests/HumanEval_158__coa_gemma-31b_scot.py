
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

def test_find_max_lexicographical_tie():
    assert find_max(["abc", "abd"]) == "abc"

# Focus: Logic Branches
def test_find_max_clear_winner():
    # Tests the branch where one word has strictly more unique characters than others
    assert find_max(["apple", "banana", "cherry"]) == "cherry"

def test_find_max_lexicographical_tie():
    # Tests the branch where multiple words have the same max unique characters
    # "apple" and "pale" both have 4 unique characters; "apple" is lexicographically smaller
    assert find_max(["apple", "pale"]) == "apple"

def test_find_max_all_same_unique_count():
    # Tests the branch where all words have the same unique count (1)
    # "aaaaaaa" < "bb" < "cc"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

# Focus: Value Scenarios
def test_find_max_lexicographical_tie():
    # Both "apple" and "pear" have 4 unique characters; "apple" comes first lexicographically
    assert find_max(["apple", "pear"]) == "apple"

def test_find_max_clear_winner():
    # "python" has 6 unique characters, "world" has 5, "hello" has 4
    assert find_max(["hello", "world", "python"]) == "python"

def test_find_max_all_same_unique_count():
    # All have 1 unique character; "aaaaa" comes first lexicographically
    assert find_max(["zz", "bb", "aaaaa"]) == "aaaaa"