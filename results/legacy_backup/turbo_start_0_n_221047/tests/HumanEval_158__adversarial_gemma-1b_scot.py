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

    max_unique_count = -1
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_count:
            max_unique_count = unique_chars
            max_word = word
        elif unique_chars == max_unique_count and word < max_word:
            max_word = word

    return max_word

import sys
def test_find_max_empty_list():
    assert find_max("") == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_same_max():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_words_different_lengths():
    assert find_max(["a", "bb", "ccc"]) == "ccc"

def test_find_max_words_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == ""