
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
from your_module import find_max  # Replace your_module

def test_empty_list():
    assert find_max([]) is None

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_repeated_chars():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_same_unique_chars_and_lexicographical_order():
    assert find_max(["abc", "bca", "cab"]) == "bca"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

def test_words_with_alphanumeric_characters():
    assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"

def test_words_with_unicode_characters():
    assert find_max(["你好", "世界", "Python"]) == "Python"

def test_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_words_with_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_words_with_numbers_as_strings():
    assert find_max(["123", "456", "789"]) == "123"

def test_words_with_mixed_empty_and_non_empty():
    assert find_max(["", "abc", ""]) == "abc"

def test_words_with_none_values():
    assert find_max(["abc", None, "def"]) == "abc"

def test_words_with_mixed_data_types():
    assert find_max(["abc", 123, "def"]) == "abc"

def test_long_list():
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == "a"