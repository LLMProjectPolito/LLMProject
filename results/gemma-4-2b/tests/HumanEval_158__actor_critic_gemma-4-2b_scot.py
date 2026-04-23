
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

    max_unique_chars = 0
    max_unique_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_unique_word = word
        elif unique_chars == max_unique_chars and word < max_unique_word:
            max_unique_word = word

    return max_unique_word


def test_basic_case():
    assert find_max(["name", "of", "string"]) == "string"

def test_tie_case():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_empty_list():
    assert find_max([]) == ""

def test_all_same_characters():
    assert find_max(["aaaaaaa", "bb"]) == "aaaaaaa"

def test_empty_string_in_list():
    assert find_max(["", "abc"]) == "abc"

def test_mixed_case():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_single_word_list():
    assert find_max(["hello"]) == "hello"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_empty_string_list():
    assert find_max(["", ""]) == ""

def test_case_sensitivity():
    assert find_max(["abc", "ABC", "def"]) == "abc"