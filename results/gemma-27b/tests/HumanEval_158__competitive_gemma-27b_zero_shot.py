
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
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_words_with_special_characters():
    assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

def test_words_with_numbers():
    assert find_max(["123", "4567", "89"]) == "4567"

def test_words_with_mixed_characters():
    assert find_max(["a1b2", "c3d4e", "f5"]) == "c3d4e"

def test_words_with_duplicates():
    assert find_max(["aabbcc", "abc", "def"]) == "abc"

def test_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_words_with_only_duplicates():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_words_with_unicode_characters():
    assert find_max(["你好", "世界"]) == "世界"

def test_lexicographical_tiebreaker():
    assert find_max(["abc", "abd", "abe"]) == "abc"

def test_case_sensitivity():
    assert find_max(["abc", "Abc", "aBc"]) == "Abc"