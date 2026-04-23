
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
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word

    return result

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_multiple_words_same_unique_chars_lexicographical_2():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_multiple_words_same_unique_chars_lexicographical_3():
    assert find_max(["abc", "cba", "bac"]) == "abc"

def test_word_with_all_same_chars():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_word_with_all_same_chars_2():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_mixed_case():
    assert find_max(["aA", "bB"]) == "aA"

def test_empty_string():
    assert find_max([""]) == ""

def test_string_with_spaces():
    assert find_max(["hello world", "goodbye"]) == "goodbye"

def test_long_string():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_duplicate_words():
  assert find_max(["abc", "abc", "def"]) == "abc"