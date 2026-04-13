
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

    def test_all_same_unique_chars(self):
        assert find_max(["abc", "cba", "bac"]) == "abc"

    def test_numbers_and_symbols(self):
        assert find_max(["123", "abc", "1234"]) == "1234"

    def test_special_characters(self):
        assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

    def test_mixed_case(self):
        assert find_max(["aBc", "AbC", "abc"]) == "AbC"

    def test_unicode_characters(self):
        assert find_max(["你好", "世界", "你好世界"]) == "你好世界"

    def test_long_strings(self):
        long_string1 = "abcdefghijklmnopqrstuvwxyz"
        long_string2 = "zyxwvutsrqponmlkjihgfedcba"
        assert find_max([long_string1, long_string2]) == long_string1

    def test_duplicate_words(self):
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_words_with_spaces(self):
        assert find_max(["hello world", "hello", "world"]) == "hello world"