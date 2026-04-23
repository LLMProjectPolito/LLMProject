
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

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_counts_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_words_same_unique_counts():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_mixed_case_words():
    assert find_max(["Hello", "world", "Python"]) == "Python"

def test_words_with_special_characters():
    assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

def test_words_with_numbers():
    assert find_max(["abc1", "def2", "ghi3"]) == "abc1"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdef"]) == "abcdefghijklmnopqrstuvwxyz"

def test_words_with_spaces():
    assert find_max(["hello world", "goodbye"]) == "hello world"

def test_words_with_unicode_characters():
    assert find_max(["你好世界", "hello"]) == "你好世界"

def test_duplicate_words():
    assert find_max(["hello", "hello", "world"]) == "hello"

def test_empty_string_in_list():
    assert find_max(["", "hello", "world"]) == "hello"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""