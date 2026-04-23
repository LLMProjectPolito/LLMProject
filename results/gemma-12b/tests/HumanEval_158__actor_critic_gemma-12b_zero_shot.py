
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

def test_multiple_words_same_unique_chars():
    assert find_max(["name", "enam", "game"]) == "name"  # First word with max unique chars

def test_numbers_as_strings_with_leading_zeros():
    assert find_max(["001", "123"]) == "001"

def test_mixed_case_and_unicode():
    assert find_max(["你好abc", "ABC"]) == "你好abc"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

def test_words_with_mixed_characters():
    assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"

def test_words_with_unicode_characters():
    assert find_max(["你好", "世界", "Python"]) == "Python"

def test_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_words_with_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_words_with_numbers_as_strings():
    assert find_max(["123", "456", "789"]) == "123"

def test_numbers_vs_strings():
    assert find_max(["123", "abc"]) == "123"

def test_case_sensitivity():
    assert find_max(["abc", "ABC"]) == "abc"

def test_words_with_long_strings():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "1234567890"]) == "abcdefghijklmnopqrstuvwxyz"

def test_same_unique_chars_lexicographical():
    assert find_max(["abc", "def", "ghi"]) == "abc"