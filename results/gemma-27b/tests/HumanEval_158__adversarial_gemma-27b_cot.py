
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

def test_all_words_same_length():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_special_characters():
    assert find_max(["hello!", "world?", "python."]) == "python."

def test_words_with_numbers():
    assert find_max(["word1", "word22", "word333"]) == "word1"

def test_mixed_case_words():
    assert find_max(["Hello", "hello", "WORLD"]) == "Hello"

def test_words_with_spaces():
    assert find_max(["hello world", "hello", "world"]) == "hello world"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_duplicate_words():
    assert find_max(["hello", "hello", "world"]) == "hello"

def test_empty_string_in_list():
    assert find_max(["", "hello", "world"]) == "hello"

def test_list_with_only_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_words_with_unicode_characters():
    assert find_max(["你好", "世界"]) == "世界"