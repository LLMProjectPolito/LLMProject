
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

    max_unique_chars = -1
    max_unique_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_unique_word = word
        elif unique_chars == max_unique_chars and word < max_unique_word:
            max_unique_word = word

    return max_unique_word

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_tie():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_same_chars():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_mixed_case():
    assert find_max(["a", "A", "b"]) == "a"

def test_long_word():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_duplicate_chars():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_empty_string():
    assert find_max([""]) == ""

def test_mixed_strings():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_complex_case():
    assert find_max(["abcde", "abcef", "abc"]) == "abcde"