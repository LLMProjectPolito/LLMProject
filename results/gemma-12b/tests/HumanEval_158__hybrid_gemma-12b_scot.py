
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

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_multiple_words_different_unique_chars(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_multiple_words_same_unique_chars_lexicographical(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_words_with_repeated_chars(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_empty_string_in_list(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_mixed_lengths_and_uniques(self):
        assert find_max(["abc", "ab", "a", "abcd"]) == "abcd"

    def test_all_same_word(self):
        assert find_max(["hello", "hello", "hello"]) == "hello"

    def test_list_with_numbers_and_letters(self):
        assert find_max(["a1b2", "abc", "a1"]) == "abc"

    def test_all_same_length_strings(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_all_same_unique_chars(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_list_with_only_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_mixed_empty_and_long_strings(self):
        assert find_max(["", "abcdefghijklmnopqrstuvwxyz"]) == "abcdefghijklmnopqrstuvwxyz"