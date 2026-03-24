
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

    max_word = ""
    max_unique_chars = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word

    return max_word


def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["apple", "banana", "orange"]) == "orange"

def test_multiple_words_same_unique_chars_lexicographical_order():
    assert find_max(["enam", "name", "game"]) == "enam"

def test_all_same_characters():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_mixed_case():
    assert find_max(["Name", "enam", "Game"]) == "enam"

def test_numbers_and_letters():
    assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"

def test_find_max_with_duplicates():
    assert find_max(["apple", "apple", "banana"]) == "banana"

def test_find_max_with_empty_string():
    assert find_max(["", "apple", "banana"]) == "apple"