
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

def test_find_max_positive():
    assert find_max(["name", "of", "string"]) == "string"

def test_empty_input():
    """Test with an empty list."""
    assert find_max([]) == ""

def test_find_max_empty_list():
    """Test with an empty list."""
    from solution import find_max
    assert find_max([]) == ""