
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
    if not words:
        return ""

    max_unique = -1
    max_word = ""

    for word in words:
        unique_count = len(set(word))
        if unique_count > max_unique:
            max_unique = unique_count
            max_word = word
        elif unique_count == max_unique:
            if word < max_word:
                max_word = word

    return max_word


def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_max_unique():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_find_max_with_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_find_max_long_strings():
    assert find_max(["abcdefg", "abc"]) == "abcdefg"

def test_find_max_mixed_case():
    assert find_max(["aBc", "AbC"]) == "AbC" #lexicographical order