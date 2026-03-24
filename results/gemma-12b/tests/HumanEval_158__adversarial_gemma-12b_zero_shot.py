
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


class TestFindMax:
    def test_empty_list(self):
        assert find_max([]) == ""

    def test_basic_case(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_lexicographical_tie(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_repeated_characters(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_mixed_lengths(self):
        assert find_max(["a", "aa", "aaa", "aaaa"]) == "a"

    def test_all_same_length_different_unique(self):
        assert find_max(["abc", "abd", "abe"]) == "abc"

    def test_all_same_length_same_unique(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_list_with_empty_string(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_list_with_only_empty_string(self):
        assert find_max([""]) == ""

    def test_list_with_duplicates(self):
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_list_with_special_characters(self):
        assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

    def test_list_with_numbers(self):
        assert find_max(["123", "456", "789"]) == "123"

    def test_list_with_mixed_characters(self):
        assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"

    def test_long_strings(self):
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "1234567890"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_unicode_characters(self):
        assert find_max(["你好世界", "こんにちは世界"]) == "你好世界"