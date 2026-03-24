
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
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_unique = 0
    max_word = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique and word < max_word:
            max_word = word
    return max_word

def test_empty_list():
    assert find_max([]) == ""

def test_single_element():
    assert find_max(["hello"]) == "hello"

def test_basic_case():
    assert find_max(["name", "of", "string"]) == "string"

def test_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_same_length():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_multiple_max_unique():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_strings_with_duplicates():
    assert find_max(["hello", "world", "python"]) == "python"

def test_mixed_lengths():
    assert find_max(["a", "aa", "aaa", "aaaa"]) == "aaaa"

def test_same_unique_count_different_lengths():
    assert find_max(["abc", "ab"]) == "abc"