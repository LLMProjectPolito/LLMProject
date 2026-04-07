
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

def find_max(words):
    """
    Finds the longest word in a list of words.
    """
    if not words:
        return None
    return max(words, key=len)

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_single_word():
    assert find_max(["name"]) == "name"