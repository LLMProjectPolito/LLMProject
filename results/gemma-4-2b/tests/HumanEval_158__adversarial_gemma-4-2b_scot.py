
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


def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_max_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_all_same_characters():
    assert find_max(["aaaa", "bb", "cc"]) == "aaaa"

def test_words_with_special_characters():
    assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

def test_words_with_numbers():
    assert find_max(["123", "abc", "1234"]) == "1234"

def test_words_with_mixed_characters():
    assert find_max(["a1b2c", "d3e4f", "g5h6i"]) == "a1b2c"