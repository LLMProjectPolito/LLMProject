
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
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return ""

    max_unique_count = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_count:
            max_unique_count = unique_chars
            result = word
        elif unique_chars == max_unique_count and word < result:
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
        assert find_max(["a", "aa", "aaa", "aaaa"]) == "aaaa"

    def test_all_same_length_different_unique(self):
        assert find_max(["abc", "abd", "abe"]) == "abc"

    def test_all_same_length_same_unique(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_duplicate_words(self):
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_words_with_spaces(self):
        assert find_max(["hello world", "hello", "world"]) == "hello world"

    def test_words_with_special_characters(self):
        assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

    def test_words_with_numbers(self):
        assert find_max(["123", "12", "1"]) == "123"

    def test_words_with_mixed_characters(self):
        assert find_max(["a1b2", "a1", "a"]) == "a1b2"

    def test_long_words(self):
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnop", "abcdef"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_case_sensitivity(self):
        assert find_max(["abc", "ABC"]) == "abc"

    def test_unicode_characters(self):
        assert find_max(["你好", "世界", "你好世界"]) == "你好世界"

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"