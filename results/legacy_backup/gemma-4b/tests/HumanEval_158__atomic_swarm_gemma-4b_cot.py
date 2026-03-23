import pytest
import math

def test_basic():
    assert find_max(["name", "of", "string"]) == "string"

import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_unique = 0
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            result = word
        elif unique_chars == max_unique and word < result:
            result = word

    return result
    
def test_edge_empty_list():
    assert find_max([]) == ""

import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_unique = 0
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            result = word
        elif unique_chars == max_unique and word < result:
            result = word

    return result
    
def test_empty_list():
    assert find_max([]) == ""