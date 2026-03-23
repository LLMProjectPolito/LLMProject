import pytest
from typing import List

def find_max(words: List[str]) -> str:
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

def test_words_with_repeated_chars():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_empty_string_in_list():
    assert find_max(["", "abc", "def"]) == "abc"

def test_mixed_lengths_and_unique_chars():
    assert find_max(["a", "bb", "ccc", "dddd"]) == "a"

def test_all_words_same_unique_chars():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc", "$%^"]) == "!@#"

def test_long_strings():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnop"]) == "abcdefghijklmnopqrstuvwxyz"

def test_unicode_strings():
    assert find_max(["你好", "世界", "你好世界"]) == "你好世界"