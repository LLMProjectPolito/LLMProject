import pytest
import math

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

    max_unique = -1
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

def test_example_1():
    assert find_max(["name", "of", "string"]) == "string"

def test_example_2():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_example_3():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_same_max_lexicographical():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_mixed_case():
    assert find_max(["Name", "name"]) == "Name"

def test_numbers_and_letters():
    assert find_max(["a1b2", "a1c2"]) == "a1b2"